import tkinter as tk

from cavegenlabs.application import AlgorithmRegistry
from cavegenlabs.presentation.generation_view_model import (
    GenerationViewModel,
)
from cavegenlabs.presentation.main_window import MainWindow


def main() -> None:
    root = tk.Tk()

    registry = AlgorithmRegistry(())

    view_model = GenerationViewModel(
        registry=registry,
    )

    MainWindow(
        root=root,
        view_model=view_model,
    )

    root.mainloop()