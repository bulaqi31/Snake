import pygame
from const import *
from game import *

class Battle_PVP(Survival_Pair):
    def __init__(self,window):
        self.window = window
        self.R_score = 0
        self.G_score = 0
        self.snakes = []
        self.points = []
        snake1 = Snake(1,(150,150),10,"RIGHT")
        snake2 = Snake(2,(150,300),10,"RIGHT")
        self.snakes.append(snake1)
        self.snakes.append(snake2)              # 一开始有两条蛇

        self.generate_time = time.time()        # 最近一次生成得分点的时间
        self.point_time = POINT_TIME            # 多久生成一个点
        self.start_time = time.time()           # 游戏开始时间
        self.generate_white_time = time.time()  # 上一次生成白点的时间
        self.white_point_time = POINT_TIME*15


    def update(self):    # 比较主干的一个函数
        if time.time() - self.generate_time > self.point_time:  # 时间到了，增加新的得分点
            self.AddPoint(1)
            self.AddPoint(2)                             # 应该改成红绿各增加一个
            self.generate_time = time.time()
        
        if time.time() - self.generate_white_time > self.white_point_time:  # 时间到了，增加新的得分点
            self.AddPoint(0)                            # 增加白色点
            self.generate_white_time = time.time()

        for snake in self.snakes:   # 更新蛇的信息
            snake.update()

        for point in self.points:   # 更新点的信息
            point.update()

        self.checkEating()
        self.checkPoints()          # 是否需要移除点
        self.checkCollide()         # 是否出现碰撞

    def AddPoint(self,property,pos_x=None,pos_y=None):
        new_property = property
        new_x,new_y = pos_x,pos_y
        new_pos = (new_x,new_y)
        if not (new_x or new_y):
            while True:
                list1 = self.snakes[0].list
                list2 = self.snakes[1].list                 # 两条蛇占据的位置
                new_x = random.randint(EDGE_LEFT//10,EDGE_RIGHT//10)*10
                new_y = random.randint(EDGE_TOP//10,EDGE_BUTTOM//10)*10             # 随机生成点的位置
                new_pos = (new_x,new_y)
                #print(new_pos)
                if new_pos not in list1 and new_pos not in list2:       # 没长在蛇身上
                    flag = 1
                    for point in self.points:
                        if new_pos == point.pos:
                            flag = 0
                            break
                    if flag:
                        break

        #for point in self.points:                       # 点的生成直接覆盖
        #    if point.pos == new_pos:
        #        self.points.remove(point)

        new_value = random.randint(30,50)               # 这里修改了一下 双人的变数小一点
        new_life = random.randint(19,21)                # 随机寿命
        if not property:                                # 白色点寿命长一些
            new_life *= 3                               # 寿命将近1分钟
        if property == 3:
            new_life = 99999
        #new_life = 99999
        new_point = Point(new_property,new_pos,new_value,new_life)
        self.points.append(new_point)

    def checkEating(self):          # 有没有点与蛇的位置重合
        # 这里应该改为给各自加分
        for point in self.points:
            pos_point = point.pos
            p_point = point.property
            for snake in self.snakes:
                if snake.pos == pos_point:
                    if p_point != snake.property and p_point: # 吃错颜色
                        snake.alive = 0
                    elif p_point:                             # 吃自己颜色
                        if snake.color == RED:
                            self.R_score += point.value
                        else:
                            self.G_score += point.value
                        point.exist = 0
                        snake.full += 5
                    else:                                     # 吃到白色
                        snake.full += 30                      # 长度直接加30
                        point.exist = 0

    def Gameover(self):     # 现在应该变成宣布谁赢
        # 创建字体对象，这里使用默认字体大小为50
        window = self.window
        snake1,snake2 = self.snakes[0],self.snakes[1]
        font = pygame.font.Font(None, 150)

        # 渲染文本
        if snake1.alive:
            text = "RED WIN!!!"
            color = RED
        elif snake2.alive:
            text = "GREEN WIN!!!"
            color = GREEN
        else:
            text = "DRAW!!!"
            color = WHITE

        text_surface = font.render(text, True, color)

        # 获取渲染文本的矩形对象
        text_rect = text_surface.get_rect()

        # 计算居中位置
        text_rect.center = (win_width // 2, win_height // 2)
        window.blit(text_surface, text_rect)

    def draw_score(self):
        window = self.window
        font = pygame.font.Font(None, 30)
        snake1,snake2 = self.snakes[0],self.snakes[1]

        # 渲染文本
        text1 = "Length: " + str(snake1.length)
        text2 = "Length: " + str(snake2.length)
        text1_surface = font.render(text1, True, LIGHT_RED)
        text2_surface = font.render(text2, True, GREEN)

        # 获取渲染文本的矩形对象
        text1_rect = text1_surface.get_rect()
        text2_rect = text2_surface.get_rect()

        # 计算位置
        text1_rect.left,text1_rect.top = (win_width//2-200, 0)
        text2_rect.left,text2_rect.top = (win_width//2+100, 0)
        window.blit(text1_surface, text1_rect)
        window.blit(text2_surface, text2_rect)

    def process(self,key):
        evt = pygame.key.name(key)
        #print(pygame.key.name(key))
        snake1 = self.snakes[0]
        snake2 = self.snakes[1]
        if evt == "a" or evt == "d" or evt == "w" or evt == "s":
            snake1.TURN(evt)
        elif evt == "left" or evt == "right" or evt == "up" or evt == "down" or evt == "enter":
            snake2.TURN(evt)
        elif evt == "space" and snake1.length >= 20:                # 长度大于20才能发动技能
            length = snake1.length
            points = snake1.list[-length//2:]
            snake1.HALF()                                           # 蛇变成一半
            for point in points:
                self.AddPoint(3,pos_x=point[0],pos_y=point[1])      # 生成永久地形

        elif evt == "right ctrl" and snake2.length >= 20:                # 长度大于20才能发动技能
            #print("***in process***")
            length = snake2.length
            points = snake2.list[-length//2:]
            snake2.HALF()                                           # 蛇变成一半
            for point in points:
                self.AddPoint(3,pos_x=point[0],pos_y=point[1])      # 生成永久地形