[![make.fun bounty](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/3215242167-create/news-image-20261118-entry/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/3215242167-create/news-image-20261118-entry/reward.svg)](https://make.fun/bounty/news-image-20261118)

# The World Today — 18 November 2026 in one image

A newspaper front page summing up Wednesday 18 November 2026's world news, for make.fun's [Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118) bounty ($250 in USDC, 50 places paid).

## The image

`entry.png` (1024×1024, PNG) is drawn entirely in code (Python + PIL + Noto fonts) from headlines first reported on 18 November 2026 — no generated imagery, no AI-written text in the picture itself. Every word on the page was typeset by the render script; the program here only copies the finished page to the output.

**Lead story — the Gulf:** Iran's Revolutionary Guards launched drones at a US-operated radar at Sheikh Isa Air Base, Bahrain; Bahrain and US Central Command say the drones were intercepted with no damage. Hours later US jets hit a missile site on Qeshm Island, and Kuwait's defences engaged unidentified drones. *(Reuters, Al Jazeera)*

**Also on the page:**
- APEC opens in Shenzhen — Trump arrives from Manila; Xi hosts him and Putin for a first three-way meeting on Thursday. *(Le Monde, Reuters)*
- Ukraine hits the Crimea bridge for a second day, as Russian missiles pound bridges in Kyiv. *(Jagran Josh, Education Times)*
- Canada and China extend trade deals as Xi meets Carney ahead of APEC. *(Jagran Josh)*
- Britain sanctions eight firms over illegal West Bank settlements; Australia follows. *(Jagran Josh, EIN Presswire)*
- Cyclone Akvan intensifies over the Bay of Bengal; Andhra Pradesh and Odisha on high alert. *(Education Times)*
- Also today: the Board of Peace warns the Gaza ceasefire "faces imminent collapse"; NASA's Voyager 1 nears one light-day from Earth; India beat Pakistan 2–1 to lift a 10th SAFF title.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Python 3.13, standard library only, no network. Copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Deterministic: two runs write the same bytes.

## License

MIT — see `LICENSE`.
