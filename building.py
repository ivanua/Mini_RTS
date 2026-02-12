from game_object import GameObject, GameObjectType
from textures import BuildingType, building_textures
from settings import *


class Building(GameObject):
    def __init__(self, game, pos, bld_type = BuildingType.FARM):
        super().__init__(game, pos, GameObjectType.BUILDING)

        self.bld_type = bld_type

    def draw(self):
        px, py = self.x * TILE, self.y * TILE
        self.game.screen.blit(building_textures[self.bld_type], (px, py))
