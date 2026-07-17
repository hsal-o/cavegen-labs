
from dataclasses import dataclass
from random import Random

from cavegenlabs.algorithms.binary_space_partition.config import BinarySpacePartitionConfig
from cavegenlabs.domain.models.cave_map import CaveMap
from cavegenlabs.domain.models.tile import Tile


@dataclass
class Room:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def center_x(self) -> int:
        return (self.x2 + self.x1) // 2

    @property
    def center_y(self) -> int:
        return (self.y2 + self.y1) // 2

    @property
    def center_coord(self) -> tuple[int, int]:
        return (
            self.center_x,
            self.center_y,
        )


class BinarySpacePartitionGenerator:
    _SIDE_LEFT = 0
    _SIDE_TOP = 1
    _SIDE_RIGHT = 2
    _SIDE_BOTTOM = 3
    
    def generate(
        self,
        config: BinarySpacePartitionConfig,
        rng: Random
    ) -> CaveMap:
        grid = [
            [Tile.SOLID for _ in range(config.width)]
            for _ in range(config.height)
        ]

        self._generate_cut(
            grid=grid,
            config=config,
            rng=rng,
            start_coord=(0, 0),
            end_coord=(
                config.width,
                config.height,
            ),
            iteration_count=0
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=tuple(tuple(row) for row in grid)
        )
    
    def _generate_cut(
        self,
        grid: list[list[Tile]],
        config: BinarySpacePartitionConfig,
        rng: Random,
        start_coord: tuple[int, int],
        end_coord: tuple[int, int],
        iteration_count: int
    ) -> list[Room]:
        x1, y1 = start_coord
        x2, y2 = end_coord

        if(
            iteration_count >= config.iteration_count or
            x2 - x1 < config.min_width or
            y2 - y1 < config.min_height
        ):
            room = Room(
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2
            )

            return [
                self._generate_single_room(
                    grid=grid,
                    room=room
                )
            ]
        
        def cut_vertical() -> tuple[
            tuple[int, int],
            tuple[int, int]
        ]:
            bound = (x2 - x1) // 3

            middle_x = rng.randint(
                x1 + bound,
                x2 - bound
            )

            return (
                (middle_x, y1),
                (middle_x, y2)
            )
        
        def cut_horizontal() -> tuple[
            tuple[int, int],
            tuple[int, int],
        ]:
            bound = (y2 - y1) // 3

            middle_y = rng.randint(
                y1 + bound,
                y2 - bound
            )

            return (
                (x1, middle_y),
                (x2, middle_y)
            )
        
        width = x2 - x1
        height = y2 - y1

        # Vertical cut
        if width > height:
            middle_start_coord, middle_end_coord = (
                cut_vertical()
            )

        # Horizontal cut
        elif height > width:
            middle_start_coord, middle_end_coord = (
                cut_horizontal()
            )

        # Choose randomly
        else:
            # Vertical cut
            if rng.choice([0, 1]) == 0:
                middle_start_coord, middle_end_coord = (
                    cut_vertical()
                )

            # Horizontal cut
            else:
                middle_start_coord, middle_end_coord = (
                    cut_horizontal()
                )

        alpha_rooms = self._generate_cut(
            grid=grid,
            config=config,
            rng=rng,
            start_coord=start_coord,
            end_coord=middle_end_coord,
            iteration_count=iteration_count + 1
        )

        beta_rooms = self._generate_cut(
            grid=grid,
            config=config,
            rng=rng,
            start_coord=middle_start_coord,
            end_coord=end_coord,
            iteration_count=iteration_count + 1
        )

        if config.do_connect_rooms:
            self._conjoin_rooms(
                grid=grid,
                config=config,
                alpha_rooms=alpha_rooms,
                beta_rooms=beta_rooms
            )

        return alpha_rooms + beta_rooms
    
    def _conjoin_rooms(
        self,
        grid: list[list[Tile]],
        config: BinarySpacePartitionConfig,
        alpha_rooms: list[Room],
        beta_rooms: list[Room]
    ) -> None:
        def rooms_overlap_x_range(
            room_a: Room,
            room_b: Room,
        ) -> bool:
            return max(room_a.x1, room_b.x1) <= min(room_a.x2, room_b.x2)
        
        def rooms_overlap_y_range(
            room_a: Room,
            room_b: Room,
        ) -> bool:
            return max(room_a.y1, room_b.y1) <= min(room_a.y2, room_b.y2)
        
        room_separation_distance = 2

        for alpha_room in alpha_rooms:
            for beta_room in beta_rooms:
                # [beta][alpha]
                if (beta_room.x2 - alpha_room.x1 == room_separation_distance):
                    if rooms_overlap_y_range(alpha_room, beta_room):
                        self._connect_rooms(
                            grid=grid,
                            config=config,
                            room_1=alpha_room,
                            room_2=beta_room,
                            side=self._SIDE_LEFT
                        )
                        return
                    
                # [beta]
                # [alpha]
                elif (beta_room.y2 - alpha_room.y1 == room_separation_distance):
                    if rooms_overlap_x_range(alpha_room, beta_room):
                        self._connect_rooms(
                            grid=grid,
                            config=config,
                            room_1=alpha_room,
                            room_2=beta_room,
                            side=self._SIDE_TOP
                        )
                        return
                    
                # [alpha][beta]
                elif (beta_room.x1 - alpha_room.x2 == room_separation_distance):
                    if rooms_overlap_y_range(alpha_room, beta_room):
                        self._connect_rooms(
                            grid=grid,
                            config=config,
                            room_1=alpha_room,
                            room_2=beta_room,
                            side=self._SIDE_RIGHT
                        )
                        return
                    
                # [alpha]
                # [beta]
                elif (beta_room.y1 - alpha_room.y2 == room_separation_distance):
                    if rooms_overlap_x_range(alpha_room, beta_room):
                        self._connect_rooms(
                            grid=grid,
                            config=config,
                            room_1=alpha_room,
                            room_2=beta_room,
                            side=self._SIDE_BOTTOM
                        )
                        return
                    
    def _connect_rooms(
        self,
        grid: list[list[Tile]],
        config: BinarySpacePartitionConfig,
        room_1: Room,
        room_2: Room,
        side: int
    ) -> None:
        if side == self._SIDE_LEFT:
            room_1_coord = (
                room_1.x1,
                (room_1.y1 + room_1.y2) // 2
            )

            room_2_coord = (
                room_2.x2,
                (room_2.y1 + room_2.y2) // 2
            )

        elif side == self._SIDE_TOP:
            room_1_coord = (
                (room_1.x1 + room_1.x2) // 2,
                room_1.y1
            )

            room_2_coord = (
                (room_2.x1 + room_2.x2) // 2,
                room_2.y2
            )

        elif side == self._SIDE_RIGHT:
            room_1_coord = (
                room_1.x2,
                (room_1.y1 + room_1.y2) // 2
            )

            room_2_coord = (
                room_2.x1,
                (room_2.y1 + room_2.y2) // 2
            )

        else:
            room_1_coord = (
                (room_1.x1 + room_1.x2) // 2,
                room_1.y2
            )

            room_2_coord = (
                (room_2.x1 + room_2.x2) // 2,
                room_2.y1
            )

        self._connect_points(
            grid=grid,
            config=config,
            start_coord=room_1_coord,
            end_coord=room_2_coord
        )
        
    def _generate_single_room(
        self,
        grid: list[list[Tile]],
        room: Room
    ) -> Room:
        x1 = room.x1 + 1
        y1 = room.y1 + 1
        x2 = room.x2 - 1
        y2 = room.y2 - 1

        start_x = x1
        start_y = y1
        end_x = x2
        end_y = y2

        for paint_x in range(start_x, end_x):
            for paint_y in range(start_y, end_y):
                grid[paint_y][paint_x] = Tile.AIR

        return Room(
            x1=start_x,
            y1=start_y,
            x2=end_x,
            y2=end_y
        )
    
    def _connect_points(
        self,
        grid: list[list[Tile]],
        config: BinarySpacePartitionConfig,
        start_coord: tuple[int, int],
        end_coord: tuple[int, int]
    ) -> None:
        x1, y1 = start_coord
        x2, y2 = end_coord

        self._draw_line(
            grid=grid,
            x1=x1,
            y1=y1,
            x2=x2,
            y2=y2,
            thickness=config.hallway_stroke_thickness
        )   

    def _draw_line(
        self,
        grid: list[list[Tile]],
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        thickness: int,
    ) -> None:
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        err = dx - dy

        while (x1 != x2) or (y1 != y2):
            self._paint_step(
                grid=grid,
                x=x1,
                y=y1,
                thickness=thickness
            )

            e2 = 2 * err

            if e2 > -dy:
                err -= dy
                x1 += sx

            if e2 < dx:
                err += dx
                y1 += sy

        self._paint_step(
            grid=grid,
            x=x2,
            y=y2,
            thickness=thickness
        )

    def _paint_step(
        self,
        grid: list[list[Tile]],
        x: int,
        y: int,
        thickness: int,
    ) -> None:
        height = len(grid)
        width = len(grid[0])

        negative_extent = (thickness - 1) // 2
        positive_extent = thickness // 2

        for paint_x in range(
            x - negative_extent,
            x + positive_extent + 1
        ):
            for paint_y in range(
                y - negative_extent,
                y + positive_extent + 1
            ):
                if (
                    0 <= paint_x < width and 0 <= paint_y < height
                ):
                    grid[paint_y][paint_x] = Tile.AIR
