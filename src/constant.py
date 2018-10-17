#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

pygame.init()  # 游戏初始化
pygame.mixer.init()  # 混音器初始化

# 游戏背景音乐
pygame.mixer.music.load('../assets/sound/game_music.wav')
pygame.mixer.music.set_volume(0.2)

# 子弹发射音乐
bullet_sound = pygame.mixer.Sound("../assets/sound/bullet.wav")
bullet_sound.set_volume(0.2)

# 我方飞机挂了的音乐
game_over_sound = pygame.mixer.Sound("../assets/sound/game_over.wav")
game_over_sound.set_volume(0.2)

# 敌方飞机挂了的音乐
enemy1_down_sound = pygame.mixer.Sound("../assets/sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)

# 游戏相关常量
WIDTH = 360
HEIGHT = 480
FPS = 60

# 定义颜色常量
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ENEMY_SIZE = 6
ENEMY_MIN_SIZE = 2
