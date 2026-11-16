"""Draw original title-menu button assets without modifying screen code."""
from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
dest = root / "game/gui/title"
dest.mkdir(parents=True, exist_ok=True)
for name, fill, edge in [
    ("idle", (255, 247, 253, 240), "#cfa5ce"),
    ("hover", (246, 219, 243, 255), "#a86baa"),
]:
    im = Image.new("RGBA", (520, 68))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, 517, 65), radius=31, fill=fill, outline=edge, width=3)
    d.line((347, 6, 347, 61), fill="#dfc9e2", width=2)
    d.line((29, 7, 490, 7), fill="#ffffff", width=2)
    im.save(dest / f"button_{name}.png")

