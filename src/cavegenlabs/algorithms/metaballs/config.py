from dataclasses import dataclass


@dataclass(frozen=True)
class MetaballsConfig:
    width: int
    height: int

    metaball_count: int
    negative_metaball_count: int

    min_radius: int
    max_radius: int

    threshold: float

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        if self.metaball_count <= 0:
            raise ValueError("Metaball count must be greater than zero.")
        
        if self.negative_metaball_count < 0:
            raise ValueError("Negative metaball count can not be less than.")

        if self.min_radius <= 0:
            raise ValueError("Minimum radius must be greater than zero.")

        if self.max_radius <= 0:
            raise ValueError("Maximum radius must be greater than zero.")
        
        if self.min_radius > self.max_radius:
            raise ValueError(
                "Minimum radius cannot be greater than maximum radius."
            )
        
        if self.width <= self.max_radius * 2:
            raise ValueError(
                "Width must be greater than twice the maximum radius."
            )

        if self.height <= self.max_radius * 2:
            raise ValueError(
                "Height must be greater than twice the maximum radius."
            )
        
        if self.threshold <= 0:
            raise ValueError("Threshold must be greater than zero.")