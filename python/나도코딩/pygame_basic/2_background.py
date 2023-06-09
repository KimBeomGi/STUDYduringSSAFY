import pygame

pygame.init()   # 초기화 해주는 작업(반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/dyd13/Desktop/my-today-ssafy-study/python/나도코딩/pygame_basic/background.png")

# 이벤트 루프
running = True      # 게임이 진행중인가? True면 진행중임
while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가? (pygame을 사용하려면 꼭 작성해야하는 것임.)
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False             # running은 False
    
    # screen.fill((0,0,255))
    screen.blit(background, (0,0))      # 배경 그리기
    
    pygame.display.update()             # 게임화면을 다시 그리기!(프레임마다 계속 그려줘야 우리눈에 보임)


# Pygame 종료
pygame.quit()
