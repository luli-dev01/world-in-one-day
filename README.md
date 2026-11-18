# The World in One Day — November 18, 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/luli-dev01/world-in-one-day/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/luli-dev01/world-in-one-day/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of **Wednesday, November 18, 2026**,
built for the [make.fun news-image-20261118 bounty](https://make.fun/bounty/news-image-20261118).

The image is a one-page newspaper front page:

- **Headline (Shenzhen):** Trump lands in Shenzhen; Xi greets him at the
  airport, in town for the APEC summit, with a first-ever trilateral
  with Xi and Putin following Thursday.
- **Crimea:** Ukraine blows a gap in the Crimea Bridge.
- **Gulf:** US jets strike Iran's Qeshm Island; tankers struck in Hormuz.
- **Health:** The US loses its measles-free status.
- **Space:** Voyager 1 is now one light-day from home.
- **Siberia:** A Russian military plane crashes in Siberia.
- **Climate:** Earthshot Prize — five winners, $1.3m each.

Plus an "ALSO TODAY" footer with the day's other stories. Sources:
AP, AFP and Reuters via The Japan Times, NDTV, The Manila Times,
Qatar Tribune and Outlook India.

## How it works

- `gen_image.py` draws the page deterministically with Pillow (DejaVu fonts).
- `entry.png` is the generated 1024×1024 image.
- `main.py` is the competition entrypoint (Python 3.13, standard library
  only): it copies `entry.png` to `/output/entry.png`, or to
  `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set. Running it
  twice produces byte-identical output.
