import pygame
import random


class Colors(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.emoji = ['trollemoji.png','happyemoji.jpg','sademoji.png', \
                      'cryingemoji.png','laughingemoji.png','smirkemoji.png', \
                      'kissemoji.png', 'scaredemoji.png','loveemoji.png']

        self.image = pygame.image.load('neutralemoji.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(topleft=(self.x,self.y))

    def flash(self):
        self.image = pygame.image.load(random.choice(self.emoji))
        self.image = pygame.transform.scale(self.image, (100,100))

    def revert(self):
        self.image = pygame.image.load('neutralemoji.png')
        self.image = pygame.transform.scale(self.image, (100,100))

    def wrong(self):
        self.image = pygame.image.load('devilemoji.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        
    def right(self):
        self.image = pygame.image.load('angelemoji.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        
