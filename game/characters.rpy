# 캐릭터 세팅 코드


#정적 변수 (게임 중 변하지않는것)
define mystery_name = "???" # 미스터리 이름

#동적 변수 (게임 중 변해됨 세이브로드가능)
default player_name = "mc" # 플레이어 이름

#등장인물 1 주인공
default mc_color = "#00ff00" # 주인공 캐릭터 색상
default mc = Character(player_name, color=mc_color, image="mc") # 플레이어 캐릭터


#등장인물 2 주인공친구
# 동갑 친구
# 옛날 같이 햄버거 아르바이트 했음
# 여친보유
# 눈동자 큼 인싸이고 ADHD기질있음
# 현재 햄버거 가게에서 매니저임

default smurf = Character("스머프", color="#00ffff", image="smurf") # 스머프 캐릭터


# 여캐 1 김이른
# 1시타임에 교대하기로되어있어서 주인공이가게에 입장하는순간 카운터에있음
# 히든 루트(알바 하다가 도망가거나 일찍 끝내고 약속잡기) 로 가야 진행가능 가능
# 말 별로없음 노말타입

default irune_color = "#ff00ff" # 이른 캐릭터 색상
default irune_name = "이른" # 이른 캐릭터 이름
default irune_cilluete = Character(mystery_name, color=irune_color, image="irune_cilluete") # 이른 실루엣 캐릭터
default irune = Character(irune_name, color=irune_color, image="irune")
