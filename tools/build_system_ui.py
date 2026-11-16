"""Generate small, original UI frames; does not modify artwork or screen code."""
from pathlib import Path
from PIL import Image, ImageDraw

dest = Path(__file__).resolve().parents[1] / "game/gui/title"
dest.mkdir(parents=True, exist_ok=True)
for name, fill, border in [
    ("panel", "#fffaf4", "#bc9cac"),
    ("control", "#f8f0e9", "#c9abba"),
    ("control_hover", "#eee0ef", "#a17da0"),
    ("control_selected", "#ded0e3", "#957095"),
]:
    image = Image.new("RGBA", (64, 64))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, 63, 63), 8, fill=fill, outline=border, width=2)
    draw.rounded_rectangle((3, 3, 60, 60), 6, outline="#ffffff", width=1)
    image.save(dest / (name + ".png"))
