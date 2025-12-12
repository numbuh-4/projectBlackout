import pygame
import math
import random
from settings import *
from map import tile_map
from map import Map
from enemy.enemyBM import EnemyBM
from enemy.enemy_bullet import Enemybullet

def random_enemy_spawn():
    while True:
        tile_y = random.randint(0, len(tile_map) - 1)
        tile_x = random.randint(0, len(tile_map[0]) - 1)

        if tile_map[tile_y][tile_x] == 0:
            x = tile_x * TILESIZE
            y = tile_y * TILESIZE
            return x, y
class Enemy:
    def __init__(self, player,game,enemyBM):
        self.player = player
        self.game = game
        self.distance = 0
        self.angle = 0
        self.visible = False
        self.dead = False
        self.map = Map(self.game)
        self.image = pygame.image.load("resources/textures/sprites/soldier/soldier-removebg-preview.png").convert_alpha()
        self.enemy_x_position, self.enemy_y_position = random_enemy_spawn()
        self.color = (255,0,0)
        self.hp = 50
        self.shoot_cooldown = 0
        self.enemybulletManager = enemyBM
        
        self.hitbox_size = 40
        self.world_hitbox = pygame.Rect(self.enemy_x_position,self.enemy_y_position,self.hitbox_size,self.hitbox_size,)
        self.world_hitbox.x = 0
        self.world_hitbox.y = 0
        self.points_given = False

    def project(self):
        if self.dead == True:
            return
        #this shit is in vectors, we have to break this into components so we can find the distance(hypotnuse)↓↓↓↓↓↓↓
        dx = self.enemy_x_position - self.player.x
        dy = self.enemy_y_position - self.player.y
        
        # distance from player↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        self.distance = math.sqrt(dx * dx + dy * dy)
        
        #the enemy angle tells you which direction to face to look at the enemy(its literally turning a line into an angle)
        enemy_angle = math.atan2(dy, dx)
        
        #how much the player must turn to face the enemy
        #positive mean the enemy is to the right
        #negative mean the enemy is to the left
        relative_angle = enemy_angle - self.player.angle
        
        #part 6(stays between -pi and pi)
        relative_angle = (relative_angle + math.pi) % (2 * math.pi) - math.pi
        
        # if outside FOV, don't draw
        if abs(relative_angle) > FOV / 2:
            self.visible = False
            return

        how_far_is_it_from_the_screen = (RES_WIDTH / 2) / math.tan(FOV / 2)

        #how tall the enemy should appear on the screen based on how far away it is.
        enemy_height = (TILESIZE / self.distance) * how_far_is_it_from_the_screen 
        enemy_width = enemy_height
        #This line figures out where (left or right) the enemy should appear on the screen based on its angle from the player.
        screen_x = (RES_WIDTH / 2) + math.tan(relative_angle) * how_far_is_it_from_the_screen - enemy_width / 2
        #This line puts the enemy vertically centered on the screen based on how tall the value is
        floor_offset = 20
        screen_y = (RES_HEIGHT / 2) - enemy_height / 2 + floor_offset
        
        #SAVE THE CALUCLATED RESULTS KEVIN!!! so i Can use them later
        self.visible = True
        self.projected_width = enemy_width
        self.projected_height = enemy_height
        self.screen_x = screen_x 
        self.screen_y = screen_y +10
        
        
        
    def update_hitbox(self):
        if self.dead == True:
            return
        self.world_hitbox.x = self.enemy_x_position - self.hitbox_size//2
        self.world_hitbox.y = self.enemy_y_position - self.hitbox_size//2
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////        
    def line_of_sight(self):
        enemy_pos = (self.enemy_x_position, self.enemy_y_position)
        player_pos = (self.player.x, self.player.y)
        for wall in self.map.BLOCKS_1:
            if wall.clipline(enemy_pos,player_pos):
                self.visible = False
                return
            
    def move_towards_player(self):
        if self.dead == True:
            return
        
        dx = self.player.x - self.enemy_x_position
        dy = self.player.y - self.enemy_y_position

        distance = math.sqrt(dx**2 + dy**2)

       
        if self.distance <= 200: 
            self.deal_damage()
            self.player.player_hp()
            return
        # we have to divide it by distance to basically make it close to 1 (normalizing the vector)
        direction_x = dx / distance
        direction_y = dy / distance
        
        self.angle = math.atan2(direction_y, direction_x) 

        
        speed = 3
        
        new_x = self.enemy_x_position + direction_x * speed 
        new_y = self.enemy_y_position + direction_y * speed 
        
        
        
        if self.map.has_wall_at(new_x, self.enemy_y_position) == 0:
            self.enemy_x_position = new_x

        if self.map.has_wall_at(self.enemy_x_position, new_y) == 0:
             self.enemy_y_position = new_y
      
#/////////////////////////////////////////////////////////////////////////////////////////////////////////           
    def enemy_health(self):
        if self.dead == True:
            return
        self.hp -=10

        # if self.hp != 0:
        #     self.hp -=10
        #     # print("the enemy hp is now"+ str(self.hp))
        # else:
        #     print("he is dead")
        #     self.dead = True
        if self.hp <= 0:
            self.dead = True
            print("he is dead")


                   
    def deal_damage(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            return
        
        dx = self.player.x - self.enemy_x_position
        dy = self.player.y - self.enemy_y_position
        distance = math.sqrt(dx**2 + dy**2)

        direction_x = dx / distance
        direction_y = dy / distance
        
        angle = math.atan2(direction_y, direction_x) 
        
        
        #then i have to create a bullet
        self.create_bullet(angle)
        self.shoot_cooldown = 40
        
        
    def create_bullet(self,angle):
        bullet = Enemybullet(self)
        bullet.dx = math.cos(angle)
        bullet.dy = math.sin(angle)
        
        self.enemybulletManager.add_bullet(bullet)
    def update_enemy_bullet(self):
        self.enemybulletManager.update()
    def draw_enemy_bullet(self,screen):
        self.enemybulletManager.draw(screen)
    
    def animation_shooting(self):
        pass         
    def draw(self, screen):
        # if self.visible == False:
        #     return

        # scaled_sprite = pygame.transform.scale(self.image, (int(self.projected_width), int(self.projected_height)))

        # screen.blit(scaled_sprite, (self.screen_x, self.screen_y))
        
        #//////////////////////////////////////////////////////////////
        rect_size = 40
        
        self.enemy_rect = pygame.Rect(self.enemy_x_position- rect_size // 2, self.enemy_y_position- rect_size //2, rect_size,rect_size)
        pygame.draw.rect(screen,self.color, self.enemy_rect)
        self.direction = (self.enemy_x_position + math.cos(self.angle)*50, self.enemy_y_position + math.sin(self.angle) *50)

        pygame.draw.line(self.game.screen, self.color, (self.enemy_x_position, self.enemy_y_position), self.direction, 2)

    def render(self, screen):
        if self.dead == True:
            return
        self.project()         
        self.line_of_sight()
        self.draw(screen)

    
