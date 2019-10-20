# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 21:04:38 2019
 pygame 外控响应测试
@author: Forry
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame游戏之旅")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #键盘对象测试
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("KEYDOWN:NONE", event.key, event.mod )
            else:
                print("KEYDOWN:", event.unicode, event.key, event.mod)
        #鼠标对象测试
        elif event.type == pygame.MOUSEMOTION:
            print("MOUSEMOTION:", event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("MOUSEBUTTONUP:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("MOUSEBUTTONDOWN:",event.pos,event.button)
    pygame.display.update()

