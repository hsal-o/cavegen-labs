
from dataclasses import dataclass
from random import Random

from cavegenlabs.algorithms.binary_space_partition.config import BinarySpacePartitionConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


@dataclass
class Room:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def center_x(self) -> int:
        return (self.x2 + self.x1) // 2

    @property
    def center_y(self) -> int:
        return (self.y2 + self.y1) // 2

    @property
    def center_coord(self) -> tuple[int, int]:
        return (
            self.center_x,
            self.center_y,
        )


class BinarySpacePartitionGenerator:
    _SIDE_LEFT = 0
    _SIDE_TOP = 1
    _SIDE_RIGHT = 2
    _SIDE_BOTTOM = 3
    
    def generate(
        self,
        config: BinarySpacePartitionConfig,
        rng: Random
    ) -> CaveMap:
        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        self._generate_cut(
            grid=grid,
            config=config,
            rng=rng,
            start_coord=(0, 0),
            end_coord=(
                config.width,
                config.height,
            ),
            iteration_count=0,
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )
    
    def _generate_cut(
        self,
        grid: list[list[Tile]],
        config: BinarySpacePartitionConfig,
        rng: Random,
        start_coord: tuple[int, int],
        end_coord: tuple[int, int],
        iteration_count: int,
    ) -> list[Room]:
        ...