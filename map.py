import pygame as pg

_ = False
mini_map = [
    [1, 1, 2, 1, 2, 1, 3, 6, 6, 5, 5, 1, 1, 4, 1, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4],
    [2, _, _, 2, 3, 4, 5, _, _, _, 6, 5, 2, _, _, 4],
    [1, _, _, _, _, _, 6, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 3],
    [2, _, _, 3, 2, 3, 2, _, _, _, _, _, _, _, _, 3],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [1, _, _, 1, _, _, 6, _, _, _, _, _, _, _, _, 1],
    [1, 1, 2, 1, 3, 2, 6, 3, 3, 1, 5, 5, 5, 3, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'dark gray', (pos[0]*100, pos[1]*100, 100, 100), 2)
         for pos in self.world_map]
