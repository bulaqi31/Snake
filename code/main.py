import pygame
import sys
import random
from const import *
from pygame.locals import *
from snake import *
import time
from game import *
from choose import *
from double_mode import *

#clock = pygame.time.Clock()
pygame.init()

window = pygame.display.set_mode(GAME_SIZE)
high_score = 0
choosing = Choose(window)

while True:
    # 先进入选择界面
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查点击是否在单人模式文本上
                choosing.process(event.pos)

        choosing.update()
        choosing.draw()
    
        if choosing.start == 1: # 点下去了，开始游戏
            break
        pygame.display.flip()
         
    # 正式进入游戏
    if choosing.mode == "SURVIVAL":
        game1 = Survival_Hand(window,high_score)
    elif choosing.mode == "BATTLE":
        game1 = Battle_PVP(window)
    while True:
        #print(snake1.list)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game1.process(event.key)
                #print(pygame.key.name(event.key))

        game1.update()
        game1.draw()
        # 更新整个窗口表面以显示我们的绘制
        if game1.isOver():
            game1.Gameover()
            pygame.display.flip()
            time.sleep(3)
            if choosing.mode == "SURVIVAL":
                high_score = game1.high_score
            game1 = None
            break
        pygame.display.flip()
        #clock.tick(10)
        #pygame.display.update()
