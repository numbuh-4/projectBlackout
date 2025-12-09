import pygame
from player.player import *
from settings import *
import math

class Enemybullet:
    def __init__(self,enemy):
        self.enemy = enemy
        self.x = self.enemy.enemy_x_position
        self.y = self.enemy.enemy_y_position

        self.dx = 0
        self.dy = 0
        
        self.speed = 1
        self.bullet_hitbox = pygame.Rect(self.x - 2, self.y - 2, 4, 4)
    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed


        self.bullet_hitbox.center = (self.x, self.y)
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,0), self.bullet_hitbox)
