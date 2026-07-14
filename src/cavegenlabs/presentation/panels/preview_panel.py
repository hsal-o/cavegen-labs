from tkinter import Canvas, ttk

from cavegenlabs.domain.models import CaveMap, Tile


class PreviewPanel(ttk.LabelFrame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(
            parent,
            text="Preview",
            padding=10,
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self._cave_map: CaveMap | None = None

        self._canvas = Canvas(
            self,
            background="white",
            highlightthickness=0,
        )
        self._canvas.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self._canvas.bind(
            "<Configure>",
            self._on_canvas_resized,
        )

    def display(
        self,
        cave_map: CaveMap,
    ) -> None:
        self._cave_map = cave_map
        self._draw_cave_map()

    def clear(self) -> None:
        self._cave_map = None
        self._draw_placeholder()

    def _on_canvas_resized(
        self,
        event: object,
    ) -> None:
        del event

        if self._cave_map is None:
            self._draw_placeholder()
        else:
            self._draw_cave_map()

    def _draw_placeholder(self) -> None:
        self._canvas.delete("all")

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        self._canvas.create_text(
            width / 2,
            height / 2,
            text="Generated cave preview will appear here.",
            fill="#666666",
        )

    def _draw_cave_map(self) -> None:
        if self._cave_map is None:
            self._draw_placeholder()
            return

        self._canvas.delete("all")

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        tile_size = min(
            canvas_width / self._cave_map.width,
            canvas_height / self._cave_map.height,
        )

        rendered_width = tile_size * self._cave_map.width
        rendered_height = tile_size * self._cave_map.height

        x_offset = (canvas_width - rendered_width) / 2
        y_offset = (canvas_height - rendered_height) / 2

        for y in range(self._cave_map.height):
            for x in range(self._cave_map.width):
                tile = self._cave_map.get_tile(x, y)

                fill = "black" if tile is Tile.SOLID else "white"

                x1 = x_offset + x * tile_size
                y1 = y_offset + y * tile_size
                x2 = x1 + tile_size
                y2 = y1 + tile_size

                self._canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=fill,
                    outline="",
                )