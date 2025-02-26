import json
import pygame
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
    tile: Tile = piece if isinstance(piece, Tile) else constructTile(piece)
    n: list[str] = grid.getNeighbours(x, y)
    e: list[str] = tile.edges

    # Check if the edges match with the neighboring tiles
    if (n[0] != "EMPTY") and (n[0] != e[0]): return False
    if (n[1] != "EMPTY") and (n[1] != e[1]): return False
    if (n[2] != "EMPTY") and (n[2] != e[2]): return False
    if (n[3] != "EMPTY") and (n[3] != e[3]): return False
    return True

def populateCenter(spread: int, count: int):
    center_x, center_y = 0, 0
    placed_tiles = 0

    while placed_tiles < count:
        x = random.randint(center_x - spread, center_x + spread)
        y = random.randint(center_y - spread, center_y + spread)
        print(f"placing tile at ({x}|{y}) - placed tiles: {placed_tiles}")
        if grid.getTile(x, y) == None:
            tile_name = random.choice(pool)
            if canPlace(x, y, tile_name): # placing logic still sucks
                grid[x,y] = constructTile(tile_name)
                #pool.remove(tile_name)
                placed_tiles += 1
    print(f"Populated map with {count} tiles")

if __name__ == "__main__":
    print("\033c",end="")
    with open("tiles.json", "r") as file:
        data = json.load(file)
    global tiles ; tiles = data.get("Tiles")
    grid: Grid = Grid()
    pool: list[ str ] = fillPool()
    # set (0|0) so start Tile
    grid[0, 0] = constructTile("StartTile")
    populateCenter(4,40)

    VAMPIRE_GRAY: tuple[int] = (12, 15, 20)
    print(grid.getTiles())
    for i in grid.getTiles(): print(i.name)

    # pygame setup
    pygame.init()
    font = pygame.font.SysFont(None, 16)
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    TILE_SIZE = 64  # Assuming each tile is 64x64 pixels
    zoom = 1.0
    offset_x, offset_y = 0, 0
    dragging = False
    drag_start_x, drag_start_y = 0, 0

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:  # Middle mouse button
                    dragging = True
                    drag_start_x, drag_start_y = event.pos
                elif event.button == 4:  # Scroll up
                    zoom *= 1.1
                elif event.button == 5:  # Scroll down
                    zoom /= 1.1
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:  # Middle mouse button
                    dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    dx, dy = event.pos[0] - drag_start_x, event.pos[1] - drag_start_y
                    offset_x += dx
                    offset_y += dy
                    drag_start_x, drag_start_y = event.pos

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(VAMPIRE_GRAY)

        for tile, x, y in grid.getTilePositions():
            tile_surface = tile.renderTile(int(TILE_SIZE * zoom), font)
            screen.blit(
                tile_surface, 
                (
                    screen.get_width()  // 2 - TILE_SIZE / 2 + x * TILE_SIZE * zoom + offset_x,
                    screen.get_height() // 2 - TILE_SIZE / 2 + y * TILE_SIZE * zoom + offset_y
                )
            )

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()