import pygame
from src.constant import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('../assets/enemy1.png')
        self.down_image_arr = (pygame.image.load('../assets/enemy1_down1.png'),
                               pygame.image.load('../assets/enemy1_down2.png'),
                               pygame.image.load('../assets/enemy1_down3.png'),
                               pygame.image.load('../assets/enemy1_down4.png'))

        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.speed = 1
        self.life = 3
        self.sys_font = pygame.font.SysFont('Comic Sans MS', 20)
        self.downIndex = 0

    def update(self):
        if self.is_survive():
            self.rect.y += self.speed
            score_surface = self.sys_font.render('life:' + str(self.life), False, RED)
            self.image.blit(score_surface, (10, 0))
        else:
            if self.downIndex > 3:
                self.kill()
            else:
                self.image.blit(self.down_image_arr[self.downIndex], self.down_image_arr[self.downIndex].get_rect())
                self.downIndex += 1

    def strike(self, bullet_group):
        collide_list = pygame.sprite.spritecollide(self, bullet_group, True)
        if len(collide_list) > 0:
            self.life -= 1

    def is_survive(self):
        return self.life > 0
