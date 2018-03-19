# -*- coding: utf-8 -*-
import pygame
import random
# 导入pygame库
from sys import exit


# 子弹 类 把子弹相关的变量和函数都封装到一起
class Bullet:
    def __init__(self):
        # 初始化成员变量，x，y，image
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('bullet.jpg').convert_alpha()
        # 默认不激活
        self.active = False

    def move(self):
        # 处理子弹的运动
        # 激活的子弹才会运动
        if self.active:
            self.y -= 3
        # 飞出屏幕，则设置为不激活
        if self.y < 0:
            self.active = False

    def restart(self):
        # 重置子弹的位置
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        # 激活子弹
        self.active = True


# 敌机类
class Enemy:
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('enemy.png').convert_alpha()

    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()

    # 随机重置敌机位置和速度
    def restart(self):
        self.x = random.randint(0, 400)
        self.y = random.randint(-10, 0)
        self.speed = random.randint(1,5)/10 + 0.1#加0.1防止出现速度很慢的飞机


# 飞机类
class Plane:
    def restart(self):
        self.x = 200
        self.y = 600

    def __init__(self):
        self.restart()
        self.image = pygame.image.load('plane.jpg').convert_alpha()

    # move方法：把飞机的坐标设置为跟随鼠标移动
    def move(self):
        x, y = pygame.mouse.get_pos()
        x -= self.image.get_width() / 2
        y -= self.image.get_height() / 2
        self.x = x
        self.y = y


# 检测子弹是否碰撞到敌机
def checkHit(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (
            bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        # 命中之后出现云彩，此处有些问题，有时云彩并没有出现
        # boom = pygame.image.load('boom.jpg').convert()
        screen.blit(boom, (bullet.x, bullet.y))
        enemy.restart()
        bullet.active = False
        return True
    return False


# 检测 飞机是否碰撞到敌机-如果碰撞则Game Over
def checkCrash(enemy, plane):
    if (
            plane.x + 0.7 * plane.image.get_width() > enemy.x and plane.x + 0.3 * plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
            plane.y + 0.7 * plane.image.get_height() > enemy.y and plane.y + 0.3 * plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    return False


# 向sys模块借一个exit函数用来退出程序
pygame.init()
# 初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode((450, 800), 0, 32)
# 创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello, World!")
# 设置窗口标题
background = pygame.image.load('bg.jpg').convert()
# plane = pygame.image.load('plane.jpg').convert_alpha()
boom = pygame.image.load('boom.jpg').convert()
#score用来记录分数
score=0
# 创建子弹的list
bullets = []
# 向list中添加5发子弹
for i in range(5):
    bullets.append(Bullet())  # 初始化了五个实例
# 子弹总数
count_b = len(bullets)
# 即将激活的子弹序号
index_b = 0
# 发射子弹的间隔
interval_b = 0
# 创建敌机的list
enemys = []
for i in range(4):
    enemys.append(Enemy())
plane = Plane()
gameover = False
font = pygame.font.Font(None, 32)
while True:
    #增加判断是否gameover逻辑
    # 游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出事件后退出程序
            pygame.quit()
            exit()
    if not gameover:
        screen.blit(background, (0, 0))
        # 如果子弹超出边界,则回到原点 如果不用类，多个子弹都要用单独的变量来记录坐标位置，并进行if判断
        # if bullet_y < 1:
        #     bullet_y = y - plane.get_height() / 2
        #     bullet_x = x  # -plane.get_width()/2
        # else:
        #     bullet_y = bullet_y - 5
        # 子弹的发射时间间隔递减
        interval_b -= 1
        # 当间隔小于0时，激活一发子弹
        if interval_b < 0:
            bullets[index_b].restart()
            # 重置间隔时间,每刷新500次界面，发射一次子弹
            interval_b = 100
            # 子弹序号周期性递增
            index_b = (index_b + 1) % count_b
        # 判断每个子弹的状态
        for b in bullets:
            # 处于激活状态的子弹，移动位置并绘制
            if b.active:
                for e in enemys:
                    #若是击中，则增加分数
                    if checkHit(e, b):
                        score+=100
                b.move()
                screen.blit(b.image, (b.x, b.y))
            for e in enemys:
                # 检测是否撞到飞机
                if checkCrash(e, plane):
                    gameover = True
                e.move()
                # 把敌机画在屏幕上
                screen.blit(e.image, (e.x, e.y))
            plane.move()
            # 把飞机画到屏幕上
            screen.blit(plane.image, (plane.x, plane.y))
            #显示分数
            text = font.render("Socre: %d" % score, 1, (0, 0, 0))
            screen.blit(text, (0, 0))
    # 结束后在屏幕中间输出分数：
    else:
        text1=font.render("Game Over!Check mouse to restart", 1, (0, 0, 0))
        screen.blit(text1, (60, 200))
        text2 = font.render("Your Socre: %d" % score, 1, (0, 0, 0))
        screen.blit(text2, (120, 300))
    # 刷新一下画面（可以理解为拍一下照，记录这一帧的画面）
    pygame.display.update()
    # 重置游戏,点击鼠标重新开始
    if gameover and event.type == pygame.MOUSEBUTTONUP:
        plane.restart()
        for e in enemys:
            e.restart()
        for b in bullets:
            b.active = False
        score = 0
        gameover = False

# sssss
