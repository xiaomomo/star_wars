import pygame
import random
from src.plane import Plane
from src.bullet import Bullet
from src.enemy import Enemy
from pygame.locals import *

WIDTH = 360
HEIGHT = 480
FPS = 30

# 定义颜色常量
BLACK = (0, 0, 0)

# 1. 初始化游戏
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("设计游戏")
clock = pygame.time.Clock()

# 2.游戏里的所有角色
all_sprites = pygame.sprite.Group()
plane = Plane((WIDTH, HEIGHT))
all_sprites.add(plane)
bullet_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
for i in range(6):
    enemy = Enemy((random.randrange(0, WIDTH), random.randrange(0, 50)))
    enemy_sprites.add(enemy)
    all_sprites.add(enemy)

# 3.游戏主循环
running = True
while running:
    # 4.设置游戏帧率
    clock.tick(FPS)
    # 5. 处理用户输入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 6. 更新所有角色
    all_sprites.update()

    # 获得用户所有的键盘输入序列(如果用户通过键盘发出“向上”的指令,其他类似)
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_w] or key_pressed[K_UP]:
        plane.move_up()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        plane.move_down()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        plane.move_left()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        plane.move_right()
    if key_pressed[K_SPACE]:
        bullet = Bullet.new_bullet((plane.rect.x, plane.rect.y))
        if bullet:
            bullet_sprites.add(bullet)
            all_sprites.add(bullet)

    # 7. 渲染游戏背景
    screen.fill(BLACK)
    # 8. 渲染所有角色
    all_sprites.draw(screen)

    ## 9. 更新游戏画面
    pygame.display.flip()

pygame.quit()
