from dataclasses import dataclass

from cavegenlabs.domain.models.grid_position import GridPosition


@dataclass(frozen=True)
class MidpointDisplacementConfig:
    width: int 
    height: int
    start_position: GridPosition
    end_position: GridPosition
    iteration_count: int 
    magnitude: int
    thickness: int
    thickness_variation: tuple[int, int]

    def __post_init__(self)  -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        if self.iteration_count < 0:
            raise ValueError("Iteration count can not be negative.")
        
        if self.magnitude < 0:
            raise ValueError("Magnitude can not be negative.")
        
        if self.thickness <= 0:
            raise ValueError("Thickness must be greater than zero.")
        
        negative_variation, positive_variation = self.thickness_variation

        if negative_variation < 0 or positive_variation < 0:
            raise ValueError("Thickness variation values can not be negative.")
        
        if self.thickness - negative_variation <= 0:
            raise ValueError("Negative thickness variation can not reduce thickness below one.")