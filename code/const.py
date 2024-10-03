

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


#（x坐标，y坐标）  右下为正方向
MOV_DIR = {
    "UP":(0,-1),
    "DOWN":(0,1),
    "LEFT":(-1,0),
    "RIGHT":(1,0)
}

snake_color = {
    0: WHITE,
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


def get_action(now,des,dir):
    if des[0] >= now[0] and des[1] >= now[1]: # 在右下
        actions = ["DOWN","RIGHT","UP","LEFT"]
    
    if des[0] >= now[0] and des[1] <= now[1]: # 在右上
        actions = ["RIGHT","UP","LEFT","DOWN"]
    
    if des[0] <= now[0] and des[1] <= now[1]: # 在左上
        actions = ["UP","LEFT","DOWN","RIGHT"]
    
    if des[0] <= now[0] and des[1] >= now[1]: # 在左下
        actions = ["LEFT","DOWN","RIGHT","UP"]
    
    if dir == "UP":
        actions.remove("DOWN")
    if dir == "DOWN":
        actions.remove("UP")
    if dir == "LEFT":
        actions.remove("RIGHT")
    if dir == "RIGHT":
        actions.remove("LEFT")
    return actions