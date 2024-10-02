import pygame
import random
from const import *
from text_rect import *

class Choose(object):
    def __init__(self,window):
        self.window = window                                # 在哪个窗口
        self.start = 0                                      # 能否开始游戏
        self.step = "survival or battle"                      # 进行什么选择
        self.mode = None                                    # 现在是什么模式，应该怎么操作
        self.text_rects = []                                # 有哪些文本框
        start_rect = Text_Rect("START",200,"start","done",center=(win_width//2,win_height//2))
        sv_hand_rect = Text_Rect("SOLO",150,"solo or pair","start",center=(win_width//2-200,win_height//2))
        sv_hands_rect = Text_Rect("PAIR",150,"solo or pair","start",center=(win_width//2+200,win_height//2))
        survival_rect = Text_Rect("SURVIVAL",100,"survival or battle","solo or pair",center=(win_width//2-200,win_height//2))
        battle_rect = Text_Rect("BATTLE",100,"survival or battle","start",center=(win_width//2+200,win_height//2))
        self.text_rects.append(start_rect)
        self.text_rects.append(sv_hand_rect)
        self.text_rects.append(sv_hands_rect)
        self.text_rects.append(survival_rect)
        self.text_rects.append(battle_rect)

    def draw(self):
        self.drawback()
        window = self.window
        for rect in self.text_rects:
            if self.step == rect.step:          #只画对应步骤的文本框
                rect.draw(window)


    def drawback(self):           # 把游戏背景画出来
        
        boundry_color = BLUE
        boundry_width = 20
        pygame.display.set_caption('Snake')
        window = self.window
        window.fill(GRAY)
        # 参数分别为：窗口对象，左上角坐标，宽度，高度，边框颜色，边框线宽
        pygame.draw.rect(window, boundry_color, (0, 0, win_width, win_height), boundry_width)


    def update(self):
        self.checkMode()

    def checkMode(self):
        step_now = self.step
        for rect in self.text_rects:
            if rect.step == step_now and rect.click:
                if rect.txt == "START":
                    self.start = 1
                else:
                    self.mode = rect.txt
                self.step = rect.nxt

    def process(self,pos):
        for rect in self.text_rects:
            if rect.step == self.step:
                rect.checkClick(pos)