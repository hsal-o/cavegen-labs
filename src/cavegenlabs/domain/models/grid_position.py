from enum import Enum
from random import Random


class GridPosition(Enum):
    CUSTOM = "custom"
    RANDOM = "random"
    TOP_LEFT = "top_left"
    TOP_CENTER = "top_center"
    TOP_RIGHT = "top_right"
    CENTER_LEFT = "center_left"
    CENTER = "center"
    CENTER_RIGHT = "center_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_CENTER = "bottom_center"
    BOTTOM_RIGHT = "bottom_right"

    def resolve(
        self,
        width: int,
        height: int,
        rng: Random,
        custom_x: int = 0,
        custom_y: int = 0,
    ) -> tuple[int, int]:
        max_x = width - 1
        max_y = height - 1

        match self:
            case GridPosition.TOP_LEFT:
                return 0, 0
            case GridPosition.TOP_CENTER:
                return max_x // 2, 0
            case GridPosition.TOP_RIGHT:
                return max_x, 0
            case GridPosition.CENTER_LEFT:
                return 0, max_y // 2
            case GridPosition.CENTER:
                return max_x // 2, max_y // 2
            case GridPosition.CENTER_RIGHT:
                return max_x, max_y // 2
            case GridPosition.BOTTOM_LEFT:
                return 0, max_y
            case GridPosition.BOTTOM_CENTER:
                return max_x // 2, max_y
            case GridPosition.BOTTOM_RIGHT:
                return max_x, max_y
            case GridPosition.RANDOM:
                return rng.randint(0, max_x), rng.randint(0, max_y)
            case GridPosition.CUSTOM:
                return (
                    max(0, min(custom_x, max_x)),
                    max(0, min(custom_y, max_y)),
                )