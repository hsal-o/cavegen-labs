from tkinter import StringVar, ttk


class StatusPanel(ttk.Frame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(parent)

        self._status = StringVar(value="Status: Ready")

        self._label = ttk.Label(
            self,
            textvariable=self._status,
        )
        self._label.pack(
            anchor="w",
            padx=5,
            pady=2,
        )

    def set_status(
        self,
        message: str,
    ) -> None:
        self._status.set(f"Status: {message}")