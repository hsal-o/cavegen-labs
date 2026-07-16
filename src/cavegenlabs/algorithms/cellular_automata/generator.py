from random import Random

from cavegenlabs.algorithms.cellular_automata.config import CellularAutomataConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


class CellularAutomataGenerator:
    def generate(
        self,
        config: CellularAutomataConfig,
        rng: Random
    ) -> CaveMap:
        # IMPLEMENT!!!

        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )