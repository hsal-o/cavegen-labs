from math import ceil, floor
from random import Random

from cavegenlabs.algorithms.random_walk.config import RandomWalkConfig
from cavegenlabs.domain.models import CaveMap, Tile


class RandomWalkGenerator:
    def generate(
        self,
        config: RandomWalkConfig,
        rng: Random
    ) -> CaveMap:
        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        for _ in range(config.walker_count):
            start_x, start_y = config.start_position.resolve(
                width=config.width,
                height=config.height,
                rng=rng,
            )

            end_x, end_y = config.end_position.resolve(
                width=config.width,
                height=config.height,
                rng=rng,
            )

            self._generate_steps(
                grid=grid,
                config=config,
                rng=rng,
                start_x=start_x,
                start_y=start_y,
                end_x=end_x,
                end_y=end_y,
            )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )

    def _generate_steps(
        self,
        grid: list[list[Tile]],
        config: RandomWalkConfig,
        rng: Random,
        start_x: int,
        start_y: int,
        end_x: int,
        end_y: int,
    ) -> None:
        current_x = start_x
        current_y = start_y

        self._paint_step(
            grid=grid,
            width=config.width,
            height=config.height,
            thickness=config.thickness,
            x=current_x,
            y=current_y,
        )

        for _ in range(config.step_count - 1):
            previous_x = current_x
            previous_y = current_y

            direction = self._choose_direction(
                rng=rng,
                bias=config.bias,
                current_x=current_x,
                current_y=current_y,
                end_x=end_x,
                end_y=end_y,
            )

            match direction:
                case 0:
                    current_y -= 1
                case 1:
                    current_x += 1
                case 2:
                    current_y += 1
                case 3:
                    current_x -= 1

            if not 0 <= current_x < config.width:
                current_x = previous_x

            if not 0 <= current_y < config.height:
                current_y = previous_y

            if current_x == previous_x and current_y == previous_y:
                continue

            self._paint_step(
                grid=grid,
                width=config.width,
                height=config.height,
                thickness=config.thickness,
                x=current_x,
                y=current_y,
            )

    def _choose_direction(
        self,
        rng: Random,
        bias: float,
        current_x: int,
        current_y: int,
        end_x: int,
        end_y: int,
    ) -> int:
        possible_directions = (0, 1, 2, 3)

        if bias == 0.0 or rng.random() >= bias:
            return rng.choice(possible_directions)

        biased_directions: list[int] = []

        if end_y < current_y:
            biased_directions.append(0)

        if end_x > current_x:
            biased_directions.append(1)

        if end_y > current_y:
            biased_directions.append(2)

        if end_x < current_x:
            biased_directions.append(3)

        if not biased_directions:
            return rng.choice(possible_directions)

        return rng.choice(biased_directions)

    def _paint_step(
        self,
        grid: list[list[Tile]],
        width: int,
        height: int,
        thickness: int,
        x: int,
        y: int,
    ) -> None:
        negative_extent  = (thickness - 1) // 2
        positive_extent  = thickness // 2

        for paint_x in range(x - negative_extent , x + positive_extent  + 1):
            for paint_y in range(y - negative_extent , y + positive_extent  + 1):
                if 0 <= paint_x < width and 0 <= paint_y < height:
                    grid[paint_y][paint_x] = Tile.AIR