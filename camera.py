import pygame as pg
from settings import *
class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.offset = pg.math.Vector2()

    def camera_follow_target(self, target):
        self.offset.x = target.rect.centerx - HALF_WIDTH
        self.offset.y = target.rect.centery - HALF_HEIGHT
    
    def custom_draw(self, player):
        self.camera_follow_target(player)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)