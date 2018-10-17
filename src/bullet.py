import pygame


class Bullet(pygame.sprite.Sprite):
    # 注意，这里定义的是类属性
    # 子弹发射间隔，毫秒单位
    shoot_delay = 250
    # 上次子弹发射时间
    last_shoot_time = 0

    # 类方法，增加子弹，这里会根据上次发射时间来决定是否能构建新子弹
    @classmethod
    def new_bullet(cls, position):
        if pygame.time.get_ticks() - cls.last_shoot_time > cls.shoot_delay:
            cls.last_shoot_time = pygame.time.get_ticks()
            return Bullet(position)

    def __init__(self, position):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('../assets/missile.png')
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        self.rect.y -= self.speed
