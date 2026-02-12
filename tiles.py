import random

import pygame as pg

from settings import *


def grass_tile():
    s = pg.Surface((TILE, TILE))
    s.fill((90, 180, 90))
    for _ in range(20):
        s.set_at((random.randint(0, 31), random.randint(0, 31)), (70, 160, 70))
    return s


def forest_tile():
    s = pg.Surface((TILE, TILE))
    s.fill((40, 120, 40))
    for _ in range(10):
        pg.draw.circle(s, (20, 90, 20), (random.randint(5, 27), random.randint(5, 27)), 3)
    return s


def mountain_tile():
    s = pg.Surface((TILE, TILE))
    s.fill((140, 140, 140))
    for _ in range(20):
        s.set_at((random.randint(0, 31), random.randint(0, 31)), (110, 110, 110))
    return s


def river_tile():
    s = pg.Surface((TILE, TILE))
    s.fill((60, 120, 200))
    for x in range(0, 32, 4):
        pg.draw.line(s, (80, 150, 220), (x, 0), (x, 32))
    return s


tiles = {
    1: grass_tile(),
    2: forest_tile(),
    3: mountain_tile(),
    4: river_tile()
}
