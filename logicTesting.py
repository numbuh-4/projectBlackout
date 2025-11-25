import math
from settings import *
import random


fov = 60  * (math.pi /180)
from map import tile_map
print(fov)

rayAngle = (0 - fov/2)

testMath2 = (RES_WIDTH /2)
testMath = math.tan(FOV/2)
project_plane_distance = testMath2 / testMath
print(project_plane_distance)

tile_y = random.randint(0, len(tile_map) - 1)
tile_x = random.randint(0, len(tile_map[0]) - 1)
print(random.randint(0,len(tile_map)-1))
print(len(tile_map[0]))
if tile_map[tile_y][tile_x] == 0:
    x = tile_x * TILESIZE
    y = tile_y * TILESIZE




