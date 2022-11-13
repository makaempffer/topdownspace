from settings import * 
import pygame as pg
import math
from functions import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, group):
        super().__init__(group)
        self.x, self.y = PLAYER_POS
        self.game = game 
        self.angle = PLAYER_ANGLE
        self.image = pg.image.load('resources/assets/Rocket.png').convert_alpha()
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=PLAYER_POS)
        self.vel_x = 0
        self.vel_y = 0
        


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_d]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        
        
        self.x += dx
        self.y += dy
        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.rect.x, self.rect.y), 
                (self.rect.x + WIDTH * math.cos(self.angle), 
                self.rect.y + WIDTH * math.sin(self.angle)), 2)

    def update_angle(self):
        offset_angle = 90
        self.image = rot_center(self.orig_image, math.degrees(-self.angle) - offset_angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.rect.x, self.rect.y = self.x, self.y
        self.update_angle()
        self.movement()
        #self.mouse_control()
