import pygame
from enemy.enemy import *
from hud import *
class roundSystem:
    def __init__(self, player,game,enemyBM, roundHud,ammoHud):
        self.player = player
        self.game = game
        self.enemyBM = enemyBM
        self.hud = roundHud
        self.ammo = ammoHud
        self.enemies = []
        self.round = 0
        self.base_spawn = 2
        self.score = 0
    
    def startRound(self):
        self.round += 1
        amountOfEnemies = self.base_spawn * self.round
        # print(f"starting the round {self.round} with {amountOfEnemies}")
        
        self.enemies = []
        
        for _ in range(amountOfEnemies):
            enemy = Enemy(self.player, self.game, self.enemyBM)
            self.enemies.append(enemy)
            
    def updateRound(self):
        all_dead = True
        all_enemies_list = self.enemies
        for enemy in self.enemies:
            if not enemy.dead:
                enemy.update_hitbox()
                enemy.move_towards_player()
                enemy.update_enemy_bullet()
            else:
                if enemy.dead and enemy.points_given == False:
                    self.score += 15
                    enemy.points_given = True
        for i in self.enemies:
            if not i.dead:
                all_dead = False
                break
        if all_dead:
            self.startRound()
            self.ammo.ammo_multiplier()
    def draw(self,screen):
        for enemy in self.enemies:
            enemy.render(screen)
            enemy.draw_enemy_bullet(screen)
        