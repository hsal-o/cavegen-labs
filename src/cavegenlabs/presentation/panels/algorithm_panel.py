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