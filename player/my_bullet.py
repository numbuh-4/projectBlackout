import pygame
from player.player import *
from settings import *
import math
# my_bullet.py

class Bullet:
    def __init__(self, player):
        
        self.x = player.x
        self.y = player.y
        
        self.dx = math.cos(player.angle)
        self.dy = math.sin(player.angle)
        
        self.speed = 10  
        self.bullet_hitbox = pygame.Rect(self.x - 2, self.y - 2, 4, 4)
    
    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed


        self.bullet_hitbox.center = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,0), self.bullet_hitbox)
