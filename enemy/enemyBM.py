import pygame
from enemy.enemy_bullet import *

class EnemyBM:
    def __init__(self):
        self.bullets = []
        
    def add_bullet(self,bullet):
        self.bullets.append(bullet)
    def update(self):
        for bullet in self.bullets:
            bullet.update()
    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        