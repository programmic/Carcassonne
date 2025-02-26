from tile import Tile

class Grid:
    """
    Grid is x positive right\n
    Grid is y positive down
    """

    def __init__(self):
        """
        Initialize the grid as an empty dictionary.
        The keys are tuples representing coordinates (x, y),
        and the values are Tile objects.
        """
        self.grid: dict[tuple[int, int], Tile] = {}

    def __setitem__(self, key: tuple[int, int], value: Tile) -> None:
        """
        Assign a Tile to a specific coordinate in the grid.
        
        Args:
            key (tuple[int, int]): The (x, y) coordinates.
            value (Tile): The Tile object to place at the coordinates.
        """
        self.grid[key] = value

    def __getitem__(self, key: tuple[int, int]) -> Tile | None:
        """
        Retrieve a Tile from a specific coordinate in the grid.
        
        Args:
            key (tuple[int, int]): The (x, y) coordinates.
        
        Returns:
            Tile | None: The Tile object at the coordinates, or None if empty.
        """
        return self.grid.get(key)

    def getTile(self, x: int, y: int) -> Tile | None:
        """
        Retrieve a Tile from a specific coordinate in the grid.
        
        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        
        Returns:
            Tile | None: The Tile object at the coordinates, or None if empty.
        """
        return self.grid.get((x, y), None)
    
    def getTiles(self) -> list[Tile]:
        """
        Retrieve all Tiles in the grid.
        
        Returns:
            list[Tile]: A list of all Tile objects in the grid.
        """
        return list(self.grid.values())

    def getTilePositions(self):
        """
        Get the positions of all tiles in the grid.
        
        Returns:
            list[tuple[Tile, int, int]]: A list of tuples containing the Tile object and its (x, y) coordinates.
        """
        return [(tile, x, y) for (x, y), tile in self.grid.items()]

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