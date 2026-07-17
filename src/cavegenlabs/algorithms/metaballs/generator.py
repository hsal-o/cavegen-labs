from dataclasses import dataclass
from math import hypot
from random import Random

from cavegenlabs.algorithms.metaballs.config import MetaballsConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile

@dataclass(frozen=True)
class Metaball:
    center_x: int
    center_y: int
    radius: int
    is_negative: bool
    
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

        metaballs = self._generate_metaballs(
            config=config,
            rng=rng,
        )

        self._carve_metaballs(
            grid=grid,
            config=config,
            metaballs=metaballs,
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )

    def _generate_metaballs(
        self,
        config: MetaballsConfig,
        rng: Random
    ) -> list[Metaball]:
        metaballs: list[Metaball] = []

        for _ in range(config.metaball_count):
            metaballs.append(
                self._generate_metaball(
                    config=config,
                    rng=rng,
                    is_negative=False
                )
            )

        for _ in range(config.negative_metaball_count):
            metaballs.append(
                self._generate_metaball(
                    config=config,
                    rng=rng,
                    is_negative=True
                )
            )
        
        return metaballs
    
    def _generate_metaball(
    self,
    config: MetaballsConfig,
    rng: Random,
    is_negative: bool,
    ) -> Metaball:
        radius = rng.randint(
            config.min_radius,
            config.max_radius
        )

        return Metaball(
            center_x=rng.randrange(
                radius,
                config.width - radius
            ),
            center_y=rng.randrange(
                radius,
                config.height - radius
            ),
            radius=radius,
            is_negative=is_negative,
        )

    def _carve_metaballs(
        self,
        grid: list[list[Tile]],
        config: MetaballsConfig,
        metaballs: list[Metaball]
    ) -> None:
        for y in range(config.height):
            for x in range(config.width):
                influence = 0
                for metaball in metaballs:
                    influence += self._calculate_influence(
                        metaball=metaball,
                        x=x,
                        y=y 
                    )

                if influence >= config.threshold:
                    grid[y][x] = Tile.AIR

    def _calculate_influence(
        self,
        metaball: Metaball,
        x: int,
        y: int,
    ) -> float:
        distance = hypot(
            x - metaball.center_x,
            y - metaball.center_y
        )

        if distance == 0:
            return float("inf")
        
        influence = (metaball.radius ** 2) / (distance ** 2)
        if metaball.is_negative:
            return -influence

        return influence