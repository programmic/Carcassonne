import json
import random

from tile import *
from grid import *

def findTile(name: str) -> dict:
    for i in tiles:
        if i.get("name") == name:
            return i
    print(f"\033[31mERROR: TILE NOT FOUND: {name}\033[0m")
    return None

def constructTile(name: str) -> Tile:
    d: dict = findTile(name)
    t = Tile( 
        d.get("name"),
        [
            d.get("edges").get("u"),
            d.get("edges").get("r"),
            d.get("edges").get("d"),
            d.get("edges").get("l")
        ],
        d.get("chapel")
        )
    return t

def fillPool():
    generatePool: list[str] = []
    for i in tiles:
        for n in range(i.get("pool")): 
            generatePool.append(i.get("name"))
    return generatePool

def canPlace(x: int, y: int, piece: (str | Tile) ) -> bool:
    tile: str    = piece if isinstance(piece, Tile) else constructTile(piece)
    n: Grid      = grid.getNeighbours(x, y)
    e: list[str] = tile.edges
    
    if (n[0] != "EMPTY") and (n[0][0] != e[0][0]): return False
    if (n[1] != "EMPTY") and (n[1][0] != e[1][0]): return False
    if (n[2] != "EMPTY") and (n[2][0] != e[2][0]): return False
    if (n[3] != "EMPTY") and (n[3][0] != e[3][0]): return False
    return True

if __name__ == "__main__":
    print("\033c",end="")
    with open("tiles.json", "r") as file:
        data = json.load(file)
    global tiles ; tiles = data.get("Tiles")
    grid: Grid = Grid()
    pool: list[ str ] = fillPool()

    grid[(0,-1)]= constructTile("Cap")
    grid[(0,1)] = constructTile("Chapel")

    print(canPlace(0,0, "Channel"))

