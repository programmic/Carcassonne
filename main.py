import json

from tile import *
from grid import *
from placing import *

def findTile(name: str) -> dict:
    for i in tiles:
        if i.get("name") == name:  # Assumes each tile has a 'name' key
            print(i, " -:-  ", str(type(i)))
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
    print (t.__repr__)
    return t

def fillPool():
    for i in tiles:
        for n in range(i.get("pool")): 
            pool.append(i.get("name"))


if __name__ == "__main__":
    print("\033c")
    with open("tiles.json", "r") as file:
        data = json.load(file)
    global tiles ; tiles = data.get("Tiles")
    global grid  ; grid = Grid()
    global pool  ; pool: list[ str ] = []


    grid[(0,0)] = constructTile("StartTile")

    print(grid[(0,0)])


    fillPool()