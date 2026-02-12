from enum import IntEnum, auto

import pygame as pg

from settings import *


class BuildingType(IntEnum):
    FARM = auto()
    MINE = auto()
    BARRACK = auto()


def farm_texture():
    s = pg.Surface((TILE, TILE), pg.SRCALPHA)
    pg.draw.rect(s, (170, 140, 60), (6, 14, 20, 12))
    for x in range(6, 26, 4):
        pg.draw.line(s, (200, 180, 90), (x, 14), (x, 26), 1)
    return s


def mine_texture():
    s = pg.Surface((TILE, TILE), pg.SRCALPHA)
    pg.draw.rect(s, (100, 100, 100), (6, 10, 20, 16))
    pg.draw.rect(s, (60, 60, 60), (12, 16, 8, 10))
    return s


def barrack_texture():
    s = pg.Surface((TILE, TILE), pg.SRCALPHA)
    pg.draw.rect(s, (130, 130, 130), (4, 10, 24, 16))
    pg.draw.rect(s, (100, 100, 100), (4, 6, 24, 6))
    pg.draw.line(s, (0, 0, 0), (16, 2), (16, 10), 2)
    pg.draw.polygon(s, (200, 50, 50), [(16, 2), (24, 4), (16, 6)])
    return s


building_textures = {
    BuildingType.FARM: farm_texture(),
    BuildingType.MINE: mine_texture(),
    BuildingType.BARRACK: barrack_texture()
}
