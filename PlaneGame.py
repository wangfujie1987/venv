# -*- coding: utf-8 -*-
import pygame
import random
# 导入pygame库
from sys import exit
#几个游戏的设置：
enemy_count=5# 敌机的数量
bullet_count=4#子弹的数量
bullet_interval_count=300  #子弹发出的时间间隔（单位为界面刷新的次数）
boss_interval_count=6000   #boss出现的时间间隔（单位为界面刷新的次数）

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
        self.speed = random.randint(0,2)/10 + 0.1#加0.1防止出现速度很慢的飞机
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
# 大Boss类
class Boss:
    def __init__(self):
        # self.restart()
        self.active=False
        self.image = pygame.image.load('boss.png').convert_alpha()
        self.score_boss=0#记录飞机的中弹数量
    def move(self):
        if self.active==True:
            if self.z > 1.5:
                self.x += self.speed
            else:
                self.x -= self.speed

            if self.x > 400 or self.x<0:
                self.restart()
    # 随机重置大Boss的位置和移动方向
    def restart(self):
        self.active=True
        self.x = random.randint(100, 201)
        self.y = random.randint(10, 10)
        self.speed = 0.1#random.randint(0,2)/10 + 0.1#加0.1防止出现速度很慢的飞机
        self.z = random.randint(1, 2)  # 取随机数，将飞机设置为随机左右运动
        #self.score_boss=0
    def dead(self):
        self.score_boss=0
        self.active=False
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
# 检测子弹是否碰撞到Boss
def checkHitBoss(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (
            bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        bullet.active = False# 子弹击中目标要回收
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
score_boss=0
# 创建子弹的list
bullets = []
# 向list中添加5发子弹
for i in range(bullet_count):
    bullets.append(Bullet())  # 初始化了五个实例
# 子弹总数
count_b = len(bullets)
# 即将激活的子弹序号
index_b = 0
# 发射子弹的间隔
interval_b = 0
#boss出现的时间间隔
interval_boss=boss_interval_count
# 创建敌机的list
enemys = []
for i in range(enemy_count):
    enemys.append(Enemy())
plane = Plane()
gameover = False
font = pygame.font.Font(None, 32)
#创建boss的对象
boss=Boss()
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
        interval_b -= 1
    # 当间隔小于0时，激活一发子弹（子弹的定时发出）
        if interval_b < 0:
            bullets[index_b].restart()
            # 重置间隔时间,每刷新100次界面，发射一次子弹（如果时间间隔太短，则还没等到飞到最顶端,又重新restart了，建议>100）
            interval_b = bullet_interval_count
            # 子弹序号周期性递增
            index_b = (index_b + 1) % count_b#用求余除法，获得index的自增及循环 （从0开始）
    # 判断每个子弹的状态，并且判断是否击中敌机
        for b in bullets:
            # 处于激活状态的子弹，移动位置并绘制
            if b.active:
                for e in enemys:
                    #若是击中，则增加分数
                    if checkHit(e, b):
                        score+=100
                b.move()
                screen.blit(b.image, (b.x, b.y))
    # 判断敌机是否撞到飞机
        for e in enemys:
            if checkCrash(e, plane):
                gameover = True
            e.move()
            # 把敌机画在屏幕上
            screen.blit(e.image, (e.x, e.y))
        plane.move()
        # 把飞机画到屏幕上
        screen.blit(plane.image, (plane.x, plane.y))
        interval_boss -= 1
        print('interval_boss:%d,boss.active:%s,boss.score_boss:%d'
              %(interval_boss,str(boss.active),boss.score_boss))
    #定时激活Boss
        if interval_boss<0 and boss.active==False:
            boss.restart()
            interval_boss = boss_interval_count
    # 记录boss的中弹情况
        if boss.active == True:
            boss.move()
            # 把Boss画到屏幕上
            screen.blit(boss.image, (boss.x, boss.y))
            if checkCrash(boss, plane):
                gameover = True
            # 判断Boss的中弹数量
            for b in bullets:
                if b.active:
                    if checkHitBoss(boss, b):
                        boss.score_boss += 1
                # boss被打20发子弹后死亡
            if boss.score_boss == 20:
                boss.dead()
                score += 5000
                interval_boss = boss_interval_count
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
        boss.dead()
        score = 0
        interval_boss=boss_interval_count
        gameover = False

# sssss
