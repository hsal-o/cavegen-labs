import tkinter as tk

from cavegenlabs.algorithms.cellular_automata.definition import CELLULAR_AUTOMATA_DEFINITION
from cavegenlabs.algorithms.midpoint_displacement.definition import MIDPOINT_DISPLACEMENT_DEFINITION
from cavegenlabs.algorithms.random_walk.definition import RANDOM_WALK_DEFINITION
from cavegenlabs.application import (
    AlgorithmRegistry,
    GenerationService,
)
from cavegenlabs.presentation.generation_view_model import (
    GenerationViewModel,
)
from cavegenlabs.presentation.main_window import MainWindow


def main() -> None:
    root = tk.Tk()

    registry = AlgorithmRegistry(
        (
            RANDOM_WALK_DEFINITION,
            MIDPOINT_DISPLACEMENT_DEFINITION,
            CELLULAR_AUTOMATA_DEFINITION
        )
    )

    generation_service = GenerationService(
        registry=registry,
    )

    view_model = GenerationViewModel(
        registry=registry,
        generation_service=generation_service
    )

    MainWindow(
        root=root,
        view_model=view_model,
    )

    root.mainloop()