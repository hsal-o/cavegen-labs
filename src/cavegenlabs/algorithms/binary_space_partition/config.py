from dataclasses import dataclass


@dataclass(frozen=True)
class BinarySpacePartitionConfig:
    width: int
    height: int
    iteration_count: int 
    min_width: int
    min_height: int
    start_coord: tuple[int, int]
    end_coord: tuple[int, int]

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
        
        start_x, start_y = self.start_coord
        end_x, end_y = self.end_coord

        if not 0 <= start_x < self.width:
            raise ValueError("Start X coordinate is out of bounds.")

        if not 0 <= start_y < self.height:
            raise ValueError("Start Y coordinate is out of bounds.")

        if not 0 <= end_x < self.width:
            raise ValueError("End X coordinate is out of bounds.")

        if not 0 <= end_y < self.height:
            raise ValueError("End Y coordinate is out of bounds.")

        if start_x > end_x:
            raise ValueError(
                "Start X coordinate cannot be greater than end X coordinate."
            )

        if start_y > end_y:
            raise ValueError(
                "Start Y coordinate cannot be greater than end Y coordinate."
            )

        if self.hallway_stroke_thickness <= 0:
            raise ValueError("Hallway stroke thickness must be greater than zero.")