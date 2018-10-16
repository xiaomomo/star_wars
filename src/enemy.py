import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('../assets/enemy1.png')
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
