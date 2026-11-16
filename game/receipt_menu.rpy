# Image buttons keep native Ren'Py actions, keyboard focus and self-voicing labels.
init offset = -1

transform receipt_focus:
    subpixel True
    on idle:
        ease 0.16 xoffset 0 yoffset 0
    on hover:
        easeout 0.12 xoffset 5 yoffset -1
    on selected_idle:
        ease 0.16 xoffset 0 yoffset 0
    on selected_hover:
        easeout 0.12 xoffset 5 yoffset -1

transform receipt_arrive:
    alpha 0.0
    yoffset 5
    easeout 0.45 alpha 1.0 yoffset 0

screen receipt_button(asset, caption, target):
    imagebutton:
        id asset
        auto "gui/receipt/" + asset + "_%s.png"
        action target
        alt caption
        focus_mask None
        at receipt_focus
        hover_sound "gui/receipt/hover.wav"
        activate_sound "gui/receipt/click.wav"

define receipt_headings = {
    "불러오기": "load", "저장하기": "save", "환경설정": "config",
    "대사록": "history", "버전정보": "about", "조작방법": "help"
}
