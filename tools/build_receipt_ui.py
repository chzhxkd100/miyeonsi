"""Rebuild the original receipt/field-notebook UI artwork (no generated art)."""
from pathlib import Path
import math
import random
import struct
import wave
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "game/gui/receipt"
OUT.mkdir(parents=True, exist_ok=True)
FONT = str(ROOT / "game/SourceHanSansLite.ttf")
S = 3
INK = "#535653"
GREEN = "#536d68"
RED = "#a96065"

def font(size):
    return ImageFont.truetype(FONT, int(size * S))

def canvas(w, h):
    im = Image.new("RGBA", (w*S, h*S))
    return im, ImageDraw.Draw(im)

def line(d, xy, fill, width=1):
    d.line(tuple(round(v*S) for v in xy), fill=fill, width=max(1, round(width*S)))

def rect(d, xy, fill=None, outline=None, width=1):
    d.rectangle(tuple(round(v*S) for v in xy), fill=fill, outline=outline, width=max(1, round(width*S)))

def txt(d, xy, text, size, fill=INK, anchor=None):
    d.text((xy[0]*S, xy[1]*S), text, font=font(size), fill=fill, anchor=anchor)

def save(im, name):
    im.resize((im.width//S, im.height//S), Image.Resampling.LANCZOS).save(OUT / (name + ".png"))

def ticket(key, label, w, h, main=False):
    for state in ("idle", "hover", "selected_idle", "selected_hover", "insensitive"):
        active = state in ("hover", "selected_idle", "selected_hover")
        im, d = canvas(w, h)
        paper = "#fff9e8" if active else "#f4edda"
        edge = GREEN if active else "#a69c83"
        rect(d, (3, 4, w-2, h-1), "#665b4934")
        points = [(2*S, 2*S), ((w-7)*S, 2*S), ((w-2)*S, 7*S), ((w-2)*S, (h-4)*S), (2*S, (h-4)*S)]
        d.polygon(points, fill=paper, outline=edge, width=S)
        rng = random.Random(61)
        for _ in range(w*h//24):
            x, y = rng.randrange(4*S, (w-7)*S), rng.randrange(4*S, (h-6)*S)
            d.point((x,y), fill="#c7bba561")
        txt(d, (w/2, (h-4)/2), label, 19 if main else 14,
            GREEN if active else INK, anchor="mm")
        if active:
            d.polygon([(10*S,(h/2-5)*S),(14*S,(h/2-2)*S),(10*S,(h/2+1)*S)],fill=RED)
        if state == "insensitive":
            im.putalpha(im.getchannel("A").point(lambda a: int(a*.40)))
        save(im, key + "_" + state)

main = [
    ("start", "처음부터"),
    ("load", "불러오기"),
    ("quick", "빠른 불러오기"),
    ("config", "환경설정"),
    ("about", "제작정보"),
    ("quit", "끝내기"),
]
for key, label in main:
    ticket("main_" + key, label, 224, 48, True)

labels = {
    "start":"처음부터", "load":"불러오기", "save":"저장하기", "config":"환경설정",
    "history":"대사록", "title":"메인 메뉴", "about":"제작정보", "help":"조작방법",
    "quit":"끝내기", "return":"돌아가기", "replay":"리플레이 종료",
    "window":"창 화면", "fullscreen":"전체 화면", "unread":"안 읽은 지문",
    "after":"선택지 이후", "transitions":"전환 효과 생략", "mute":"모두 음소거",
    "yes":"예", "no":"아니오",
}
for key, label in labels.items():
    ticket(key, label, 146, 34)

# Small nine-slice assets: crisp paper borders, squared archival labels.
for name, fill, edge in [("panel", "#faf5e7", "#a49e87"), ("control", "#eee7d4", "#b2a78f"),
                         ("control_hover", "#faf0d8", GREEN), ("control_selected", "#d8e0d4", GREEN)]:
    im, d = canvas(64,64)
    rect(d, (1,1,62,62), fill, edge)
    rect(d, (4,4,59,59), None, "#fffbed")
    save(im,name)

for key, label in [("load","불러오기"),("save","저장하기"),
    ("config","환경설정"),("history","대사록"),
    ("about","제작정보"),("help","조작방법")]:
    im,d=canvas(330,52)
    txt(d,(2,1),label,25,GREEN)
    line(d,(0,51,327,51),"#c2b8a0",.7)
    save(im,"heading_"+key)

# Very quiet, short UI sounds generated locally.
for name, hz, duration in [("hover",900,.024),("click",560,.046)]:
    with wave.open(str(OUT / (name+".wav")),"wb") as f:
        f.setparams((1,2,22050,0,"NONE","not compressed"))
        samples=[]
        for i in range(int(duration*22050)):
            t=i/22050
            amp=.045 * math.sin(math.pi*t/duration)**2 * math.exp(-65*t)
            samples.append(struct.pack("<h",int(32767*amp*math.sin(2*math.pi*hz*t))))
        f.writeframes(b"".join(samples))

# Review sheet containing only the generated UI assets.
sheet = Image.new("RGB",(760,490),"#e4dfd1")
draw = ImageDraw.Draw(sheet)
for row, (key, _) in enumerate(main):
    for col,state in enumerate(("idle","hover","insensitive")):
        asset=Image.open(OUT/f"main_{key}_{state}.png")
        sheet.paste(asset,(15+col*250,15+row*62),asset)
for col,key in enumerate(("window","fullscreen","return","yes")):
    asset=Image.open(OUT/f"{key}_selected_idle.png")
    sheet.paste(asset,(15+col*185,415),asset)
sheet.save(ROOT / "tools/receipt-ui-preview.png")
print(f"Built {len(list(OUT.glob('*.png')))} PNG assets in {OUT}")
