import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        # Use an image for player sprite...
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("I can jump")
            self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # if friction - apply here
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.acc.y += self.vel.y * (PLAYER_FRIC + 0.3)
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # if self.rect.x > WIDTH:
        #     self.rect.x = 0
        # if self.rect.y > HEIGHT:
        #     self.rect.y = 0
        self.rect.midbottom = self.pos

# mobs

class Mob(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, '.png')).convert()
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        # Use an image for mob sprite...
    def update(self):
        if player.rect.x > self.rect.x:
            self.rect.x += 1
    def seeking(self):
        if player.rect.x > self.rect.x:
            self.rect.x += 1
        elif player.rect.x < self.rect.x:
            self.rect.x -=1
        elif player.rect.y > self.rect.y:
            self.rect.y +=1
        elif player.rect.y > self.rect.y:
            self.rect.y -=1    
    def update(self):
        self.seeking()
# platforms

class Platform(Sprite):
    def __init__(self, x, y, w, h, kind):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
    def update(self):
        if self.kind == "moving":
            self.pos = self.rect.x
            self.rect.x = self.pos + 2


