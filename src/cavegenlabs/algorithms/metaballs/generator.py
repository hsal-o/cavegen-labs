from dataclasses import dataclass
from math import hypot
from random import Random

from cavegenlabs.algorithms.metaballs.config import MetaballsConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile

@dataclass(frozen=True)
class Cluster:
    center_x: int
    center_y: int

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

        clusters = self._generate_clusters(
            config=config,
            rng=rng
        )

        metaballs = self._generate_metaballs(
            config=config,
            rng=rng,
            clusters=clusters
        )

        self._carve_metaballs(
            grid=grid,
            config=config,
            metaballs=metaballs
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid)
        )
    
    def _generate_clusters(
        self,
        config: MetaballsConfig,
        rng: Random
    ) -> list[Cluster]:
        if config.cluster_count == 0:
            return []

        clusters: list[Cluster] = []

        spread = config.cluster_spread

        for _ in range(config.cluster_count):
            clusters.append(
                Cluster(
                    center_x=rng.randrange(
                        spread,
                        config.width - spread,
                    ),
                    center_y=rng.randrange(
                        spread,
                        config.height - spread,
                    ),
                )
            )

        return clusters

    def _generate_metaballs(
        self,
        config: MetaballsConfig,
        rng: Random,
        clusters: list[Cluster]
    ) -> list[Metaball]:
        metaballs: list[Metaball] = []

        for _ in range(config.metaball_count):
            metaballs.append(
                self._generate_metaball(
                    config=config,
                    rng=rng,
                    clusters=clusters,
                    is_negative=False
                )
            )

        for _ in range(config.negative_metaball_count):
            metaballs.append(
                self._generate_metaball(
                    config=config,
                    rng=rng,
                    clusters=clusters,
                    is_negative=True
                )
            )
        
        return metaballs
    
    def _generate_metaball(
        self,
        config: MetaballsConfig,
        rng: Random,
        clusters: list[Cluster],
        is_negative: bool,
    ) -> Metaball:
        radius = rng.randint(
            config.min_radius,
            config.max_radius
        )

        if not clusters:
            return Metaball(
                center_x=rng.randrange(radius, config.width - radius),
                center_y=rng.randrange(radius, config.height - radius),
                radius=radius,
                is_negative=is_negative,
            )

        cluster = rng.choice(clusters)
        spread = config.cluster_spread
        center_x = max(
                radius,
                min(
                    cluster.center_x + rng.randint(-spread, spread),
                    config.width - radius,
                ),
            )
        center_y = max(
            radius,
            min(
                cluster.center_y + rng.randint(-spread, spread),
                config.height - radius,
            ),
        )

        return Metaball(
            center_x=center_x,
            center_y=center_y,
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
        delta_x = x - metaball.center_x
        delta_y = y - metaball.center_y

        distance_squared = delta_x ** 2 + delta_y ** 2

        if distance_squared == 0:
            if metaball.is_negative:
                return float("-inf")
            else:
                return float("inf")
        
        influence = (metaball.radius ** 2) / distance_squared

        return -influence if metaball.is_negative else influence