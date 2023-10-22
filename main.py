# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
import random
from random import randint
from settings import *
from sprites import *

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Bradley's Game")
        # very powerful; a game clock
        clock = pg.time.Clock()
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):      
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player()

        for p in PLATFORM_LIST:
            # Instantiation of the Platform 
            self.plat = Platform(*p)
            self.all_sprites.add(self.plat)
            self.all_platforms.add(self.plat)

        for m in range(0, 15):
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
        self.run()

        # add instances to groups
        self.all_sprites.add(self.player)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    # this is what prevents the player from falling through the platform when falling down...
    if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
                
    # this prevents the player from jumping up through a platform
    if self.player.vel.y < 0:
        hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
        if hits:
            print("ouch")
            SCORE -= 1
            if self.player.rect.bottom >= hits[0].rect.top - 5:
                self.player.rect.top = hits[0].rect.bottom
                self.player.acc.y = 5
                self.player.veself.l.y = 0

    def events(self):
        for event in pg.event.get():
        # check for closed window; the X at the top right
            if event.type == pg.QUIT:
                running = False

    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(screen)
        draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

        

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()
