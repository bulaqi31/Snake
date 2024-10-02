import pygame
import random
import time
from const import *
from snake import *
from point import *
from game import *

class Survival_Solo(Survival_Pair):
    def __init__(self,window,high_score):
        self.window = window
        self.score = 0
        self.high_score = high_score
        self.snakes = []
        self.points = []
        snake1 = Snake(1,(150,150),3,"RIGHT")
        snake2 = Snake(0,(150,300),3,"RIGHT")
        self.snakes.append(snake1)
        self.snakes.append(snake2)              # 一开始有两条蛇

        self.generate_time = time.time()        # 最近一次生成得分点的时间
        self.point_time = POINT_TIME            # 多久生成一个点
        self.start_time = time.time()           # 游戏开始时间
    
    def update(self):    # 比较主干的一个函数
        if time.time() - self.generate_time > self.point_time:  # 时间到了，增加新的得分点
            new_property = random.randint(1,2)
            self.AddPoint(new_property)
            self.generate_time = time.time()

        #这里的新蛇直接往最后一个点跑
        if self.points:
            destination = self.points[-1].pos
            now_pos = self.snakes[1].pos
            direction= self.snakes[1].direction
            action = get_action(now_pos,destination,direction)
            
            #print(action)
            snake2 = self.snakes[1]
            snake2.direction = action
            snake2.turn_pos = snake2.pos
        # 依照我的设想 小蛇不需要指令缓冲区

        for snake in self.snakes:   # 更新蛇的信息
            snake.update()

        for point in self.points:   # 更新点的信息
            point.update()

        self.checkEating()
        self.checkPoints()          # 是否需要移除点
        self.checkCollide()         # 是否出现碰撞
        self.new_snake()            # 判断是否需要生成新的障碍蛇
        if self.score > self.high_score:
            self.high_score = self.score

    def AddPoint(self,property,pos_x=None,pos_y=None):
        new_property = property
        new_x,new_y = pos_x,pos_y
        new_pos = (new_x,new_y)
        if not (new_x or new_y):         # 这句好像有点没必要
            while True:
                list1 = self.snakes[0].list
                list2 = self.snakes[1].list                 # 两条蛇占据的位置
                new_x = random.randint(EDGE_LEFT//10,EDGE_RIGHT//10)*10
                new_y = random.randint(EDGE_TOP//10,EDGE_BUTTOM//10)*10             # 随机生成点的位置
                new_pos = (new_x,new_y)
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

        new_value = random.randint(10,50)
        new_life = random.randint(9,11)                # 随机寿命
        if property == 3:
            new_life = 99999
        #new_life = 99999
        new_point = Point(new_property,new_pos,new_value,new_life)
        self.points.append(new_point)

    def process(self,key):
        evt = pygame.key.name(key)
        #print(pygame.key.name(key))
        if evt == "a" or evt == "d" or evt == "w" or evt == "s":
            self.snakes[0].TURN(evt)
        




    def draw(self):
        #print("***")
        window = self.window
        self.drawback()     #画背景
        self.draw_score()
        for snake in self.snakes:       # 画蛇
            snake.draw(window)
        for point in self.points:       # 画点
            point.draw(window)

        time.sleep(MOVING_TIME)

    
    def checkEating(self):          # 有没有点与蛇的位置重合
        for point in self.points:
            pos_point = point.pos
            p_point = point.property
            for snake in self.snakes:
                if snake.pos == pos_point:
                    if (p_point != snake.property and snake.property) or p_point == 3: # 吃错颜色 并且不是障碍蛇
                        snake.alive = 0
                    else:
                        point.exist = 0
                        snake.full += 3
                        if snake.property:                  # 障碍蛇吃东西不加分
                            self.score += point.value
                        else:                               # 障碍蛇一下增长10
                            snake.full += 7

    def checkPoints(self):
        for point in self.points:
            if point.exist == 0:
                self.points.remove(point)   # 已经去世或者被吃了
    
    def checkCollide(self):
        snake1 = self.snakes[0]
        snake2 = self.snakes[1]
        if snake1.pos in snake2.list:
            snake1.alive = 0
        if snake2.pos in snake1.list:
            snake2.alive = 0
            self.score += random.randint(50,100)

    # 这个模式应该增加一个 生成新的障碍蛇
    def new_snake(self):
        old_snake = self.snakes[1]
        if old_snake.alive:
            return False
        points = old_snake.list
        self.snakes.remove(old_snake)   
        for point in points:
            self.AddPoint(3,pos_x=point[0],pos_y=point[1])      # 生成永久地形
        self.generate_snake()

    def generate_snake(self):
        list1 = self.snakes[0].list # 自己这条蛇的位置
        flag = 0

        while not flag:
            new_x = random.randint(EDGE_LEFT//10,EDGE_RIGHT//10)*10
            new_y = random.randint(EDGE_TOP//10,EDGE_BUTTOM//10)*10             # 随机生成点的位置
            new_pos = (new_x,new_y)
            #print(new_pos)
            if new_pos not in list1:       # 没长在蛇身上
                flag = 1
                for point in self.points:
                    if new_pos == point.pos:
                        flag = 0
                        break

        new_snake = Snake(0,new_pos,1,"RIGHT")
        self.snakes.append(new_snake)

    def drawback(self):           # 把游戏背景画出来
        
        boundry_color = BLUE
        boundry_width = 20
        pygame.display.set_caption('Snake')
        window = self.window
        window.fill(GRAY)
        # 参数分别为：窗口对象，左上角坐标，宽度，高度，边框颜色，边框线宽
        pygame.draw.rect(window, boundry_color, (0, 0, win_width, win_height), boundry_width)

    def Gameover(self):
        # 创建字体对象，这里使用默认字体大小为50
        window = self.window
        font = pygame.font.Font(None, 150)

        # 渲染文本
        text = "Game Over"
        text_surface = font.render(text, True, WHITE)

        # 获取渲染文本的矩形对象
        text_rect = text_surface.get_rect()

        # 计算居中位置
        text_rect.center = (win_width // 2, win_height // 2)
        window.blit(text_surface, text_rect)

    def draw_score(self):
        window = self.window
        font = pygame.font.Font(None, 30)

        # 渲染文本
        text = "Score: " + str(self.score) + "     Highest: " + str(self.high_score)
        text_surface = font.render(text, True, WHITE)

        # 获取渲染文本的矩形对象
        text_rect = text_surface.get_rect()

        # 计算位置
        text_rect.left,text_rect.top = (0, 0)
        window.blit(text_surface, text_rect)

    def isOver(self):
        if self.snakes[0].alive == 0:
            return True
        return False