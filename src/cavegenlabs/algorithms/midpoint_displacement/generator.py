from random import Random

from cavegenlabs.algorithms.midpoint_displacement.config import MidpointDisplacementConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


class MidpointDisplacementGenerator:
    def generate(
        self,
        config: MidpointDisplacementConfig,
        rng: Random
    ) -> CaveMap:
        # IMPLEMENT ME!

        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )