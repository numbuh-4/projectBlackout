import pygame
from settings import *
from player import *
import sys
from map import *
from raycasting import *    
from db_connect import *
from weapon import *
from enemy import *
from hud import *
from bullet_Manager import *

from bullet import *

# variables from one method can be accessed and used in other methods within the same class in Python

class Game:
    #automatically called
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.shoot_sound = pygame.mixer.Sound('resources/sound_effects/pistol-shot.mp3')
        self.screen = pygame.display.set_mode((RES_WIDTH, RES_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.running = True
        self.new()
    
    
    def new(self):
        self.playing = True
        self.map = Map(self)
        self.ammo = Ammo(self)
        self.health = Health(self)
        self.round = Round(self)
        self.points = Points(self)
        self.player = Player(self)
        self.bullet_Manager = BulletManager()
        self.enemy = Enemy(self.player,self)
        self.weapon = Weapon(self.player, self.enemy)
        self.rayCasting = RayCasting(self.player, self.map)
        self.db_connection = db_connect()

        
    def draw(self):
        self.screen.fill((0, 0, 0))  
        # self.map.create_blocks() #this draws the map on the screen
        self.player.draw()
        # self.rayCasting.render(self.screen) 
        self.map.draw()
        
        self.weapon.render(self.screen)
        # self.health.render(self.screen)
        # self.ammo.render(self.screen)
        self.round.render(self.screen)
        self.points.render(self.screen)
        self.enemy.render(self.screen)
        self.bullet_Manager.draw(self.screen)

        pygame.display.update()
    def events(self):
        for event in pygame.event.get(): #get events from the queue
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # print("Spacebar pressed!")
                        # self.shoot_sound.play()
                        self.weapon.animate()
                        self.ammo.ammo_reducer()
                        self.bullet_Manager.add_bullet(Bullet(self.player))
                        self.weapon.damage(self.bullet_Manager, self.enemy)

                    elif event.key == pygame.K_r:
                        print("The Key r was pressed!")

                
                        

    def update(self):

        self.player.update()
        self.rayCasting.castAllRays()
        self.delta_time = self.clock.tick(FPS) 
        self.weapon.image_update()
        self.enemy.move_towards_player()
        self.bullet_Manager.update()

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
    def database(self):
        self.db_connection.confirm_connection()
        # self.db_connection.show_all_tables()
        self.db_connection.get_data()



g = Game()

g.intro_screen()
g.new()
g.database()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()