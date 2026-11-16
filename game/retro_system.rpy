# Receipt and field-notebook system windows. Loaded after the default screen styles.
init offset = 10

style game_menu_outer_frame:
    xpos 16
    ypos 24
    xsize 768
    ysize 552
    top_padding 65
    bottom_padding 48
    background Frame("gui/receipt/panel.png", 10, 10)

style game_menu_navigation_frame:
    xsize 174

style game_menu_content_frame:
    left_margin 16
    right_margin 16
    top_margin 7

style game_menu_viewport:
    xsize 546

style game_menu_label:
    xpos 39
    ypos 27
    ysize 58

style game_menu_label_text:
    size 27
    color "#536d68"
    outlines [(1, "#ffffff", 0, 0)]

style navigation_button:
    xsize 145
    ysize 32
    padding (12, 4)
    background Frame("gui/receipt/control.png", 10, 10)
    hover_background Frame("gui/receipt/control_hover.png", 10, 10)
    selected_background Frame("gui/receipt/control_selected.png", 10, 10)

style navigation_button_text:
    size 15
    color "#626057"
    hover_color "#536d68"
    selected_color "#355b50"
    insensitive_color "#b5a9b0"

style return_button:
    xpos 36
    yoffset -35

style slot_button:
    background Frame("gui/receipt/control.png", 10, 10)
    hover_background Frame("gui/receipt/control_hover.png", 10, 10)
    selected_background Frame("gui/receipt/control_selected.png", 10, 10)

style slot_button_text:
    color "#626057"
    hover_color "#536d68"
    selected_color "#355b50"

style page_label_text:
    color "#536d68"
    hover_color "#a96065"

style page_button_text:
    color "#8a816f"
    hover_color "#536d68"
    selected_color "#355b50"

style pref_label_text:
    color "#536d68"
    size 17

style pref_vbox:
    xsize 176

style radio_button:
    foreground None
    padding (10, 5)
    background Frame("gui/receipt/control.png", 10, 10)
    hover_background Frame("gui/receipt/control_hover.png", 10, 10)
    selected_background Frame("gui/receipt/control_selected.png", 10, 10)

style check_button:
    foreground None
    padding (10, 5)
    background Frame("gui/receipt/control.png", 10, 10)
    hover_background Frame("gui/receipt/control_hover.png", 10, 10)
    selected_background Frame("gui/receipt/control_selected.png", 10, 10)

style radio_button_text:
    color "#626057"
    hover_color "#536d68"
    selected_color "#355b50"

style check_button_text:
    color "#626057"
    hover_color "#536d68"
    selected_color "#355b50"

style radio_vbox:
    spacing 5

style check_vbox:
    spacing 5

style slider_vbox:
    xsize 260

style slider_slider:
    ysize 14
    left_bar Frame("gui/receipt/control_selected.png", 8, 6)
    right_bar Frame("gui/receipt/control.png", 8, 6)
    thumb Solid("#667e70", xsize=8, ysize=18)
    thumb_offset 4

style game_menu_vscrollbar:
    base_bar Solid("#e6dec9")
    thumb Solid("#a7ac95")

style about_text:
    color "#626057"

style about_label_text:
    color "#536d68"

style help_text:
    color "#626057"

style help_label_text:
    color "#536d68"

style help_button_text:
    color "#8a816f"
    hover_color "#536d68"
    selected_color "#355b50"

style history_text:
    color "#626057"

style confirm_frame:
    background Frame("gui/receipt/panel.png", 10, 10)

style confirm_prompt_text:
    color "#626057"

style confirm_button:
    padding (20, 8)
    background Frame("gui/receipt/control.png", 10, 10)
    hover_background Frame("gui/receipt/control_hover.png", 10, 10)

style confirm_button_text:
    color "#626057"
    hover_color "#536d68"
