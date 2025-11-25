import pygame
import math
import random
from settings import *
from map import tile_map
from map import Map


def random_enemy_spawn():
    while True:
        tile_y = random.randint(0, len(tile_map) - 1)
        tile_x = random.randint(0, len(tile_map[0]) - 1)

        if tile_map[tile_y][tile_x] == 0:
            x = tile_x * TILESIZE
            y = tile_y * TILESIZE
            return x, y
class Enemy:
    def __init__(self, player,game):
        self.player = player
        self.game = game
        self.distance = 0
        self.angle = 0
        self.visible = False
        self.map = Map(self.game)
        self.image = pygame.image.load("resources/textures/sprites/soldier/soldier-removebg-preview.png").convert_alpha()
        self.enemy_x_position, self.enemy_y_position = random_enemy_spawn()
        self.elimnated = False
        
    def project(self):

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

        self.visible = True
        self.projected_width = enemy_width
        self.projected_height = enemy_height
        self.screen_x = screen_x 
        self.screen_y = screen_y +10
        
        
        self.hitbox = pygame.Rect(int(self.screen_x),int(self.screen_y ),int(self.projected_width ),int(self.projected_height))

#/////////////////////////////////////////////////////////////////////////////////////////////////////////        
    def line_of_sight(self):
        enemy_pos = (self.enemy_x_position, self.enemy_y_position)
        player_pos = (self.player.x, self.player.y)
        for wall in self.map.BLOCKS_1:
            if wall.clipline(enemy_pos,player_pos):
                self.visible = False
                return
            
    def move_towards_player(self):
        dx = self.player.x - self.enemy_x_position
        dy = self.player.y - self.enemy_y_position

        distance = math.sqrt(dx**2 + dy**2)

       
        if distance <= 200: 
            return
        # we have to divide it by distance to basically make it close to 1 (normalizing the vector)
        direction_x = dx / distance
        direction_y = dy / distance
        speed = 3
        
        new_x = self.enemy_x_position + direction_x * speed
        new_y = self.enemy_y_position + direction_y * speed
        
        
        
        if self.map.has_wall_at(new_x, self.enemy_y_position) == 0:
            self.enemy_x_position = new_x

        if self.map.has_wall_at(self.enemy_x_position, new_y) == 0:
             self.enemy_y_position = new_y
             
#/////////////////////////////////////////////////////////////////////////////////////////////////////////           
             
    def deal_damage(self):
        pass        
             
             
             
             
             
             
    def draw(self, screen):
        # if self.visible == False:
        #     return

        # scaled_sprite = pygame.transform.scale(self.image, (int(self.projected_width), int(self.projected_height)))

        # screen.blit(scaled_sprite, (self.screen_x, self.screen_y))
        pygame.draw.circle(screen,COLOR, (self.enemy_x_position,self.enemy_y_position),20)
    def render(self, screen):
        self.project()         
        self.line_of_sight()
        self.draw(screen)

    
