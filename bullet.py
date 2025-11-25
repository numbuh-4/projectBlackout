import pygame
from player import *
from settings import *
import math
class Bullet:
    def __init__(self, player):
        self.imageBullet = pygame.image.load("resources/light_bullet.png").convert_alpha()
        self.x = player.x
        self.y = player.y
        
        self.dx = math.cos(player.angle)
        self.dy = math.sin(player.angle)
        
        self.speed = 10  
        self.bullet_hitbox = self.imageBullet.get_rect(center=(self.x,self.y))
        
    
    def update(self):
        self.x = self.x + (self.dx * self.speed)
        self.y = self.y + (self.dy * self.speed)

        self.bullet_hitbox.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.imageBullet, self.bullet_hitbox)
