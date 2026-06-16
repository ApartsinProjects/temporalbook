"""Composite the title/subtitle/authors onto the generated cover artwork.

Produces KDP/cover/cover_kdp.jpg: 1600x2560 baseline (non-progressive) sRGB JPEG.
Text is drawn with PIL (crisp), never baked by the image model.
"""
from PIL import Image, ImageDraw, ImageFont
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE / "generated_1.png"
OUT = HERE / "cover_kdp.jpg"
W, H = 1600, 2560

TITLE = "BUILDING TEMPORAL AI"
SUBTITLE = "From Forecasting to Sequential Decision Making"
AUTHORS = "Alexander Apartsin & Yehudit Aperstein"

ARIAL_BD = "C:/Windows/Fonts/arialbd.ttf"
ARIAL = "C:/Windows/Fonts/arial.ttf"


def fit_font(path, text, max_w, start, draw, min_size=24):
    s = start
    while s > min_size:
        f = ImageFont.truetype(path, s)
        if draw.textlength(text, font=f) <= max_w:
            return f
        s -= 2
    return ImageFont.truetype(path, min_size)


def wrap(text, font, max_w, draw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# 1. Canvas from art: scale to full height, center, pad sides with art's corner color
art = Image.open(ART).convert("RGB")
aw, ah = art.size
scale = H / ah
art2 = art.resize((round(aw * scale), H), Image.LANCZOS)
pad = art.getpixel((2, 2))  # dark navy corner
canvas = Image.new("RGB", (W, H), pad)
canvas.paste(art2, ((W - art2.width) // 2, 0))

# 2. Soft scrims (top for title contrast, bottom for author contrast)
scrim = Image.new("L", (1, H), 0)
for y in range(H):
    a = 0
    if y < int(H * 0.17):                      # top scrim
        a = int(150 * (1 - y / (H * 0.17)))
    if y > int(H * 0.86):                       # bottom scrim
        a = max(a, int(190 * (y - H * 0.86) / (H * 0.14)))
    scrim.putpixel((0, y), a)
scrim = scrim.resize((W, H))
navy = Image.new("RGB", (W, H), (6, 12, 30))
canvas = Image.composite(navy, canvas, scrim)

draw = ImageDraw.Draw(canvas)
margin = 110
maxw = W - 2 * margin

# 3. Title (bold, letter-spaced, white)
tf = fit_font(ARIAL_BD, TITLE, maxw, 150, draw)
# manual letter spacing
def draw_spaced(cx, y, text, font, fill, ls):
    total = sum(draw.textlength(c, font=font) for c in text) + ls * (len(text) - 1)
    x = cx - total / 2
    for c in text:
        draw.text((x, y), c, font=font, fill=fill)
        x += draw.textlength(c, font=font) + ls
    return font.getbbox(text)[3] - font.getbbox(text)[1]

th = draw_spaced(W // 2, int(H * 0.045), TITLE, tf, (255, 255, 255), 6)

# 4. Subtitle (regular, light, wrapped)
sf = fit_font(ARIAL, SUBTITLE, maxw, 70, draw)
slines = wrap(SUBTITLE, sf, maxw, draw)
y = int(H * 0.045) + th + 60
for ln in slines:
    w = draw.textlength(ln, font=sf)
    draw.text(((W - w) / 2, y), ln, font=sf, fill=(196, 214, 240))
    y += sf.getbbox(ln)[3] - sf.getbbox(ln)[1] + 18

# 5. Authors (regular, white, near bottom)
af = fit_font(ARIAL, AUTHORS, maxw, 62, draw)
aw_ = draw.textlength(AUTHORS, font=af)
ah_ = af.getbbox(AUTHORS)[3] - af.getbbox(AUTHORS)[1]
draw.text(((W - aw_) / 2, int(H * 0.945) - ah_), AUTHORS, font=af, fill=(244, 248, 255))

# 6. Save baseline sRGB JPEG
canvas.save(OUT, "JPEG", quality=92, progressive=False, optimize=True,
            icc_profile=None)
print("wrote", OUT, canvas.size)
