from dataclasses import dataclass


@dataclass(frozen=True)
class BinarySpacePartitionConfig:
    width: int
    height: int
    iteration_count: int 
    min_width: int
    min_height: int
    
    do_connect_rooms: bool
    hallway_stroke_thickness: int
    
    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        if self.iteration_count < 0:
            raise ValueError("Iteration count can not be negative.")
        
        if not 0 < self.min_width < self.width:
            raise ValueError("Minimum width must be greater than 0 and less than width.")
        
        if not 0 < self.min_height < self.height:
            raise ValueError("Minimum width must be greater than 0 and less than height.")

        if self.hallway_stroke_thickness <= 0:
            raise ValueError("Hallway stroke thickness must be greater than zero.")