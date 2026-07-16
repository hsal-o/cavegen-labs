from dataclasses import dataclass


@dataclass(frozen=True)
class CellularAutomataConfig:
    width: int
    height: int 
    iteration_count: int
    nonsolid_odds: float
    solidify_threshold: int
    nonsolidify_threshold : int

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        if self.iteration_count < 0:
            raise ValueError("Iteration count can not be negative.")
        
        if not 0.0 <= self.nonsolid_odds <= 1.0:
            raise ValueError(
                "Nonsolid odds must be between 0.0 and 1.0."
            )

        if not 0 <= self.solidify_threshold <= 8:
            raise ValueError(
                "Solidify threshold must be between 0 and 8."
            )

        if not 0 <= self.nonsolidify_threshold <= 8:
            raise ValueError(
                "Nonsolidify threshold must be between 0 and 8."
            )
