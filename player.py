
# import pygame
# from settings import *

# # pygame.sprite.Sprite = a base class in Pygame for creating visible, movable game objects
# class Player(pygame.sprite.Sprite):
#     def __init__(self, game,x,y):
#         self.game =game
#         self._layer = PLAYER_LAYER
#         self.groups = self.game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)

#         self.x = x * TILESIZE
#         self.y = y * TILESIZE
#         self.width = TILESIZE
#         self.height = TILESIZE


#         #this is how it looks like
#         self.image = pygame.Surface([self.width, self.height])
#         self.image.fill(COLOR)

#         #where its positioned and its size
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
    

#     def update(self):
#         pass