# -*- coding: utf-8 -*-
import pygame
# 导入pygame库
from sys import exit
#子弹 类
class Bullet:
    def __init__(self):
        #初始化成员变量，x，y，image
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('bullet.jpg').convert_alpha()

    def move(self):
        #处理子弹的运动
        if self.y < 0:
            mouseX, mouseY = pygame.mouse.get_pos()
            self.x = mouseX #- self.image.get_width() / 2
            self.y = mouseY #- self.image.get_height() / 2
            print('test')
        else:
            self.y -= 5

# 向sys模块借一个exit函数用来退出程序
pygame.init()
# 初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((450, 800), 0, 32)
# 创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello, World!")
# 设置窗口标题
background = pygame.image.load('bg.jpg').convert()
plane = pygame.image.load('plane.jpg').convert_alpha()
#bullet = pygame.image.load('bullet.jpg').convert_alpha()
bullet=Bullet()
while True:
    # 游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出事件后退出程序
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    # 如果子弹超出边界,则回到原点
    # if bullet_y < 1:
    #     bullet_y = y - plane.get_height() / 2
    #     bullet_x = x  # -plane.get_width()/2
    # else:
    #     bullet_y = bullet_y - 5
    bullet.move()
    # 把子弹画到屏幕上 初始位置为飞机后面
    screen.blit(bullet.image, (bullet.x, bullet.y))
    # 计算飞机的左上角位置
    x, y = pygame.mouse.get_pos()
    x -= plane.get_width() / 2
    y -= plane.get_height() / 2
    # 把飞机画到屏幕上
    screen.blit(plane, (x, y))
    # 刷新一下画面
    pygame.display.update()
#sssss