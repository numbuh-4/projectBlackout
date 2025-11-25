import pygame
from settings import *
#we create a nested list
tile_map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]



class Map:
    #constuctor below (this runs automatically)
    def __init__(self, game):
        self.game = game
        self.map = tile_map    
        self.BLOCKS_1 = [] 
        self.create_blocks() 
        
        
        
        
        
    # this function basically checks if there is a wall at a specific (x,y) coordniate↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    # this takes in a x and a y and we divide it by tilesize
    # This converts from pixel coordinates → tile coordinates.
    def has_wall_at(self,x,y):
        return tile_map[int(y // TILESIZE)][int(x // TILESIZE)]

    def stores_wall_rect(self,col_index, row_index):
        x = col_index * TILESIZE
        y = row_index * TILESIZE      
        self.wall_rect = pygame.Rect(x,y,TILESIZE,TILESIZE) 
        self.BLOCKS_1.append(self.wall_rect)
    #loops through the tile_map and calls stores_wall_rect for every wall which is labeled as 1
    def create_blocks(self):
        for row_index, row in enumerate(self.map):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    self.stores_wall_rect(col_index, row_index)
    def draw(self):

        for row_index, row in enumerate(self.map):
            for col_index, tile in enumerate(row):
                if tile == 1:
                    wall_rect = self.stores_wall_rect(col_index, row_index)

                     #we need to store this to figure out collisons later on!!!!!!!!!!FUCK!!!!!!!
                    pygame.draw.rect(self.game.screen, BLUE, self.wall_rect, 2)  # this draws the map on the screen the way were telling it too
                    #uncomment this above to see the orginal tile map
