import pygame
from settings import *
from player.my_bullet import *
from player.bullet_Manager import *
class Weapon:
    def __init__(self,player,roundSystem, bullet_Manager):
        self.player = player
        self.roundSystem = roundSystem
        self.bullet_Manager = bullet_Manager
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

    
    def damage(self):
        
        self.hit_sound = pygame.mixer.Sound('resources/sound_effects/hitmarker_2.mp3')
        
        for enemy in self.roundSystem.enemies:
            if enemy.dead:
                continue
            for bullet in self.bullet_Manager.bullets:
                if bullet.bullet_hitbox.colliderect(enemy.world_hitbox):
                    self.hit_sound.play()
                    print("hit")
                    enemy.color = (0,255,0) 
                    enemy.enemy_health()
                    self.bullet_Manager.bullets.remove(bullet)
                    
                    break

    def render(self, screen):
        screen.blit(self.scaled_images[int(self.current_gun_image)], self.rect)
        

