#!/usr/bin/env python3
"""Draw the front-page image for the make.fun bounty
"Sum up 22 November's world news in one image" (news-image-20261122).

The picture is a newspaper front page drawn from scratch with PIL: a navy
masthead, five numbered rows for the day's biggest stories, and a footer.
No AI image generator, no network calls, nothing read besides the fonts
installed on this machine.

Run it and it writes assets/entry.png — a 1024x1024 PNG.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1024, 1024
OUT = Path(__file__).resolve().parent.parent / "assets" / "entry.png"

# Colours.
PAPER = (250, 247, 240)
NAVY = (16, 38, 59)
INK = (20, 32, 46)
BODY = (61, 74, 87)
MUTED = (120, 128, 138)
GOLD = (232, 179, 75)
RULE = (214, 208, 196)
WHITE = (255, 255, 255)

# Geometry.
MASTHEAD_H = 148
EDGE = 48
BADGE_X = 48
COPY_X = 132
ROW_TOP = 204
ROW_H = 140
ROW_GAP = 8

# The five stories of Sunday 22 November 2026: section tag, badge colour,
# a headline that fits on one line, and a summary of at most two lines.
STORIES = [
    ("CLIMATE", (29, 78, 137),
     "COP31 climate talks collapse with no deal",
     "The Antalya summit ends on Sunday with no agreement after the EU rejects a draft that says nothing about fossil fuels."),
    ("UKRAINE", (109, 40, 217),
     "Russian drone hits flats near Kyiv; 14 missing",
     "A drone strike on a five-storey block in Dymer leaves 14 people missing as rescuers search through the rubble."),
    ("GULF", (194, 65, 12),
     "Iran strikes Bahrain site; Gulf states condemn",
     "Bahrain says Iranian projectiles hit an industrial site and injured two people; Gulf neighbours condemn the attack."),
    ("SPACE", (15, 118, 110),
     "BepiColombo reaches Mercury after 8 years",
     "The European-Japanese spacecraft slips into orbit around Mercury, though ESA reports a thruster glitch during the burn."),
    ("DISASTER", (180, 35, 24),
     "Indonesia factory fire leaves dozens missing",
     "A candy factory blaze in Cikande kills three; police remove 24 body bags as the search for missing workers resumes."),
]

DATE_LINE = "S U N D A Y  ·  2 2  N O V E M B E R  2 0 2 6"
FOOTER_LINE = "Summarised from major news outlets  ·  22 November 2026"


def _load_fonts():
    folder = Path("/usr/share/fonts/truetype/dejavu")
    return {
        "title": ImageFont.truetype(str(folder / "DejaVuSerif-Bold.ttf"), 66),
        "kicker": ImageFont.truetype(str(folder / "DejaVuSerif.ttf"), 24),
        "headline": ImageFont.truetype(str(folder / "DejaVuSans-Bold.ttf"), 31),
        "summary": ImageFont.truetype(str(folder / "DejaVuSans.ttf"), 23),
        "small": ImageFont.truetype(str(folder / "DejaVuSans.ttf"), 20),
        "tag": ImageFont.truetype(str(folder / "DejaVuSans-Bold.ttf"), 21),
        "number": ImageFont.truetype(str(folder / "DejaVuSans-Bold.ttf"), 26),
    }


def _wrap(pen, text, font, width):
    """Greedy-wrap a summary into at most two lines of at most `width` px."""
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if pen.textlength(trial, font=font) <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > 2:
        raise ValueError(f"summary needs {len(lines)} lines: {text!r}")
    return lines


def _centred(pen, text, y, font, colour):
    pen.text(((WIDTH - pen.textlength(text, font=font)) / 2, y),
             text, font=font, fill=colour)


def _masthead(pen, fonts):
    pen.rectangle([0, 0, WIDTH, MASTHEAD_H], fill=NAVY)
    _centred(pen, "THE WORLD TODAY", 26, fonts["title"], WHITE)
    _centred(pen, DATE_LINE, 106, fonts["small"], GOLD)


def _row(pen, fonts, number, story, top, divider):
    tag, colour, headline, summary = story
    copy_w = WIDTH - EDGE - COPY_X
    if pen.textlength(headline, font=fonts["headline"]) > copy_w:
        raise ValueError(f"headline too long for one line: {headline!r}")
    # Numbered round badge.
    pen.ellipse([BADGE_X, top + 8, BADGE_X + 56, top + 64], fill=colour)
    digit = str(number)
    pen.text((BADGE_X + (56 - pen.textlength(digit, font=fonts["number"])) / 2,
              top + 18), digit, font=fonts["number"], fill=WHITE)
    # Tag, headline, then the wrapped summary.
    pen.text((COPY_X, top + 2), tag, font=fonts["tag"], fill=colour)
    pen.text((COPY_X, top + 30), headline, font=fonts["headline"], fill=INK)
    for i, line in enumerate(_wrap(pen, summary, fonts["summary"], copy_w)):
        pen.text((COPY_X, top + 74 + i * 30), line,
                 font=fonts["summary"], fill=BODY)
    if divider:
        pen.line([EDGE, top + ROW_H - 4, WIDTH - EDGE, top + ROW_H - 4],
                 fill=RULE, width=2)


def build():
    page = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    pen = ImageDraw.Draw(page)
    fonts = _load_fonts()

    _masthead(pen, fonts)

    _centred(pen, "Five stories that defined the day", 160,
             fonts["kicker"], BODY)
    pen.line([EDGE, 196, WIDTH - EDGE, 196], fill=RULE, width=2)

    for i, story in enumerate(STORIES):
        _row(pen, fonts, i + 1, story,
             ROW_TOP + i * (ROW_H + ROW_GAP),
             divider=i < len(STORIES) - 1)

    _centred(pen, FOOTER_LINE, 966, fonts["small"], MUTED)
    _centred(pen, "Code-rendered summary image", 992, fonts["small"], MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    page.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}  {OUT.stat().st_size} bytes  {page.size}")


if __name__ == "__main__":
    build()
