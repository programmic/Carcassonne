from tile import *
from grid import *
def canPlaceHere(t1: Tile, grid: Grid, x: int, y: int) -> bool:
    c = Grid.getTile(x, y)