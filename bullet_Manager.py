import pygame
from bullet import Bullet


class BulletManager:
    def __init__(self):
        self.bullets =[]
        self.counter = 0
        self.track = True
    def add_bullet(self,bullet):
        if self.track == True:
            self.bullets.append(bullet)
            self.counter += 1
        print("this is bullet " + str(self.counter))
    def update(self):
        for bullet in self.bullets:
            bullet.update()
    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)
