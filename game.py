import pygame
from settings import *
from player.player import *
import sys
from map import *
from raycasting import *    
from db_connect import *
from player.weapon import *
from enemy.enemy import *
from hud import *
from player.bullet_Manager import *
from player.my_bullet import Bullet
from enemy.enemy_bullet import Enemybullet
from roundSystem import *

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
        self.game_over_screen_active = False
    
    def new(self):
        self.playing = True
        self.map = Map(self)
        self.ammo = Ammo(self)
        self.health = Health(self)
        self.round = Round(self)
        self.score = Score(self)
        self.enemyBM = EnemyBM()
        self.crossHair = CrossHair()
        self.player = Player(self,self.enemyBM, self.health)
        self.bullet = Bullet(self.player)
        self.bullet_Manager = BulletManager()

        
        self.roundSystem = roundSystem(self.player,self, self.enemyBM, self.round,self.ammo)

        self.weapon = Weapon(self.player, self.roundSystem,self.bullet_Manager)
        
        self.rayCasting = RayCasting(self.player, self.map)
        self.db_connection = db_connect()

    
    def draw(self):
        self.screen.fill((0, 0, 0))  
        # self.map.create_blocks() #this draws the map on the screen
        # self.player.draw()
        self.rayCasting.render(self.screen) 
        # self.map.draw()
#HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD

        self.weapon.render(self.screen)
        self.health.render(self.screen)
        self.ammo.render(self.screen)
        self.round.round_update(self.screen, self.roundSystem.round)
        self.score.score_update(self.screen, self.roundSystem.score)
#HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD HUD

        
        
        self.roundSystem.draw(self.screen)
        self.crossHair.draw_crossHair(self.screen)

        pygame.display.update()
        
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.shoot_sound.play()
                        self.weapon.animate()
                        self.ammo.ammo_reducer(self.weapon)
                        self.bullet_Manager.add_bullet(Bullet(self.player))

                    elif event.key == pygame.K_r:
                        print("The Key r was pressed!")

                


    def update(self):

        self.player.update()
        self.rayCasting.castAllRays()
        self.delta_time = self.clock.tick(FPS) 
        self.weapon.image_update()
        self.weapon.damage()
        self.health.regen_health()
        self.player.player_update_hitbox()
        self.roundSystem.updateRound()
        self.bullet_Manager.update()
        if self.health.hp <= 0:
            return "dead"
        

    def main(self):
        while self.playing:
            
            
            if self.health.hp <= 0:
                self.game_over_screen_active =True
                # print(f"You died your score was {self.roundSystem.score}")
                # print(f"You died on round {self.roundSystem.round}")
                return "dead"
            self.events()
            self.update()
            self.draw()
            
        return "quit"
    
    
    def database(self):
        self.db_connection.confirm_connection()
       

    
    def startGame(self):
        self.new()
        self.database()
        
        self.main()
        
        if self.game_over_screen_active:
            final_score = self.roundSystem.score
            round_died_on = self.roundSystem.round
            result = "dead"
            return result, final_score,round_died_on
        
        return "quit", 0, 0
            
        
        



