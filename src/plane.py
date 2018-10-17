import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super(Plane, self).__init__()
        self.image = pygame.image.load('../assets/plant1.png')
        self.rect = self.image.get_rect()
        self.speed = 5
        self.bg_size = bg_size
        # 飞机位于舞台底部
        self.rect.x = self.bg_size[0] / 2
        self.rect.y = self.bg_size[1] - self.rect.height
        self.life = 3

    def update(self, *args):
        pass

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.rect.y = 0

    def move_down(self):
        # 注意这里还有一个飞机本身的高度
        if self.rect.y < self.bg_size[1] - 60:
            self.rect.y += self.speed
        else:
            self.rect.y = self.bg_size[1] - 60

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
        else:
            self.rect.x = 0

    def move_right(self):
        # 注意这里还有一个飞机本身的宽度
        if self.rect.x < self.bg_size[0] - 60:
            self.rect.x += self.speed
        else:
            self.rect.x = self.bg_size[0] - 60

    # 撞击
    def strike(self, enemy_group):
        collide_planes = pygame.sprite.spritecollide(self, enemy_group, True)
        if len(collide_planes) > 0:
            self.life -= 1
            print('life', self.life)

    # 是否存活
    def is_survive(self):
        return self.life > 0
