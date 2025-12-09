import math
import pygame
RES_WIDTH = 1280 #1600
RES_HEIGHT = 720 #900
pygame.init()
FONT = pygame.font.SysFont("Arial", 34)
FPS = 60
TILESIZE = 80
PLAYER_LAYER = 1
COLOR = (255,0,0)
SCREEN_COLOR = (0,0,0)
BLOCK_LAYER = 1
BLUE = (0,0 ,255)

PLAYER_POS = 1.2, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.25
PLAYER_ROT_SPEED = 0.002

FOV = 60  * (math.pi /180) #answer is 1 but in radians its in 60

RES = 3 #the width of each rectangle getting drawn on to the screen
NUM_RAYS = RES_WIDTH // RES #426

#3D Projection
WALL_HEIGHT = 80 #same as tile tilesize btw
WALL_COLOR = 255
TEXTURE_SIZE = 64
DISTANCE_FROM_PLAYER_TO_PROJECTED_SCREEN = 1108 #half of RES_WIDTH / tan(FOV/2)

DATABASE_PASSWORD = 'Waterbottle321$'
DATABASE_USER = 'root'