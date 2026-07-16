from math import ceil, floor
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
        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        start_x, start_y = config.start_position.resolve(
            width=config.width,
            height=config.height,
            rng=rng
        )

        end_x, end_y = config.end_position.resolve(
            width=config.width,
            height=config.height,
            rng=rng
        )

        points = self._generate_points(
            width=config.width,
            height=config.height,
            rng=rng,
            x1=start_x,
            y1=start_y,
            x2=end_x,
            y2=end_y,
            magnitude=config.magnitude,
            step=config.iteration_count
        )

        self._connect_points(
            grid=grid,
            width=config.width,
            height=config.height,
            rng=rng,
            points=points,
            stroke_thickness=config.thickness,
            thickness_variation=config.thickness_variation
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )
    
    def _generate_points(
        self,
        width: int,
        height: int,
        rng: Random,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        magnitude: int,
        step: int
    ) -> list[tuple[float, float]]:
        # End case
        if step == 0:
            return [(x1, y1), (x2, y2)]
        
        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2

        new_midpoint_x = midpoint_x + rng.randint(
            -magnitude,
            magnitude,
        )
        new_midpoint_y = midpoint_y + rng.randint(
            -magnitude,
            magnitude,
        )

        new_midpoint_x = max(
            0,
            min(new_midpoint_x, width - 1),
        )
        new_midpoint_y = max(
            0,
            min(new_midpoint_y, height - 1),
        )

        points_start = self._generate_points(
            width=width,
            height=height,
            rng=rng,
            x1=x1,
            y1=y1,
            x2=new_midpoint_x,
            y2=new_midpoint_y,
            magnitude=magnitude,
            step=step-1,
        )

        points_end = self._generate_points(
            width=width,
            height=height,
            rng=rng,
            x1=new_midpoint_x,
            y1=new_midpoint_y,
            x2=x2,
            y2=y2,
            magnitude=magnitude,
            step=step-1,
        )

        return (
            points_start +
            [(new_midpoint_x, new_midpoint_y)] +
            points_end
        )

    def _connect_points(
        self,
        grid: list[list[Tile]],
        width: int,
        height: int,
        rng: Random,
        points: list[tuple[float, float]],
        stroke_thickness: int,
        thickness_variation: tuple[int, int],
    ) -> None:
        for i in range(len(points)-1):
            self._draw_line(
                grid=grid,
                width=width,
                height=height,
                rng=rng,
                x1=points[i][0],
                y1=points[i][1],
                x2=points[i+1][0],
                y2=points[i+1][1],
                stroke_thickness=stroke_thickness,
                thickness_variation=thickness_variation,
            )

    def _draw_line(
        self,
        grid: list[list[Tile]],
        width: int,
        height: int,
        rng: Random,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        stroke_thickness: int,
        thickness_variation: tuple[int, int],
    ) -> None:
        x1, y1 = int(x1), int(y1)
        x2, y2 = int(x2), int(y2)

        delta_x = abs(x2 - x1)
        delta_y = abs(y2 - y1)

        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        error = delta_x - delta_y

        if thickness_variation != (0, 0):
            increase, decrease = thickness_variation

            new_thickness = stroke_thickness + rng.choice(
                [-decrease, increase]
            )
        else:
            new_thickness = stroke_thickness

        max_iterations = width * height
        iterations = 0

        while True:
            if 0 <= x1 < width and 0 <= y1 < height:
                x_thickness = new_thickness - 1
                x_tt = ceil(x_thickness / 2)
                x_bt = floor(x_thickness / 2)

                y_thickness = new_thickness - 1
                y_tt = ceil(y_thickness / 2)
                y_bt = floor(y_thickness / 2)

                for paint_x in range(
                    max(0, x1 - x_tt),
                    min(width, x1 + x_bt + 1),
                ):
                    for paint_y in range(
                        max(0, y1 - y_tt),
                        min(height, y1 + y_bt + 1),
                    ):
                        grid[paint_y][paint_x] = Tile.AIR

            if x1 == x2 and y1 == y2:
                break

            e2 = 2 * error

            if e2 > -delta_y:
                error -= delta_y
                x1 += sx

            if e2 < delta_x:
                error += delta_x
                y1 += sy

            iterations += 1
            if iterations > max_iterations:
                break