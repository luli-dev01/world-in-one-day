#!/usr/bin/env python3
"""Draw 'The World in One Day' - a one-page newspaper for 2026-11-18.
Deterministic PIL drawing, no randomness, no network."""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 242, 230)
INK = (26, 26, 26)
MUTED = (90, 84, 72)
RULE = (26, 26, 26)
CARD_BG = (255, 253, 247)
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, fnt, fill, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y

def icon_bridge(d, x, y, c):
    d.line([(x, y+50), (x+64, y+50)], fill=c, width=5)
    d.line([(x+8, y+50), (x+8, y+18)], fill=c, width=4)
    d.line([(x+56, y+50), (x+56, y+18)], fill=c, width=4)
    d.line([(x+8, y+18), (x+56, y+18)], fill=c, width=3)
    d.line([(x+8, y+18), (x+32, y+50)], fill=c, width=2)
    d.line([(x+56, y+18), (x+32, y+50)], fill=c, width=2)
    d.rectangle([x+27, y+46, x+37, y+54], fill=CARD_BG)

def icon_ship(d, x, y, c):
    d.polygon([(x+6, y+42), (x+58, y+42), (x+50, y+54), (x+14, y+54)], fill=c)
    d.rectangle([x+24, y+28, x+44, y+42], outline=c, width=3)
    d.rectangle([x+30, y+16, x+38, y+28], fill=c)
    d.arc([x+2, y+48, x+30, y+62], 0, 180, fill=c, width=2)
    d.arc([x+34, y+48, x+62, y+62], 0, 180, fill=c, width=2)

def icon_virus(d, x, y, c):
    d.ellipse([x+18, y+18, x+46, y+46], fill=c)
    for dx, dy in [(32,6),(50,14),(54,32),(50,50),(32,56),(14,50),(8,32),(14,14)]:
        d.line([(x+32, y+32), (x+dx, y+dy)], fill=c, width=3)
        d.ellipse([x+dx-4, y+dy-4, x+dx+4, y+dy+4], fill=c)
    for dx, dy in [(26,26),(38,30),(30,40)]:
        d.ellipse([x+dx-3, y+dy-3, x+dx+3, y+dy+3], fill=(255,253,247))

def icon_space(d, x, y, c):
    d.rectangle([x+26, y+10, x+40, y+26], fill=c)
    d.rectangle([x+4, y+12, x+22, y+24], outline=c, width=3)
    d.rectangle([x+44, y+12, x+62, y+24], outline=c, width=3)
    d.line([(x+33, y+26), (x+33, y+34)], fill=c, width=3)
    d.arc([x+16, y+34, x+50, y+58], 20, 160, fill=c, width=3)
    d.line([(x+33, y+46), (x+33, y+58)], fill=c, width=3)
    d.line([(x+22, y+58), (x+44, y+58)], fill=c, width=3)

def icon_plane(d, x, y, c):
    d.polygon([(x+6, y+18), (x+44, y+30), (x+58, y+38), (x+52, y+44), (x+34, y+38), (x+14, y+32)], fill=c)
    d.polygon([(x+20, y+28), (x+30, y+12), (x+36, y+13), (x+32, y+30)], fill=c)
    d.line([(x+10, y+52), (x+30, y+52)], fill=c, width=2)
    d.line([(x+38, y+56), (x+58, y+56)], fill=c, width=2)

def icon_leaf(d, x, y, c):
    d.ellipse([x+14, y+8, x+52, y+48], fill=c)
    d.line([(x+18, y+54), (x+48, y+14)], fill=(255,253,247), width=3)
    d.line([(x+18, y+54), (x+30, y+54)], fill=c, width=3)

ICONS = [icon_bridge, icon_ship, icon_virus, icon_space, icon_plane, icon_leaf]

