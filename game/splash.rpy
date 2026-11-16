image company_logo = "images/kmhsoft_logo.png"

label splashscreen:
    
    scene black

    pause 1.0

    play music "<from 0 to 6>audio/tracking_signal.mp3" fadein 1.0 noloop

    show company_logo:
        xalign 0.5
        yalign 0.5
        zoom 0.12
        alpha 0.0
        linear 1.0 alpha 1.0

    pause 4.0

    stop music fadeout 2.0
    hide company_logo
    with Dissolve(2.0)

    pause 1.0

    return
