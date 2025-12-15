import pygame
import math
from settings import *
from ray import Ray

class RayCasting:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map
        self.wall_texture = pygame.image.load("resources/textures/sprites/bricks.png")
        
    def castAllRays(self):
        self.rays = []
        rayAngle  = (self.player.angle - FOV/2) 
        for i in range (NUM_RAYS): #320
            ray = Ray(rayAngle, self.player, self.map) # every time we want to create a new ray we have to call this class again
            ray.cast()
            self.rays.append(ray)
            
            rayAngle = rayAngle + FOV  / NUM_RAYS #this makes sure we have a 3-d 
            
    def render(self, screen):
        wall_counter = 0

        texture_width = self.wall_texture.get_width() #256
        texture_height = self.wall_texture.get_height() #256
        #this draws the floor 
        pygame.draw.rect(screen, (110, 108, 97), (0, RES_HEIGHT // 2, RES_WIDTH, RES_HEIGHT // 2))


        for ray in self.rays:
            projected_line_height = (WALL_HEIGHT/ ray.distance) *  554 
            draw_begin = (RES_HEIGHT / 2) - (projected_line_height / 2) 
            height = projected_line_height
             
            # slice = pygame.Rect(wall_counter * RES, draw_begin, RES, height)
            
            texture_x = ray.offset * texture_width
            #figure out where on the wall texture image to start scalling
            #ray.offet is only a number between 0 - 1 multiplying it by texture_width gives us the exact pixel giving us the column
            wall_column = self.wall_texture.subsurface(texture_x, 0, 1, texture_height)
            # this grabs one slice of the picture of the texture 
            scaled_column = pygame.transform.scale(wall_column, (RES, int(height)))
            # then stretch that slice to the final size needed acording to our screen dimensions
            x_coord = wall_counter * RES
            y_coord = draw_begin
            screen.blit(scaled_column, (x_coord, y_coord))
            #moves the drawing position over by 3 pixels(RES) to prepare for the next ray slice
            wall_counter += 1   

    
