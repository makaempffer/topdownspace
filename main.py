import pygame as pg
from camera import *
import sys
from settings import *
from player import *
from random import randint

class Object(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pg.Surface([50, 50])
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft= pos)



class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(True)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1

        self.new_game()

    def new_game(self):
        self.camera_group = CameraGroup()
        for i in range(10):
            Object((randint(0, WIDTH), randint(0, HEIGHT)), self.camera_group)
        self.player = Player(self, self.camera_group)


    def update(self):
        self.camera_group.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}, {self.player.rect.center}')
    
    def draw(self):
        self.screen.fill('black')
        self.camera_group.custom_draw(self.player)
        #self.player.draw()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()


