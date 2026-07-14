from tkinter import ttk


class StatusPanel(ttk.Frame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(parent)

        self._label = ttk.Label(
            self,
            text="Status: Ready",
        )

        self._label.pack(
            anchor="w",
            padx=5,
            pady=2,
        )