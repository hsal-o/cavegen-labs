from random import Random

from cavegenlabs.algorithms.diffusion_limited_aggregation.config import DiffusionLimitedAggregationConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


class DiffusionLimitedAggregationGenerator:
    def generate(
        self,
        config: DiffusionLimitedAggregationConfig,
        rng: Random
    ) -> CaveMap:
        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        # IMPLEMENT ME!!!

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )