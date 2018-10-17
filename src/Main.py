import pygame
import random
from src.plane import Plane
from src.bullet import Bullet
from src.enemy import Enemy
from pygame.locals import *

WIDTH = 360
HEIGHT = 480
FPS = 60

# 定义颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ENEMY_SIZE = 6
ENEMY_MIN_SIZE = 2

# 1. 初始化游戏
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("射击游戏")
clock = pygame.time.Clock()

# 2.游戏里的所有角色
all_sprites = pygame.sprite.Group()
plane = Plane((WIDTH, HEIGHT))
all_sprites.add(plane)
bullet_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()


def init_enemy(size):
    for i in range(size):
        enemy = Enemy((random.randrange(0, WIDTH), random.randrange(0, 50)))
        enemy_sprites.add(enemy)
        all_sprites.add(enemy)


# 初始化敌舰
init_enemy(ENEMY_SIZE)

# 3.游戏主循环
running = True
score = 0
life = 3
pygame.font.init()


def show_text(word, color, position, font_size):
    sys_font = pygame.font.SysFont('Comic Sans MS', font_size)
    score_surface = sys_font.render(word, False, color)
    screen.blit(score_surface, position)


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

    # 子弹击毁敌舰
    bullet_collide_dic = pygame.sprite.groupcollide(bullet_sprites, enemy_sprites, True, True)
    for bullet in bullet_collide_dic:
        score += 1
        print(bullet, bullet_collide_dic[bullet], score)

    # 增加敌舰
    if len(enemy_sprites) <= ENEMY_MIN_SIZE:
        init_enemy(ENEMY_SIZE - len(enemy_sprites))

    # 敌舰撞击飞机
    collide_planes = pygame.sprite.spritecollide(plane, enemy_sprites, True)
    if len(collide_planes) > 0:
        life -= 1
        print('life', life)
        if life <= 0:
            running = False

    # 7. 渲染游戏背景
    screen.fill(BLACK)
    show_text('score:' + str(score), WHITE, (WIDTH - 100, 0), 30)
    show_text('life:' + str(life), RED, (WIDTH - 100, 20), 30)

    # 8. 渲染所有角色
    all_sprites.draw(screen)

    ## 9. 更新游戏画面
    pygame.display.flip()

pygame.quit()
