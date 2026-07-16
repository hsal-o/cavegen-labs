from random import Random

from perlin_noise import PerlinNoise

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

        lower_bound, upper_bound = config.threshold

        self._generate_perlin_noise(
            grid=grid,
            width=config.width,
            height=config.height,
            octave=config.octaves,
            rng=rng,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )
    
    def _generate_perlin_noise(
        self,
        grid: list[list[Tile]],
        width: int,
        height: int,
        octave: int,
        rng: Random,
        lower_bound: float,
        upper_bound: float,
    ) -> None:
        noise = PerlinNoise(
            octaves=octave,
            seed=rng.getrandbits(32),
        )

        for y in range(height):
            for x in range(width):
                perlin_noise_value = (
                    self._get_normalized_perlin_value(
                        noise=noise,
                        x=x,
                        y=y,
                        width=width,
                        height=height,
                    )
                )

                self._apply_perlin_worm_point(
                    grid=grid,
                    x=x,
                    y=y,
                    perlin_noise_value=perlin_noise_value,
                    lower_bound=lower_bound,
                    upper_bound=upper_bound,
                )

    def _get_normalized_perlin_value(
        self,
        noise: PerlinNoise,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> float:
        normalized_x = x / width
        normalized_y = y / height

        return noise([normalized_x, normalized_y])

    def _apply_perlin_worm_point(
        self,
        grid: list[list[Tile]],
        x: int,
        y: int,
        perlin_noise_value: float,
        lower_bound: float,
        upper_bound: float,
    ) -> None:
        if lower_bound < perlin_noise_value < upper_bound:
            grid[y][x] = Tile.AIR
        else:
            grid[y][x] = Tile.SOLID