from random import Random

from cavegenlabs.algorithms.perlin_worms.config import PerlinWormsConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


class PerlinWormsGenerator:
    def generate(
        self,
        config: PerlinWormsConfig,
        rng: Random
    ) -> CaveMap:
        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        # IMPLEMENT!!!

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )