import pygame
import time
from const import *


class Snake(object):
    def __init__(self,property,pos,length,direction="RIGHT"):
        self.property = property
        self.color = snake_color[property]  # 这条蛇是什么颜色       
        self.pos = pos              # 位置
        self.length = length
        self.list = []
        for i in range(length):
            pos_x = pos[0] - i*10
            self.list.append((pos_x,pos[1]))
        
        self.turn_pos = pos         # 上一次转弯时的位置
        self.direction = direction  # 运动方向
        self.alive = 1              # 生存情况
        self.full = 0               # 上一秒有没有吃东西
        self.buffer = []            # 按键的缓冲区

    def draw(self,window):       
        #if self.alive:
        length = self.length
        for i in range(length):
            item = self.list[i]
            #print(i)
            color_R,color_G,color_B = self.color                      # 给蛇添加渐变色
            if self.property:
                if color_R:
                    delta = i*2
                    color_G = min(color_G+delta,200)
                    color_B = min(color_B+delta,200)
                elif color_G:
                    delta = i*2
                    color_R = min(color_R+delta,200)
                    color_B = min(color_B+delta,200)
            color = (color_R,color_G,color_B)
            pygame.draw.rect(window,color,(item[0],item[1],SNAKE_SIZE,SNAKE_SIZE),SNAKE_SIZE//2)
        
            

    def update(self):
        #print(self.list)
        pos_now = self.pos
        dir = MOV_DIR[self.direction]                   
        new_x = pos_now[0] + SNAKE_SIZE * dir[0]
        new_y = pos_now[1] + SNAKE_SIZE * dir[1]       
        pos_next = (new_x,new_y)                        # 新蛇头
        self.pos = pos_next                             # 赋值更改
        #print(pos_next)
        if self.full:                  # 上一秒吃东西了，要变长
            new_list = self.list       # 最尾巴就不删掉了
            self.length += 1           # 长度变长一个
            self.full -= 1              # 现在肚子又饿了
        else:
            new_list = self.list[:-1]
        new_list.insert(0,pos_next)    # 新蛇
        self.list = new_list           # 赋值更改

        if self.isDead():
            self.alive = 0
        if self.buffer:
            self.TURN(self.buffer.pop(0))

    def TURN(self,evt):
        #print("******")
        #print("now_dirction: " + self.direction + "  ***  event: " + evt)
        
        if (evt == "a" or evt == "left") and self.direction != "RIGHT":
            #print("a or left")
            if self.pos != self.turn_pos:             # 时间满足就转弯
                self.direction = "LEFT"
                self.turn_pos = self.pos
            else:
                self.buffer.append(evt)
        elif (evt == "w" or evt == "up") and self.direction != "DOWN":
            #print("w or up")
            if self.pos != self.turn_pos:
                self.direction = "UP"
                self.turn_pos = self.pos
            else:
                self.buffer.append(evt)
        elif (evt == "s" or evt == "down") and self.direction != "UP":
            #print("s or down")
            if self.pos != self.turn_pos:
                self.direction = "DOWN"
                self.turn_pos = self.pos
            else:
                self.buffer.append(evt)
        elif (evt == "d" or evt == "right") and self.direction != "LEFT":
            #print("d or right")
            if self.pos != self.turn_pos:
                self.direction = "RIGHT"
                self.turn_pos = self.pos
            else:
                self.buffer.append(evt)
        
        #print("next_dirction: " + self.direction)

    def HALF(self):                                         # 蛇切掉自己的一半
        #print("***in HALF***")
        self.length = (self.length+1)//2
        self.list = self.list[:self.length]

    def isDead(self):           #死亡判定
        if self.isOut():
            return True
        if self.isSuicide():
            return True
        return False

    def isSuicide(self):
        body = self.list[2:]    # 除了头
        if self.pos in body:    # 头撞身体
            return True
        return False

    def isOut(self):    # 越界判定
        x = self.pos[0]
        y = self.pos[1]
        if x<EDGE_LEFT or x>EDGE_RIGHT or y<EDGE_TOP or y>EDGE_BUTTOM:
            return True
        return False