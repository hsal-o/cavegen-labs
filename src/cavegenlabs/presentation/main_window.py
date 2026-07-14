from tkinter import Tk, ttk


class MainWindow:
    def __init__(self, root: Tk) -> None:
        self._root = root

        self._configure_window()

        self._main_frame = ttk.Frame(
            self._root,
            padding=10,
        )

        self._main_frame.pack(
            fill="both",
            expand=True,
        )

    def _configure_window(self) -> None:
        self._root.title("CaveGen Labs")

        self._root.geometry("1200x800")

        self._root.minsize(
            width=900,
            height=600,
        )