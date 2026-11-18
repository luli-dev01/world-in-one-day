#!/usr/bin/env python3
"""Draw the news-image-20261118 front page: one image summing up the world
news of Wednesday 18 November 2026. Deterministic: pure PIL drawing."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)
INK = (26, 24, 22)
RED = (178, 34, 40)
BLUE = (30, 64, 140)
GRAY = (96, 92, 86)
CARD = (255, 253, 247)
RULE = (26, 24, 22)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def text_cx(cx, y, s, font, fill=INK):
    d.text((cx, y), s, font=font, fill=fill, anchor="ma")

def wrap(s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 112], fill=INK)
text_cx(W // 2, 14, "THE WORLD IN ONE DAY", F(SERIF_B, 58), fill=(247, 242, 231))
d.rectangle([0, 112, W, 118], fill=RED)
text_cx(W // 2, 126, "Wednesday, November 18, 2026  ·  One day of world news, in one picture",
        F(SANS_B, 21), fill=INK)

# ---------------- lead story ----------------
LY = 162
d.rectangle([28, LY, W - 28, LY + 248], fill=CARD, outline=RULE, width=3)
# lead illustration: skyline + three flags + plane
ix0, iy0, ix1, iy1 = 48, LY + 20, 400, LY + 228
d.rectangle([ix0, iy0, ix1, iy1], fill=(214, 228, 240))
d.rectangle([ix0, iy1 - 52, ix1, iy1], fill=(90, 110, 130))  # water/ground
for bx, bw, bh in [(60, 34, 90), (104, 26, 120), (140, 40, 76), (300, 30, 104), (340, 24, 84), (376, 30, 116)]:
    d.rectangle([bx, iy1 - 52 - bh, bx + bw, iy1 - 52], fill=(52, 66, 84))
# three flag poles with flags (China red, US blue canton, Russia white-blue-red)
for px, col in [(196, (222, 41, 47)), (238, (60, 59, 110)), (280, (240, 240, 240))]:
    d.line([px, iy1 - 52, px, iy1 - 176], fill=INK, width=4)
    d.rectangle([px, iy1 - 176, px + 34, iy1 - 148], fill=col, outline=INK, width=1)
d.rectangle([280, iy1 - 162, 314, iy1 - 155], fill=(30, 64, 175))
d.rectangle([280, iy1 - 155, 314, iy1 - 148], fill=(213, 0, 50))
# plane silhouette
d.polygon([(352, iy0 + 26), (392, iy0 + 40), (396, iy0 + 48), (360, iy0 + 46), (338, iy0 + 56), (344, iy0 + 42)],
          fill=INK)
lx = 424
d.text((lx, LY + 18), "SHENZHEN, CHINA", font=F(SANS_B, 19), fill=RED)
ly = LY + 46
for line in wrap("Trump lands in Shenzhen; Xi greets him at the airport", F(SERIF_B, 34), W - 28 - lx - 18):
    d.text((lx, ly), line, font=F(SERIF_B, 34), fill=INK)
    ly += 41
ly += 4
for line in wrap("In Shenzhen for the APEC summit; a first-ever trilateral "
                 "with Xi and Putin follows Thursday.", F(SERIF, 21), W - 28 - lx - 18):
    d.text((lx, ly), line, font=F(SERIF, 21), fill=(52, 50, 46))
    ly += 27

# ---------------- story cards ----------------
def icon_bridge(x, y, s):
    d.line([x, y + s * 0.62, x + s * 0.40, y + s * 0.62], fill=BLUE, width=7)
    d.line([x + s * 0.62, y + s * 0.62, x + s, y + s * 0.62], fill=BLUE, width=7)
    for fx in (0.08, 0.88):
        d.line([x + s * fx, y + s * 0.22, x + s * fx, y + s * 0.62], fill=BLUE, width=4)
    d.line([x, y + s * 0.22, x + s, y + s * 0.22], fill=BLUE, width=4)
    d.line([x + s * 0.40, y + s * 0.66, x + s * 0.50, y + s * 0.86], fill=RED, width=4)
    d.line([x + s * 0.62, y + s * 0.66, x + s * 0.54, y + s * 0.86], fill=RED, width=4)
    d.line([x + s * 0.06, y + s * 0.94, x + s * 0.94, y + s * 0.94], fill=BLUE, width=3)

def icon_ship(x, y, s):
    d.polygon([(x + s * 0.1, y + s * 0.62), (x + s * 0.9, y + s * 0.62), (x + s * 0.78, y + s * 0.82),
               (x + s * 0.22, y + s * 0.82)], fill=(70, 70, 76))
    d.rectangle([x + s * 0.38, y + s * 0.42, x + s * 0.62, y + s * 0.62], fill=(120, 124, 130))
    d.polygon([(x + s * 0.68, y + s * 0.10), (x + s * 0.76, y + s * 0.30), (x + s * 0.60, y + s * 0.30)], fill=RED)
    d.line([x, y + s * 0.92, x + s, y + s * 0.92], fill=BLUE, width=4)

def icon_virus(x, y, s):
    cx, cy, r = x + s / 2, y + s / 2, s * 0.26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED)
    import math
    for a in range(0, 360, 45):
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        d.line([cx + dx * r, cy + dy * r, cx + dx * s * 0.44, cy + dy * s * 0.44], fill=RED, width=5)
        d.ellipse([cx + dx * s * 0.44 - 5, cy + dy * s * 0.44 - 5, cx + dx * s * 0.44 + 5, cy + dy * s * 0.44 + 5], fill=RED)
    for dx, dy in [(-0.1, -0.06), (0.11, 0.05), (0.0, 0.13)]:
        d.ellipse([cx + dx * s - 4, cy + dy * s - 4, cx + dx * s + 4, cy + dy * s + 4], fill=(255, 220, 220))

def icon_craft(x, y, s):
    d.polygon([(x + s * 0.34, y + s * 0.30), (x + s * 0.52, y + s * 0.16), (x + s * 0.60, y + s * 0.24),
               (x + s * 0.42, y + s * 0.38)], fill=(110, 118, 128))
    d.rectangle([x + s * 0.10, y + s * 0.08, x + s * 0.30, y + s * 0.26], fill=(70, 110, 180))
    d.rectangle([x + s * 0.48, y + s * 0.34, x + s * 0.68, y + s * 0.52], fill=(70, 110, 180))
    d.arc([x + s * 0.08, y + s * 0.52, x + s * 0.62, y + s * 1.02], start=300, end=60, fill=INK, width=5)
    d.line([x + s * 0.35, y + s * 0.72, x + s * 0.35, y + s * 0.94], fill=INK, width=5)
    d.line([x + s * 0.20, y + s * 0.94, x + s * 0.50, y + s * 0.94], fill=INK, width=5)
    for sx, sy in [(0.82, 0.10), (0.93, 0.34), (0.74, 0.52)]:
        d.text((x + s * sx, y + s * sy), "+", font=F(SANS_B, 20), fill=INK)

def icon_crash(x, y, s):
    import math
    cx, cy = x + s * 0.58, y + s * 0.52
    ang = math.radians(38)
    def P(dx, dy):
        return (cx + dx * math.cos(ang) - dy * math.sin(ang), cy + dx * math.sin(ang) + dy * math.cos(ang))
    d.polygon([P(-0.30 * s, 0), P(0.26 * s, -0.07 * s), P(0.36 * s, 0), P(0.26 * s, 0.07 * s), P(-0.30 * s, 0)], fill=(90, 96, 104))
    d.polygon([P(-0.02 * s, 0), P(-0.20 * s, 0.26 * s), P(-0.08 * s, 0.27 * s), P(0.10 * s, 0.02 * s)], fill=(90, 96, 104))
    d.polygon([P(-0.30 * s, 0), P(-0.38 * s, -0.16 * s), P(-0.26 * s, -0.02 * s)], fill=(90, 96, 104))
    for t in (0.52, 0.68, 0.84):
        px, py = cx - math.cos(ang) * s * t, cy - math.sin(ang) * s * t
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(150, 150, 150))
    d.line([x, y + s * 0.94, x + s, y + s * 0.88], fill=(255, 255, 255), width=5)
    d.line([x, y + s * 1.0, x + s, y + s * 0.94], fill=(180, 200, 220), width=4)

def icon_leaf(x, y, s):
    d.pieslice([x + s * 0.14, y + s * 0.06, x + s * 0.86, y + s * 0.78], start=300, end=120, fill=(46, 140, 74))
    d.line([x + s * 0.22, y + s * 0.86, x + s * 0.78, y + s * 0.20], fill=(30, 100, 52), width=4)
    d.ellipse([x + s * 0.36, y + s * 0.80, x + s * 0.64, y + s * 0.97], outline=(150, 110, 30), width=4)

def icon_quake(x, y, s):
    pts = []
    xs = [0.0, 0.18, 0.30, 0.40, 0.48, 0.56, 0.64, 0.76, 1.0]
    ys = [0.55, 0.55, 0.30, 0.72, 0.12, 0.88, 0.38, 0.55, 0.55]
    for fx, fy in zip(xs, ys):
        pts.append((x + s * fx, y + s * fy))
    d.line(pts, fill=RED, width=5, joint="curve")

CARDS = [
    ("CRIMEA", icon_bridge, "Ukraine blows a gap in the Crimea Bridge",
     "Zelensky confirms the strike partially wrecked the bridge."),
    ("GULF", icon_ship, "US jets strike Iran's Qeshm Island",
     "Iran drones hit a US base in Kuwait; tankers struck in Hormuz."),
    ("HEALTH", icon_virus, "US loses its measles-free status",
     "More than 5,400 cases in 2026 — the worst outbreak in three decades."),
    ("SPACE", icon_craft, "Voyager 1 is now one light-day from home",
     "NASA's farthest spacecraft crosses the milestone 49 years after launch."),
    ("SIBERIA", icon_crash, "Russian military plane crashes in Siberia",
     "An An-12 transport came down in the Kemerovo region; at least 17 killed."),
    ("CLIMATE", icon_leaf, "Earthshot Prize: five winners, $1.3m each",
     "Prince William honours green innovators at this year's awards."),
]

GX, GY = 28, 426
CW = (W - 56 - 18) // 2
CH = 148
for i, (tag, icon, head, dek) in enumerate(CARDS):
    col = i % 2
    row = i // 2
    x0, y0, wdt = GX + col * (CW + 18), GY + row * (CH + 12), CW
    d.rectangle([x0, y0, x0 + wdt, y0 + CH], fill=CARD, outline=RULE, width=2)
    d.text((x0 + 18, y0 + 10), tag, font=F(SANS_B, 16), fill=RED)
    icon(x0 + 18, y0 + 36, 84)
    tx = x0 + 122
    ty = y0 + 34
    for line in wrap(head, F(SERIF_B, 24), x0 + wdt - tx - 14):
        d.text((tx, ty), line, font=F(SERIF_B, 24), fill=INK)
        ty += 29
    ty += 4
    for line in wrap(dek, F(SANS, 18), x0 + wdt - tx - 14):
        d.text((tx, ty), line, font=F(SANS, 18), fill=(52, 50, 46))
        ty += 22

# ---------------- footer ----------------
FY = 904
d.rectangle([0, FY, W, FY + 3], fill=RULE)
also = ("ALSO TODAY:  Earthquakes — magnitude 6.0 off Papua New Guinea, 5.3 in Romania  ·  Canada seeks a "
        "trade reset with China  ·  Israel's Knesset elects a speaker backed by Netanyahu's rivals  ·  "
        "Pakistani jailed 27 years in the US over a plot to kill Trump  ·  Scientists: everyday chemicals "
        "cost the world $1 trillion a year")
fy = FY + 10
for line in wrap(also, F(SANS_B, 17), W - 56):
    text_cx(W // 2, fy, line, F(SANS_B, 17), fill=INK)
    fy += 22
text_cx(W // 2, fy + 4, "Reporting: AP · AFP · Reuters via The Japan Times, NDTV, The Manila Times, Qatar Tribune and Outlook India",
        F(SANS, 16), fill=GRAY)

img.save("/home/hatch/workspace/makefun/news-image/entry_draft.png", optimize=True)
import os
print("saved", os.path.getsize("/home/hatch/workspace/makefun/news-image/entry_draft.png"), "bytes")
