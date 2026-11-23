# Dossier — make.fun bounty "Sum up 22 November's world news in one image"

## Bounty (verified 23 Nov 2026, ~07:55 WIB)

- Bounty: **Sum up 22 November's world news in one image** — https://make.fun/bounty/news-image-20261122
- Slug: `news-image-20261122` · Prize: **$100, 50 places paid** (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each), USDC on Solana, escrow funded 2026-11-22. (Note: this edition's prize is $100, down from $250 on the 19–20 Nov editions.)
- Deadline: **Tuesday 24 Nov 2026, 07:00 WIB** (2026-11-24T00:00:00Z).
- Judging: an AI judge that can see images compares entries two at a time; the image itself must show the day's news (the judge has no news feed).
- Same format as the accepted 19, 20 and 21 Nov entries (world-today-20261119, world-today-20261120, world-today-20261121); this build reuses their verified render pipeline, with render.py, main.ts, README.md and DOSSIER.md rewritten fresh in-session.

## The image — five stories (checked 23 Nov against OneTurn 22 Nov brief, Reuters via Devdiscourse, AP/Reuters on BepiColombo, all dated 22 Nov 2026)

1. **CLIMATE — COP31 climate talks collapse with no deal.** The Antalya summit ends on Sunday with no agreement after the EU rejects a draft that says nothing about fossil fuels.
2. **UKRAINE — Russian drone hits flats near Kyiv; 14 missing.** A drone strike on a five-storey block in Dymer leaves 14 people missing as rescuers search through the rubble.
3. **GULF — Iran strikes Bahrain site; Gulf states condemn.** Bahrain says Iranian projectiles hit an industrial site and injured two people; Gulf neighbours condemn the attack.
4. **SPACE — BepiColombo reaches Mercury after 8 years.** The European-Japanese spacecraft slips into orbit around Mercury, though ESA reports a thruster glitch during the burn.
5. **DISASTER — Indonesia factory fire leaves dozens missing.** A candy factory blaze in Cikande kills three; police remove 24 body bags as the search for missing workers resumes.

Design: same newspaper front-page style as the 19/20/21 Nov entries — navy masthead "THE WORLD TODAY / SUNDAY · 22 NOVEMBER 2026", five numbered colour-tagged rows, footer citing major news outlets. Rendered in code with Python/PIL (`scripts/render.py`) — no AI image generator.

## Program

`main.ts` copies `assets/entry.png` to `/output/entry.png` — deterministic, no network. Verified locally: two runs byte-identical and equal to the source asset (sha256 bb81d0dd…5b975, 1024x1024, 124,171 bytes).
