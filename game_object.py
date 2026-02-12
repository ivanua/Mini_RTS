from enum import IntEnum, auto

import pygame as pg


class GameObjectType(IntEnum):
    BUILDING = auto()
    UNIT = auto()
    NONE = auto()


class GameObject(pg.sprite.Sprite):
    def __init__(self, game, pos, obj_type = GameObjectType.NONE, *groups):
        super().__init__(*groups)

        self.game = game
        self.obj_type = obj_type
        self.x = pos[0]
        self.y = pos[1]

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return abs(self.x), abs(self.y)
