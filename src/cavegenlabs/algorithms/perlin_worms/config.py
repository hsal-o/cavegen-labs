from dataclasses import dataclass


@dataclass(frozen=True)
class PerlinWormsConfig:
    width: int 
    height: int
    octaves: int
    threshold: tuple[float, float]

    def __post_init__(self) -> None:
        if self.width <= 0:
            raise ValueError("Width must be greater than zero.")

        if self.height <= 0:
            raise ValueError("Height must be greater than zero.")
    
        lower_threshold, upper_threshold = self.threshold

        if lower_threshold >= upper_threshold:
            raise ValueError(
                "Lower threshold must be less than upper threshold."
            )

        if not -1.0 <= lower_threshold <= 1.0:
            raise ValueError(
                "Lower threshold must be between -1.0 and 1.0."
            )

        if not -1.0 <= upper_threshold <= 1.0:
            raise ValueError(
                "Upper threshold must be between -1.0 and 1.0."
            )