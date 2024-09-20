import pygame
import random
import time
from const import *

class Point(object):
    def __init__(self,property,pos,value,lifespan):
        self.property = property
        self.color = point_color[property]
        self.pos = pos
        self.value = value                  # 吃掉它的加分
        self.lifespan = lifespan            # 存在的时间
        self.exist = 1                      # 是否还在
        self.born_time = time.time()        # 出生时间

    def draw(self,window):
        pos = self.pos
        pygame.draw.rect(window,self.color,(pos[0],pos[1],SNAKE_SIZE,SNAKE_SIZE),SNAKE_SIZE//2)

    def update(self):
        if self.exist and time.time()-self.born_time > self.lifespan:
            self.exist = 0