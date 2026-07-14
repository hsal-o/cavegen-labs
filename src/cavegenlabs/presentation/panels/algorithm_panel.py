from tkinter import ttk


class AlgorithmPanel(ttk.LabelFrame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(
            parent,
            text="Algorithms",
            padding=10,
        )

        self.columnconfigure(0, weight=1)

        self._empty_label = ttk.Label(
            self,
            text="No algorithms available.",
        )
        self._empty_label.grid(
            row=0,
            column=0,
            sticky="nw",
        )