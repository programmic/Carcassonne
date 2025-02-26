import pygame
import re

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
    
        self.COL_ERROR: tuple[int] = (139, 1, 1)

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

    def get_color(self) -> tuple[int, int, int]:
        colors = {
            "grass": (34, 139, 34),
            "road": (139, 69, 19),
            "city": (128, 128, 128),
            "chapel": (255, 215, 0)
        }
        return colors
    
    def getEdgeColor(self, t: str) -> tuple[int, int, int]:
        colors: dict = self.get_color()
        if t == 'N': return colors.get("grass")
        if t == 'p': return colors.get("road")
        if t == 'c': return colors.get("city")

    def renderTile(self, TILE_SIZE, font):
        half_size = TILE_SIZE // 2
        quarter_size = TILE_SIZE // 4

        # Create a subcanvas
        subcanvas = pygame.Surface((TILE_SIZE, TILE_SIZE))

        # Define the points for the triangles
        points = [
            [(0, 0),            (TILE_SIZE, 0),         (half_size, half_size)],  # Top
            [(TILE_SIZE, 0),    (TILE_SIZE, TILE_SIZE), (half_size, half_size)],  # Right
            [(0, TILE_SIZE),    (TILE_SIZE, TILE_SIZE), (half_size, half_size)],  # Bottom
            [(0, 0),            (0, TILE_SIZE),         (half_size, half_size)]   # Left
        ]

        # Draw the triangles
        for i, edge in enumerate(self.edges):
            color = self.getEdgeColor(edge[0])
            pygame.draw.polygon(subcanvas, color, points[i])

        # Draw the chapel if present
        if self.chapel == "True":
            chapel_rect = pygame.Rect(quarter_size, quarter_size, half_size, half_size)
            pygame.draw.rect(subcanvas, (255, 215, 0), chapel_rect)  # Chapel color

        # Render the tile name
        if self.name:
            max_width = TILE_SIZE - 10  # Padding of 5 pixels on each side
            words = re.findall(r'[A-Z][^A-Z]*', self.name)
            lines = []
            current_line = words[0]

            for word in words[1:]:
                # Check the width of the current line with the next word added
                if font.size(current_line + word)[0] <= max_width:
                    current_line += word
                else:
                    if len(current_line) >= 2: lines.append(current_line)
                    current_line = word

            if len(current_line) >= 2: lines.append(current_line)

            # Render each line
            y_offset = half_size - (len(lines) * font.get_height() // 2)
            for line in lines:
                text_surface = font.render(line, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(half_size, y_offset))
                subcanvas.blit(text_surface, text_rect)
                y_offset += font.get_height()

        return subcanvas

