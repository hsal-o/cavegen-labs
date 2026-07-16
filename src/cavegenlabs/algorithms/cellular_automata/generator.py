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
        grid = self._generate_initial_grid(
            width=config.width,
            height=config.height,
            rng=rng,
            nonsolid_odds=config.nonsolid_odds
        )

        self._apply_iterations(
            grid=grid,
            config=config
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid),
        )
    
    def _apply_iterations(
        self,
        grid: list[list[Tile]],
        config: CellularAutomataConfig
    ) -> None:
        for _ in range(config.iteration_count):
            grid[:] = self._generate_iteration(
                grid=grid,
                width=config.width,
                height=config.height,
                num_to_turn_solid=config.solidify_threshold,
                num_to_turn_nonsolid=config.nonsolidify_threshold,
            )

    def _generate_initial_grid(
        self,
        width: int,
        height: int,
        rng: Random,
        nonsolid_odds: float
    ) -> list[list[Tile]]:
        grid = [
            [Tile.AIR for _ in range(width)]
            for _ in range(height)
        ]

        for y in range(height):
            for x in range(width):
                if (
                    y == 0 or
                    x == 0 or
                    y == height - 1 or
                    x == width - 1
                ):
                    grid[y][x] = Tile.SOLID
                    continue

                chance = rng.random()

                grid[y][x] = (
                    Tile.AIR if chance <= nonsolid_odds else Tile.SOLID
                )
            
        return grid
    
    def _count_solid_neighbors(
        self,
        grid: list[list[Tile]],
        width: int,
        height: int,
        y: int,
        x: int,
    ) -> int:
        count = 0

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue

                ny = y + dy
                nx = x + dx

                if (
                    ny < 0 or
                    nx < 0 or
                    ny >= height or
                    nx >= width
                ):
                    continue

                if grid[ny][nx] is Tile.SOLID:
                    count += 1

        return count
    
    def _generate_iteration(
        self,
        grid: list[list[Tile]],
        width: int,
        height: int,
        num_to_turn_solid: int,
        num_to_turn_nonsolid: int,
    ) -> list[list[Tile]]:
        new_grid = [
            row.copy() for row in grid
        ]

        for y in range(height):
            for x in range(width):
                # Exclude border cells
                if (
                    y == 0 or
                    x == 0 or 
                    y == height - 1 or
                    x == width - 1
                ):
                    new_grid[y][x] = Tile.SOLID
                    continue

                num_solid_neighbors = self._count_solid_neighbors(
                    grid=grid,
                    width=width,
                    height=height,
                    y=y,
                    x=x
                )

                # If current cell is Solid
                if grid[y][x] is Tile.SOLID:
                    if num_solid_neighbors < num_to_turn_nonsolid:
                        # Cell turns nonsolid due to under/overpopulation
                        new_grid[y][x] = Tile.AIR
                    else:
                        # Cell remains solid
                        new_grid[y][x] = Tile.SOLID

                # If current cell is NonSolid
                else:
                    if num_solid_neighbors > num_to_turn_solid:
                        # Cell turns solid due to reproduction
                        new_grid[y][x] = Tile.SOLID
                    else:
                        # Cell remains nonsolid
                        new_grid[y][x] = Tile.AIR

        return new_grid


