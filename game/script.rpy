# 이 파일에 게임 스크립트를 입력합니다.

# 캐릭터 그림이 준비되면 아래 이미지 경로를 바꿉니다.
image dummy_character = "images/characters/dummy.png"
image dummy_background = Solid("#dddcd0")
image room_window_background = "images/room_window.png"

define audio.bird = "audio/bird_sound_full.mp3"
define audio.ringtone = "audio/acapella_beatbox.mp3"

define smurf = Character("스머프", color="#2a8cce")
define mc = Character("나", color="#ffffff")

# 여기에서부터 게임이 시작합니다.
label start:

    scene black
    stop music fadeout 2.0

    centered "20XX년 12월 24일 . . ."
    with dissolve

    centered "Thursday"
    with Dissolve(3.0)

    #밝은 햇살이 방 창문으로 들어온다 겨울 눈오고있따'
    scene room_window_background
    
    

    " . . . "
    #참새소리
    play sound bird


    "창문 밖 으로 참 새가 지저귀는 소리가 들려온다"


    #전화소리

    play sound ringtone loop
    
    "갑자기 전화가 온다"

    "누가 전화했는지 보니 초등학교때부터 알고 지냈던 친구 녀석이다"

    "이녀석은 용건없이 절대 전화를 걸리가 없는데..."

    jump call_event
    
    return



label call_event:
    menu:
        "전화를 받을까?"

        "받기":
            stop sound
            jump connect_event
            return

        "안받기":
            stop sound
            jump disconnect_event

        "잠수타기":
            ". . ."
            ""
            "전화가 계속 울린다"
            jump call_event
    return


label disconnect_event:

    "하루종일 침대애 누운채로 아무것도없이 보냈다"

    return

label connect_event:

    "전화를 받았다"

    mc "아침부터 뭐야, 스머프?"

    "이녀석의 별명은 스머프다."

    show smurf_call at right with dissolve
    
    smurf "기합찬 아침! 해병 체조를 실시한다"
    
    mc "아침 댓바람 부터 무슨 귀신 시나락 까먹는 소리야?!"

    smurf "해병은 귀신을 대려잡는다 !"

    mc "그래그래 이런 평일 아침에 전화 건 이유가 뭐야?"

    smurf "워 워. 진정해, 너 별 일 없지?"

    mc "뭐 딱히.."

    smurf "하는 일도 없지?"

    "AI 시대의 여파로 몇 달 전부터 백수가 되버린 내 상황을 아는건지 모르는건지 짐작하는건지 그냥 내가 그럴거 같은 이미지인지 이 놈 생각은 알수가 없다"

    mc "어, 왜?"

    smurf "오, 진짜? 그렇단말이지.."

    mc "무슨 일인데"

    smurf "오늘이 무슨 날인지 알고있어?"

    "그렇다. 오늘은 12월 24일 빌어먹을 크리스마스 이브날이다. 하지만 내 입으로 꺼내긴 싫었다."

    mc "목요일"
    
    smurf "오늘 크리스마스 이브잖아, 몰랐던거냐? 밖에도 좀 나가고 하라고. 나무 장식같은것도 좀 해놨을텐데."
    
    mc "어차피 나는 매일 공휴일이나 마찬가지야"

    smurf "이자식 완전히 백수생활에 적응해버렸군, 부탁이 하나 있는데 들어줄래?"

    mc "뭔데? 말해봐"

    smurf "내가 몇 달 전부터 여자친구가 생겨서 말이야..."

    mc "이런 샹!"

    "이런 녀석도 여자친구가 생겨버렸는데 나만 메리솔로크리스마스이브라니, 저절로 짜증이 올라왔다."

    smurf "부탁이야. 제발. 크리스마스 까지만 대타 뛰어줄 수 있어?"

    "스머프 랑은"

    
    