CARDS = [
    ("CRIMEA", (185, 28, 28),
     "Ukraine blows a gap in the Crimea Bridge",
     "Zelensky confirms the strike partially wrecked the bridge."),
    ("GULF", (194, 65, 12),
     "US jets strike Iran's Qeshm Island",
     "Iran drones hit a US base in Kuwait; tankers struck in Hormuz."),
    ("HEALTH", (21, 101, 52),
     "US loses its measles-free status",
     "More than 5,400 cases in 2026 - the worst outbreak in three decades."),
    ("SPACE", (30, 64, 175),
     "Voyager 1 is now one light-day from home",
     "NASA's farthest spacecraft crosses the milestone 49 years after launch."),
    ("SIBERIA", (91, 33, 182),
     "Russian military plane crashes in Siberia",
     "An An-12 transport came down in the Kemerovo region; at least 17 killed."),
    ("CLIMATE", (22, 130, 60),
     "Earthshot Prize: five winners, $1.3m each",
     "Prince William honours green innovators at this year's awards."),
]

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([10, 10, W-11, H-11], outline=INK, width=3)
    d.rectangle([16, 16, W-17, H-17], outline=INK, width=1)
    f_title = font(SERIF_B, 58)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W-tw)/2, 26), title, font=f_title, fill=INK)
    d.line([(32, 102), (W-32, 102)], fill=RULE, width=3)
    d.text((32, 112), "Wednesday, November 18, 2026", font=font(SANS_B, 20), fill=(185, 28, 28))
    right = "World news - one page - one day"
    d.text((W-32-d.textlength(right, font=font(SANS, 16)), 115), right, font=font(SANS, 16), fill=MUTED)
    d.line([(32, 142), (W-32, 142)], fill=RULE, width=1)
    y = 154
    d.text((32, y), "SHENZHEN - APEC SUMMIT - HEADLINE", font=font(SANS_B, 17), fill=(185, 28, 28))
    y += 26
    y = draw_wrapped(d, 32, y, "Trump lands in Shenzhen; Xi greets him at the airport", font(SERIF_B, 39), INK, W-64, 46)
    y += 2
    y = draw_wrapped(d, 32, y, "In Shenzhen for the APEC summit; a first-ever trilateral with Xi and Putin follows Thursday.", font(SERIF, 19), MUTED, W-64, 25)
    y += 10
    d.line([(32, y), (W-32, y)], fill=RULE, width=2)
    y += 12
    margin, gap, cols = 32, 12, 2
    card_w = (W - margin*2 - gap) // cols
    card_h = 148
    f_label = font(SANS_B, 15)
    f_ctitle = font(SANS_B, 19)
    f_csub = font(SANS, 15)
    for i, (label, colour, ctitle, csub) in enumerate(CARDS):
        cx = margin + (i % cols) * (card_w + gap)
        cy = y + (i // cols) * (card_h + gap)
        d.rectangle([cx, cy, cx+card_w, cy+card_h], fill=CARD_BG, outline=(180, 172, 150), width=1)
        d.rectangle([cx, cy, cx+card_w, cy+6], fill=colour)
        ICONS[i](d, cx+14, cy+38, colour)
        tx = cx + 92
        tw2 = card_w - 92 - 12
        d.text((tx, cy+14), label, font=f_label, fill=colour)
        ty = draw_wrapped(d, tx, cy+36, ctitle, f_ctitle, INK, tw2, 23)
        draw_wrapped(d, tx, ty+3, csub, f_csub, MUTED, tw2, 19)
    y = y + 3 * (card_h + gap) + 4
    d.line([(32, y), (W-32, y)], fill=RULE, width=2)
    y += 8
    d.text((32, y), "ALSO TODAY", font=font(SANS_B, 16), fill=INK)
    y += 22
    also = ("Earthquakes - magnitude 6.0 off Papua New Guinea, 5.3 in Romania  |  "
            "Canada seeks a trade reset with China  |  Israel's Knesset elects a speaker backed by Netanyahu's rivals  |  "
            "Pakistani jailed 27 years in the US over a plot to kill Trump  |  "
            "Scientists: everyday chemicals cost the world $1 trillion a year")
    y = draw_wrapped(d, 32, y, also, font(SANS, 15), (50, 46, 38), W-64, 20)
    y += 6
    src = "Reporting: AP - AFP - Reuters via The Japan Times, NDTV, The Manila Times, Qatar Tribune and Outlook India."
    draw_wrapped(d, 32, y, src, font(SERIF, 13), MUTED, W-64, 17)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, format="PNG", optimize=False)
    print("wrote", out, os.path.getsize(out))

if __name__ == "__main__":
    main()
