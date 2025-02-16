from tile import Tile

class Grid:
    def __init__(self):
        self.grid: dict[tuple[int, int], Tile] = {}

    def __setitem__(self, key: tuple[int, int], value: Tile) -> None:
        self.grid[key] = value

    def __getitem__(self, key: tuple[int, int]) -> Tile | None:
        return self.grid.get(key)

    def getTile(self, x: int, y: int) -> Tile | None:
        return self.grid.get((x, y), None)


if __name__ == "__main__":
    grid = Grid()
    grid[(22, 9)] = Tile()
    tile = grid.getTile(22, 9)
    print(tile)
