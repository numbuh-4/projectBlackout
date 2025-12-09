import pygame 
from settings import *
from roundSystem import *

class Health:
    def __init__(self,game):
        self.game = game
        self.max_hp = 100
        self.hp = self.max_hp
        
        self.regen_rate = 0.1
        self.regen_delay = 180
        
        self.time_since_hit = 0
        self.damage = 5

        self.font = FONT
        self.text = self.font.render(str(int(self.hp)), True, (255, 0, 0))
        
    def damage_taken(self):
        self.hp -= self.damage
        if self.hp <0:
            self.hp = 0
            
        self.time_since_hit = 0
        
        
        self.text = self.font.render(str(int((self.hp))), True, (255, 0, 0))
    def regen_health(self):
        # Increment time since last hit
        self.time_since_hit += 1

        # Only regenerate if the player has not been hit recently
        if self.time_since_hit > self.regen_delay:
            if self.hp < self.max_hp:
                self.hp += self.regen_rate
                if self.hp > self.max_hp:
                    self.hp = self.max_hp
                    
                    
                self.text = self.font.render(str(int(self.hp)), True, (255, 0, 0))
    def update_player_hp(self):
        self.regen_health()
    def render(self,screen):
        # screen.blit((self.scaled_image), (15, 15))
        screen.blit(self.text, (15,15))

    



class Ammo:
    def __init__(self,game):
        self.game = game
        self.ammo = 100
        self.subtract_ammo = 1
        self.font = FONT
        self.text = self.font.render(str(self.ammo), True, (255, 0, 0))
        self.gun_image = pygame.image.load("resources/gun-2.png").convert_alpha()
       
        self.new_width = 135
        self.new_height = 81.25
        self.new_gunImg_size = (self.new_width,self.new_height)
        self.scaled_img = pygame.transform.scale(self.gun_image,  self.new_gunImg_size)

    def ammo_reducer(self,weapon):
        self.weapon = weapon
        if self.ammo == 0:
            self.weapon.animation = False
            return
        self.ammo -= self.subtract_ammo
        self.text = self.font.render(str(self.ammo), True, (255, 0, 0))
    def ammo_multiplier(self):
        if self.ammo == 100:
            return
        else:
            self.ammo += 100
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
        self.font = pygame.font.SysFont("Arial", 64)
   
    def round_update(self,screen,round):
        text = self.font.render(str(round), True, (255, 0, 0))

        screen.blit(text, (50,625))

class Score:
    def __init__(self,game):
        self.game = game
        self.points = 0
        self.font = FONT
        self.text = self.font.render(str(self.points), True, (255, 0, 0))
    def score_update(self,screen,score):
        score = self.font.render(str(score), True, (255, 0, 0))
        screen.blit(score, (1200,575))

class CrossHair:
    def __init__(self):
        self.center_x = RES_WIDTH / 2
        self.center_y = RES_HEIGHT / 2
        self.crossHair_color = (255,255,255)
        self.crossHair_thickness = 2
        self.line_length = 10
    def draw_crossHair(self,screen):
        start_h = (self.center_x - self.line_length, self.center_y)
        end_h = (self.center_x + self.line_length, self.center_y)
        pygame.draw.line(screen, self.crossHair_color, start_h, end_h, self.crossHair_thickness)

        start_v = (self.center_x, self.center_y - self.line_length)
        end_v = (self.center_x, self.center_y + self.line_length)
        pygame.draw.line(screen, self.crossHair_color, start_v, end_v, self.crossHair_thickness)
        