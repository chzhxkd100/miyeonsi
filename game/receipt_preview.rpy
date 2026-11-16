# Only enabled by the local visual-check launcher. No effect in ordinary play.
init python:
    import os
    if os.environ.get("RECEIPT_UI_PREVIEW") == "1":
        _receipt_check_step = 0

        def receipt_visual_check_step():
            global _receipt_check_step
            if not renpy.get_screen("main_menu") and _receipt_check_step == 0:
                return
            paths = ["tools/menu-main.png", "tools/menu-hover.png", "tools/menu-load.png", "tools/menu-config.png", "tools/menu-confirm.png"]
            renpy.screenshot(os.path.join(config.basedir, paths[_receipt_check_step]))
            _receipt_check_step += 1
            if _receipt_check_step == 1:
                renpy.set_focus("main_menu", "main_config")
            elif _receipt_check_step == 2:
                renpy.run(ShowMenu("load"))
            elif _receipt_check_step == 3:
                renpy.run(ShowMenu("preferences"))
            elif _receipt_check_step == 4:
                renpy.show_screen("confirm", message="기록을 덮고 종료할까요?", yes_action=NullAction(), no_action=Hide("confirm"))
            else:
                renpy.quit()

screen receipt_visual_check():
    timer 1.5 repeat True action Function(receipt_visual_check_step)
