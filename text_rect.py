import pygame
from const import *

class Text_Rect(object):
    def __init__(self,txt,font,step,nxt,color=WHITE,left=None,top=None,center=None,click=0):
        self.color = color                              # 字体颜色
        self.txt = txt                                  # 文本内容
        self.font = pygame.font.Font(None,font)         # 字号
        self.step = step                                # 它在进行什么选择
        self.nxt = nxt                                # 接下来要进行什么选择

        self.left = left            
        self.top = top
        self.center = center                            # 位置
        self.click = click                              # 是否被点击
        font = self.font
        text = self.txt
        self.surface = font.render(text, True, self.color)
        self.rect = self.surface.get_rect()             # 把这个矩形对象也放进来

    
    def draw(self,window):
        
        rect = self.rect
        # 计算居中位置
        if self.center:
            rect.center = self.center
        elif self.left and self.top:
            rect.left = self.left
            rect.top = self.top
        else:
            print("No Position!!!")
        window.blit(self.surface, rect)

    def checkClick(self,pos):
        if self.rect.collidepoint(pos):
            self.click = 1