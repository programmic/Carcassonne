class Tile:
    def __init__(
            self, 
            name: str = None,
            edges: list[str] = [None, None, None, None],
            chapel: bool = None,
            rotation: int = 0
            ):
        
        self.name = name
        self.edges = edges
        self.chapel = chapel
        self.rotation = 0
        self.meeplePosition = None
        self.meepleOwner = None
    
    def printout(self):
        print(f"Tile(\033[35m\n\tname={self.name}\n\tedges={self.edges}\n\tchapel={self.chapel}\n\trotation={self.rotation}\n\033[0m)")
    
    def __repr__(self):
        return f"Tile(\033[35m\n  -name={self.name}\n  -edges={self.edges}\n  -chapel={self.chapel}\n  -rotation={self.rotation}\n\033[0m)"

    def setup(self, edges: list[str], chapel: bool):
        if len(edges) != 4:
            raise ValueError(f"Tile must have 4 edges: Given tile has: {edges}")
        self.edges = edges
        self.chapel = chapel
    
    def setRotation(self, rotation: int):
        if rotation % 90 != 0:
            raise ValueError("Rotation must be a multiple of 90 degrees")
        else:
            self.rotation = rotation

    def setMeeple(self, position, owner):
        self.meeplePosition = position
        self.meepleOwner = owner