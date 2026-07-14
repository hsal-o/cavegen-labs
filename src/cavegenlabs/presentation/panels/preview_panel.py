from tkinter import ttk


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