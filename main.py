import pygame
from settings import *
from player import *
import sys
from map import *
# variables from one method can be accessed and used in other methods within the same class in Python

class Game:
    #automatically called
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))
        #This sets our frame rate so how many times the screen refereshs per second
        self.clock = pygame.time.Clock()
        self.running = True
        self.new()
    
    def new(self):
        self.playing = True

       
        self.map = Map(self) #giving the Map class access to everything inside the Game class.
        
    def draw(self):
       
        self.clock.tick(FPS)
        pygame.display.update()
        self.map.draw()

    def events(self):
        for event in pygame.event.get(): #get events from the queue
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #makes sure its not a static image (#game look updates)
        pass
    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    def game_over(self):
        pass
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()