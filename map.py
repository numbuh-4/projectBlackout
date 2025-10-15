import pygame
from settings import *
_ = False
#we create a nested list
map = [
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
        self.map = map
        self.walls = {} #creating an empty dictionary.
        self.get_map()

   
    def get_map(self):
       
        pass
    def draw(self):
        pass

        

       

    