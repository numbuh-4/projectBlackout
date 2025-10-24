import pygame
from settings import *
_ = False
#we create a nested list
tile_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,1,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,1,1,1,1,1,_,_,_,1,_,_,_,1],
    [1,_,_,1,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,1,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,1,_,_,_,1],
    [1,_,_,1,_,_,_,_,1,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


class Map:
    #constuctor below (this runs automatically)
    def __init__(self, game):
        self.game = game
        self.map = tile_map    
        self.BLOCKS_1 = []  

    def draw(self):
        self.BLOCKS_1 = []  

        for row_index, row in enumerate(self.map):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    wall_rect = pygame.Rect(x, y, TILESIZE, TILESIZE)

                    self.BLOCKS_1.append(wall_rect) #we need to store this to figure out collisons later on!!!!!!!!!!FUCK!!!!!!!
                    pygame.draw.rect(self.game.screen, BLUE, wall_rect, 2)  # this draws the map on the screen the way were telling it too

