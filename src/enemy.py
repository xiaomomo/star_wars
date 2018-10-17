import pygame
from src.constant import *


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('../assets/enemy1.png')

        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.speed = 1
        self.life = 3
        self.sys_font = pygame.font.SysFont('Comic Sans MS', 20)

    def update(self):
        self.rect.y += self.speed
        score_surface = self.sys_font.render('life:' + str(self.life), False, RED)
        self.image.blit(score_surface, (10, 0))

    def strike(self, bullet_group):
        collide_list = pygame.sprite.spritecollide(self, bullet_group, True)
        if len(collide_list) > 0:
            self.life -= 1
            if self.life <= 0:
                self.kill()

    def is_survive(self):
        return self.life > 0
