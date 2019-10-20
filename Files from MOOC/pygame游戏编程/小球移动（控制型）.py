# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame

pygame.init()
speed = [1,1]
black = 0, 0, 0
#vinfo = pygame.display.Info()
#游戏适应屏幕大小
#size = width, high =vinfo.current_w, vinfo.current_h
size = width, high = 600, 400
#固定屏幕大小
#screen = pygame.display.set_mode(size)
#屏幕大小可调
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
#无边框
#screen = pygame.display.set_mode(size, pygame.NOFRAME)
pygame.display.set_caption("Pygame壁球")
#支持13种图片格式
ball = pygame.image.load("1.jpg")
#pygame将导入图象都视作surface对象
#.get_rect方法返回一个图像的外切矩形
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]-1) * int(abs(speed[0])/speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0]+1 if speed[0]>0 else speed[0]-1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1]+1 if speed[1]>0 else speed[1]-1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1]==0 else (abs(speed[1]-1) * int(abs(speed[1])/speed[1]))
            #捕捉接收esc键并退出
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
        '''窗体调整，无法正确运行
        elif event.type == pygame.VIDEORESIZE:
            size = width, high = 500,300
            #size = width, high = event.size[0], event,size[1]
            sreen = pygame.display.set_mode(size, pygame.RESIZABLE)
            '''
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
    fclock.tick(fps)
    
    
    
    
    
    
    
    
    
    
    
    