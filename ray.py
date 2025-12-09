import math, pygame
from settings import *

#Ensures the angle stays within 0 to 2π radians (a full circle). going the other way would mean we would have to create two cases 

def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle  = (2 * math.pi) + angle
    return angle
#this basically calculate the distance between two points (some highschool shit)
#in my case it Calculates how far a ray travels before it hits a wall.
def distance_between(x1, y1, x2, y2):
    return math.sqrt((x2 -x1) * (x2 -x1) + (y2-y1) * (y2 - y1))


class Ray:
    def __init__(self, angle, player, map):
        self.rayAngle = normalizeAngle(angle)
        self.player = player
        self.map = map
        #which way the ray is facing 
        self.is_facing_down = self.rayAngle > 0 and self.rayAngle < math.pi
        self.is_facing_up = not self.is_facing_down
        self.is_facing_right = self.rayAngle < math.pi/2  or self.rayAngle > (3* math.pi)/2
        self.is_facing_left = not self.is_facing_right
        self.hit_vertical = False   # True if the ray hit a vertical wall
        
        #These will store the exact coordinates of where the ray hits a wall.
        self.wall_hit_x = 0
        self.wall_hit_y = 0
        self.distance = 0
        
    def cast(self):
        found_horizontal_wall = False
        horizontal_hit_x = 0
        horizontal_hit_y = 0
        
        first_intersection_x = None
        first_intersection_y = None
        
        if self.is_facing_up:
            first_intersection_y = ((self.player.y // TILESIZE) * TILESIZE) - 1 # we subtract by one because the y-coordniate system increase down and we want to check the tile above
        elif self.is_facing_down:
            first_intersection_y = ((self.player.y // TILESIZE) * TILESIZE) + TILESIZE
            
        first_intersection_x = self.player.x + (first_intersection_y - self.player.y) / math.tan(self.rayAngle)
        
        nextHorizontalX = first_intersection_x
        nextHorizontalY = first_intersection_y
        
        xa = 0
        ya = 0
        
        if self.is_facing_up:
            ya = -TILESIZE
        if self.is_facing_down:
            ya = TILESIZE
            
        xa = ya / math.tan(self.rayAngle)
        
        # while it is inside the window
        while (nextHorizontalX <= RES_WIDTH and nextHorizontalX >= 0 and nextHorizontalY <= RES_HEIGHT and nextHorizontalY >= 0):
            if self.map.has_wall_at(nextHorizontalX, nextHorizontalY):
                found_horizontal_wall = True
                horizontal_hit_x = nextHorizontalX
                horizontal_hit_y = nextHorizontalY
                break
            else:
                nextHorizontalX += xa
                nextHorizontalY += ya
      
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        

        #vertical checking(starts below)
        found_vertical_wall = False
        vertical_hit_x = 0
        vertical_hit_y = 0

        if self.is_facing_right:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) + TILESIZE
        elif self.is_facing_left:
            first_intersection_x = ((self.player.x // TILESIZE) * TILESIZE) - 0.01
        
        first_intersection_y = self.player.y + (first_intersection_x - self.player.x) * math.tan(self.rayAngle)
        
        nextVerticalX = first_intersection_x
        nextVerticalY = first_intersection_y


        #Find Xa (just the width of the grid)

        if self.is_facing_right:
            xa = TILESIZE
        elif self.is_facing_left:
            xa = -TILESIZE
        
        ya = xa * math.tan(self.rayAngle)

        # this loop continues only as long as the ray's current position is inside the boundaries of the game screen    
        while (nextVerticalX <= RES_WIDTH and nextVerticalX >= 0 and nextVerticalY <= RES_HEIGHT and nextVerticalY >= 0):
            
            if self.map.has_wall_at(nextVerticalX, nextVerticalY):
                found_vertical_wall = True
                vertical_hit_x = nextVerticalX
                vertical_hit_y = nextVerticalY
                break
            else:
                nextVerticalX += xa
                nextVerticalY += ya
        
        #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        #DISTANCE CALCULATION
        horizontal_distance = 0
        vertical_distance = 0

        if found_horizontal_wall:
            horizontal_distance = distance_between(self.player.x, self.player.y, horizontal_hit_x, horizontal_hit_y)
        else:
            # the 999 is just infinity in our case so we dont have gaps(LOOK DOWN)
            # We didn’t find a wall in that direction, so pretend it’s very far away farther than any possible valid hit.
            horizontal_distance = 9999
        if found_vertical_wall:
            vertical_distance = distance_between(self.player.x, self.player.y, vertical_hit_x, vertical_hit_y)
        else:
            vertical_distance = 9999
        
        #then we have to pick which wall is closest
        if horizontal_distance < vertical_distance:
            self.wall_hit_x = horizontal_hit_x
            self.wall_hit_y = horizontal_hit_y
            self.distance = horizontal_distance
            self.hit_vertical = False   

        else:
            self.wall_hit_x = vertical_hit_x
            self.wall_hit_y = vertical_hit_y
            self.distance = vertical_distance
            self.hit_vertical = True  
        
        self.distance *= math.cos(self.player.angle - self.rayAngle)
        #this line of code just fixes the fisheye effect when getting close towards walls
        
        
        
        #this is for the texture on the walls
        if self.hit_vertical:
            self.offset = (self.wall_hit_y % TILESIZE) / TILESIZE
        else:
            self.offset = (self.wall_hit_x % TILESIZE) / TILESIZE
    