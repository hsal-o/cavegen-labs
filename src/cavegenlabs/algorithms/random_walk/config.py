from dataclasses import dataclass

from cavegenlabs.domain.models.grid_position import GridPosition


@dataclass(frozen=True)
class RandomWalkConfig:
    width: int
    height: int
    walker_count: int
    step_count: int
    thickness: int
    bias: float
    start_position: GridPosition
    end_position: GridPosition

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")

        if self.walker_count <= 0:
            raise ValueError("Walker count must be greater than zero.")

        if self.step_count <= 0:
            raise ValueError("Step count must be greater than zero.")

        if self.thickness <= 0:
            raise ValueError("Thickness must be greater than zero.")

        if not 0.0 <= self.bias <= 1.0:
            raise ValueError("Bias must be between 0 and 1.")