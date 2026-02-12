import pygame as pg

from building import Building, BuildingType
from map import Map
from settings import *


class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Mini RTS")
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, 24)
        self.running = True
        self.timer = 0
        self.selected_building = BuildingType.FARM
        self.gold = 200
        self.food = 200

        self.map = Map(self)
        self.game_objects = []

    def process_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1: self.selected_building = BuildingType.FARM
                if event.key == pg.K_2: self.selected_building = BuildingType.MINE
                if event.key == pg.K_3: self.selected_building = BuildingType.BARRACK
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pg.mouse.get_pos()
                tx, ty = mx // TILE, my // TILE

                if 0 <= tx <= MAP_W and 0 <= ty <= MAP_H:
                    self.game_objects.append(Building(self, (tx, ty), self.selected_building))

    def update(self):
        self.timer += self.clock.tick(FPS)

        if self.timer >= MILLISECONDS_PER_SEC:
            self.timer = 0


        pg.display.flip()

    def draw(self):
        self.screen.fill(BG_COLOR)

        self.map.draw()

        if len(self.game_objects) > 0:
            for obj in self.game_objects:
                obj.draw()

        self.screen.blit(self.font.render(f"Gold: {self.gold}", True, (255, 255, 0)), (10, 10))
        self.screen.blit(self.font.render(f"Food: {self.food}", True, (0, 255, 0)), (10, 30))

        self.screen.blit(self.font.render("1-Farm 2-Mine 3-Barrack | Q-Spearman W-Archer | ESC-Deselect",
                                True, (255, 255, 255)), (10, HEIGHT - 30))
        self.screen.blit(self.font.render("E - Spawn enemy (test) | LMB - Select/Build | RMB - Move/Attack",
                                True, (200, 200, 200)), (10, HEIGHT - 60))

    def run(self):
        while self.running:
            self.process_event()
            self.update()
            self.draw()

        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
