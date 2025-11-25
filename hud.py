import pygame 
from settings import *

class Health:
    def __init__(self,game):
        self.game = game
        self.health = 100
        self.font = FONT
        self.text = self.font.render(str(self.health), True, (255, 0, 0))
        
        self.damage = 10
    def damage_taken(self):
        self.health -= self.damage
        self.text = self.font.render(str(self.health), True, (255, 0, 0))

    def render(self,screen):
        # screen.blit((self.scaled_image), (15, 15))
        screen.blit(self.text, (15,15))

    



class Ammo:
    def __init__(self,game):
        self.game = game
        self.ammo = 15
        self.subtract_ammo = 1
        self.font = FONT
        self.text = self.font.render(str(self.ammo), True, (255, 0, 0))
        self.gun_image = pygame.image.load("resources/gun-2.png").convert_alpha()
       
        self.new_width = 135
        self.new_height = 81.25
        self.new_gunImg_size = (self.new_width,self.new_height)
        self.scaled_img = pygame.transform.scale(self.gun_image,  self.new_gunImg_size)

    def ammo_reducer(self):
        if self.ammo == 0:
            return
        self.ammo -= self.subtract_ammo
        self.text = self.font.render(str(self.ammo), True, (255, 0, 0))
    def reload_animation():
        pass
    def render(self,screen):
        #ammo count
        screen.blit(self.text,(1050,670))
        #gun image
        screen.blit(self.scaled_img,(1110,625))
        



        

class Round:
    def __init__(self,game):
        self.game = game
        self.round = 1
        self.font = pygame.font.SysFont("Arial", 64)
        self.text = self.font.render(str(self.round), True, (255, 0, 0))
    def render(self,screen):
        screen.blit(self.text, (50,625))
        
class Points:
    def __init__(self,game):
        self.game = game
        self.points = 0
        self.font = FONT
        self.text = self.font.render(str(self.points), True, (255, 0, 0))
    def render(self,screen):
        screen.blit(self.text,(1200,575))