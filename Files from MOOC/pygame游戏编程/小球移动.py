# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:36:54 2019

@author: Forry
"""

import pygame, sys

pygame.init()
speed = [1,1]
black = 0, 0, 0
size = width, high = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame壁球")
#支持13种图片格式
ball = pygame.image.load("1.jpg")
#pygame将导入图象都视作surface对象
#.get_rect方法返回一个图像的外切矩形
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #矩形移动一个偏移量(x,y)
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left <0 or ballrect.right>width:
        speed[0] = -speed[0]
    if ballrect.top<0 or ballrect.bottom>high:
        speed[1] = -speed[1]
    #填充背景颜色
    screen.fill(black)
    #将一个图像绘制在另一个图像上
    screen.blit(ball, ballrect)
    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    