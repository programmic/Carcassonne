from tile import Tile

class Grid:
    """
    Grid is x positive right\n
    Grid is y positive down
    """

    def __init__(self):
        self.grid: dict[tuple[int, int], Tile] = {}

    def __setitem__(self, key: tuple[int, int], value: Tile) -> None:
        self.grid[key] = value

    def __getitem__(self, key: tuple[int, int]) -> Tile | None:
        return self.grid.get(key)

    def getTile(self, x: int, y: int) -> Tile | None:
        return self.grid.get((x, y), None)

    def getNeighbours(self, x: int, y: int) -> list[str]:
        uT: Tile | None = self.grid.get((x, y-1))
        rT: Tile | None = self.grid.get((x+1, y))
        dT: Tile | None = self.grid.get((x, y+1))
        lT: Tile | None = self.grid.get((x-1, y))

        u = uT.edges[2] if uT else "EMPTY"
        r = rT.edges[3] if rT else "EMPTY"
        d = dT.edges[0] if dT else "EMPTY"
        l = lT.edges[1] if lT else "EMPTY"
        return [ u, r, d, l ]

        