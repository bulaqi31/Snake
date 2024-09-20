

GAME_SIZE = (1020,510)
win_width,win_height = GAME_SIZE
SNAKE_SIZE = 10
RED = (255,0,0)
LIGHT_RED = (255,150,150)
GREEN = (0,255,0)
LIGHT_GREEN = (150,255,150)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (180,0,180)
GRAY = (50,50,50)

MOV_DIR = {
    "UP":(0,-1),
    "DOWN":(0,1),
    "LEFT":(-1,0),
    "RIGHT":(1,0)
}

snake_color = {
    1: RED,
    2: GREEN
}
point_color = {
    0: PURPLE,
    1: LIGHT_RED,
    2: LIGHT_GREEN,
    3: BLUE
}

MOVING_TIME = 0.08
POINT_TIME = 3
EDGE_TOP = 20
EDGE_BUTTOM = win_height-30
EDGE_LEFT = 20
EDGE_RIGHT = win_width-30
