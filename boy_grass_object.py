import random
from pico2d import *

# Game object class here
class Grass:
    def __init__( self ):  # 생성자
        self.image = load_image('grass.png')

    def draw( self ):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(-400, 400), 90
        self.frame = random.randint(0, 7)

    def update( self ):  # 소년의 행위 구현
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.balls = ['ball21x21.png', 'ball41x41.png']
        self.ball_type = random.randint(0, 1)
        self.ball_speed = random.randint(5, 20)
        self.image = load_image(self.balls[self.ball_type])
        self.x, self.y = random.randint(0, 799), 599

    def update(self):
        self.y -= self.ball_speed

        if self.ball_type == 0:
            if self.y <= 61:
                self.y = 61
                return
        elif self.ball_type == 1:
            if self.y <= 71:
                self.y = 71
                return

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

delay(5)

grass = Grass()  # 잔디 객체 생성

# team
team = [ Boy() for i in range(11) ]

balls = [ Ball() for i in range(20) ]

running = True

# game main loop code
while running:
    handle_events() # 키 입력 처리

    # Game logic
    # grass 상호작용
    for boy in team:
        boy.update()  # boy 상호작용

    for ball in balls:
        ball.update()

    # Game drawing
    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)

# finalization code