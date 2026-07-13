from dataclasses import dataclass

from cavegenlabs.domain.models.tile import Tile


@dataclass(frozen=True)
class CaveMap:
    width: int
    height: int 
    cells: tuple[tuple[Tile, ...], ...]

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")
        
        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        if len(self.cells) != self.height:
            raise ValueError("Cell row count must match height.")
        
        if any(len(row) != self.width for row in self.cells):
            raise ValueError("Each cell row must match width.")
        
    def get_tile(self, x: int, y: int) -> Tile:
        if not self.is_in_bounds(x, y):
            raise IndexError(f"Coordinates out of bounds: ({x}, {y})")
        
        return self.cells[y][x]
    
    def is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x and x < self.width and 0 <= y and y < self.height