from dataclasses import dataclass
from random import Random

from cavegenlabs.algorithms.diffusion_limited_aggregation.config import DiffusionLimitedAggregationConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile

@dataclass
class Particle:
    x: int
    y: int 

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

        self._create_seed(
            grid=grid,
            config=config
        )

        self._grow_cave(
            grid=grid,
            config=config,
            rng=rng
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )
    
    def _create_seed(
        self,
        grid: list[list[Tile]],
        config: DiffusionLimitedAggregationConfig
    ) -> None:
        grid[config.height // 2][config.width // 2] = Tile.AIR

    def _grow_cave(
        self,
        grid: list[list[Tile]],
        config: DiffusionLimitedAggregationConfig,
        rng: Random
    ) -> None:
        for _ in range(config.particle_count):
            particle = self._spawn_particle(
                config=config,
                rng=rng,
            )

            self._simulate_particle(
                config=config,
                grid=grid,
                particle=particle,
                rng=rng
            )

    def _spawn_particle(
        self,
        config: DiffusionLimitedAggregationConfig,
        rng: Random
    ) -> Particle:
        side = rng.randint(0, 3)

        match side:
            # Left
            case 0:
                return Particle(
                    x=0,
                    y=rng.randrange(config.height),
                )
            
            # Top
            case 1:
                return Particle(
                    x=rng.randrange(config.width),
                    y=0,
                )
            
            # Right
            case 2:
                return Particle(
                    x=config.width - 1,
                    y=rng.randrange(config.height),
                )
            
            # Bottom
            case 3:
                return Particle(
                    x=rng.randrange(config.width),
                    y=config.height - 1,
                )
            
    def _simulate_particle(
        self,
        grid: list[list[Tile]],
        config: DiffusionLimitedAggregationConfig,
        particle: Particle,
        rng: Random
    ) -> None:
        for _ in range(config.width * config.height):
            self._move_particle(
                config=config,
                particle=particle,
                rng=rng
            )

            if self._is_touching_cave(
                grid=grid,
                particle=particle
            ):
                grid[particle.y][particle.x] = Tile.AIR
                return
            
    def _move_particle(
        self,
        config: DiffusionLimitedAggregationConfig,
        particle: Particle,
        rng: Random
    ) -> None:
        direction = rng.randint(0, 3)

        match direction:
            # Left
            case 0:
                if particle.x > 0:
                    particle.x -= 1

            # Up
            case 1:
                if particle.y > 0:
                    particle.y -= 1

            # Right
            case 2:
                if particle.x < config.width - 1:
                    particle.x += 1

            # Down
            case 3: 
                if particle.y < config.height - 1:
                    particle.y += 1

    def _is_touching_cave(
        self,
        grid: list[list[Tile]],
        particle: Particle
    ) -> bool:
        directions = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        )

        for delta_x, delta_y in directions:
            x = particle.x + delta_x
            y = particle.y + delta_y

            if (
                0 <= x < len(grid[0]) and
                0 <= y < len(grid) and
                grid[y][x] == Tile.AIR
            ):
                return True
            
        return False