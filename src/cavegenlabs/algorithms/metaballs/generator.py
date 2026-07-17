from random import Random

from cavegenlabs.algorithms.metaballs.config import MetaballsConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


class MetaballsGenerator:
    def generate(
        self,
        config: MetaballsConfig,
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