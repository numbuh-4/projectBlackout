import pygame
from settings import *
from player import *
import sys
from map import *
from raycasting import *
# variables from one method can be accessed and used in other methods within the same class in Python

class Game:
    #automatically called
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.running = True
        self.new()

    
    def new(self):
        self.playing = True
        self.map = Map(self)
        self.player = Player(self)
        self.rayCasting = RayCasting(self, self.player)
    def draw(self):
        self.screen.fill((0, 0, 0))  
        self.map.draw() #this draws the map on the screen
        self.player.draw()
        pygame.display.update()
    def events(self):
        for event in pygame.event.get(): #get events from the queue
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.player.update()
        self.rayCasting.update()
        self.delta_time = self.clock.tick(FPS)
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