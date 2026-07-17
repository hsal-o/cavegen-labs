from dataclasses import dataclass


@dataclass(frozen=True)
class DiffusionLimitedAggregationConfig:
    width: int
    height: int
    particle_count: int
    stroke_thickness: int

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        if self.particle_count <= 0:
            raise ValueError("Particle count must be greater than zero.")
        
        if self.stroke_thickness <= 0:
            raise ValueError("Stroke thickness must be greater than zero.")
        