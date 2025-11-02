import pygame
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS[0] * TILESIZE, PLAYER_POS[1] * TILESIZE #coverts the player position from tile coordinates to pixel coordniates
        self.angle = PLAYER_ANGLE #0
        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationAngle = 0
        

    def movement(self):
        # Calculates the sine and cosine of the player's angle to move in the direction they’re facing.
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        
        speed = PLAYER_SPEED * self.game.delta_time #delta time is 1
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if key[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if key[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if key[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        self.check_walls_collisions(dx, dy)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
        
        
    def check_walls(self, x, y):
        COLLISION_SIZE = 40
        COLLISION_OFFSET = COLLISION_SIZE // 2
        
        # Create player rect in tile space, then convert to pixel space for collision
        player_rect = pygame.Rect(
            int(x - COLLISION_OFFSET), 
            int(y - COLLISION_OFFSET), 
            COLLISION_SIZE, 
            COLLISION_SIZE
        )
        
        # we have to Check collision against all walls !!!HOW THE FUCK DO WE DO THAT!!!!!!!!!!!!!!!!!!!!!!!
        for wall_rect in self.game.map.BLOCKS_1:
            if player_rect.colliderect(wall_rect):
                return False
        
        return True
    
    def check_walls_collisions(self, dx, dy):
        if self.check_walls(self.x + dx, self.y):  # safe to move left and right
            self.x += dx
        if self.check_walls(self.x, self.y + dy):  # safe to move up and down
            self.y += dy
    
    def draw(self):

        # pygame.draw.circle(self.game.screen, COLOR, (int(self.x), int(self.y)), 20)
        line_end_x = self.x + math.cos(self.angle) * 50
        line_end_y = self.y + math.sin(self.angle) * 50
        # pygame.draw.line(self.game.screen, COLOR, (self.x, self.y), (line_end_x, line_end_y), 2)

    def update(self):
        self.movement()




