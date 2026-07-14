from tkinter import Canvas, ttk


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
            self._draw_placeholder,
        )

    def _draw_placeholder(
        self,
        event: object,
    ) -> None:
        del event

        self._canvas.delete("placeholder")

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        self._canvas.create_text(
            width / 2,
            height / 2,
            text="Generated cave preview will appear here.",
            fill="#666666",
            tags="placeholder",
        )