import pygame
from settings import *
from bullet import *
from bullet_Manager import *
class Weapon:
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy
        screen_center_x = RES_WIDTH // 2
        screen_center_y = (RES_HEIGHT // 2) + 157 
        new_width = 400
        new_height = 400
        new_size = (new_width, new_height)
        
        self.gun_images = [pygame.image.load("resources/textures/sprites/weapon/gun_0.png").convert_alpha(),
        pygame.image.load("resources/textures/sprites/weapon/gun_1.png").convert_alpha(),
        pygame.image.load("resources/textures/sprites/weapon/gun_2.png").convert_alpha()
        ]
        self.scaled_images =[]
        for img in self.gun_images:
            scaled_img = pygame.transform.scale(img, new_size)
            self.scaled_images.append(scaled_img)
        
        self.current_gun_image = 0
        self.gun_image = self.scaled_images[self.current_gun_image]
        self.rect = self.gun_image.get_rect()
        self.rect.center = (screen_center_x, screen_center_y)
        self.pistolDamage_amount = 1
        # Animation control
        self.animation = False
        self.shot_count = 0  
        self.shoot = False
    def image_update(self,):
        if self.animation == True:
            self.current_gun_image += 0.2
            
            if self.current_gun_image >= len(self.gun_images):
                self.current_gun_image = 0
                self.animation = False
            
            self.gun_image = self.gun_images[int(self.current_gun_image)]
            
    def animate(self):
        self.animation = True

    
    def damage(self,bullet_Manager,enemy):
        self.bullet_Manager = bullet_Manager
        self.enemy = enemy
        enemy_health = 10
        self.hit = False
        self.hit_sound = pygame.mixer.Sound('resources/sound_effects/hitmarker_2.mp3')

        # if self.bullet x and y coordniates collides with the hitbox of the enemy print(hit)
        
        for bullet in self.bullet_Manager.bullets:
            if bullet.bullet_hitbox.colliderect(self.enemy.hitbox):
                print("hit")
                self.hit_sound.play()

                self.hit = True
            else:
                self.hit= False

        
    
    
    
    
    
    
    def render(self, screen):
        screen.blit(self.scaled_images[int(self.current_gun_image)], self.rect)
        

