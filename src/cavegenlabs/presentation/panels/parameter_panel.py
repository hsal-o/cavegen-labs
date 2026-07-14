from tkinter import ttk

from cavegenlabs.presentation.inputs.parameter_input import ParameterInput
from cavegenlabs.presentation.panels.algorithm_parameter_panel import AlgorithmParameterPanel
from cavegenlabs.presentation.panels.base_parameter_panel import BaseParameterPanel


class ParameterPanel(ttk.LabelFrame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(
            parent,
            text="Parameters",
            padding=10,
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._base_panel = BaseParameterPanel(self)
        self._base_panel.grid(
            row=0,
            column=0,
            sticky="ew",
        )

        self._algorithm_panel = AlgorithmParameterPanel(self)
        self._algorithm_panel.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=(10, 0),
        )

        self._generate_button = ttk.Button(
            self,
            text="Generate",
            state="disabled",
        )
        self._generate_button.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(10, 0),
        )

    def get_base_values(self) -> dict[str, int | None]:
        return {
            "width": self._base_panel.get_width(),
            "height": self._base_panel.get_height(),
            "seed": self._base_panel.get_seed(),
        }

    def get_algorithm_values(self) -> dict[str, object]:
        return self._algorithm_panel.get_values()

    def set_algorithm_inputs(
        self,
        inputs: tuple[ParameterInput, ...],
    ) -> None:
        self._algorithm_panel.set_inputs(inputs)
        self._generate_button.configure(state="normal")

    def set_generate_callback(
        self,
        callback: Callable[[], None],
    ) -> None:
        self._generate_button.configure(command=callback)

    def disable_generate(self) -> None:
        self._generate_button.configure(state="disabled")