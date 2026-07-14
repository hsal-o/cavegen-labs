from tkinter import ttk

from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class AlgorithmParameterPanel(ttk.LabelFrame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(
            parent,
            text="Algorithm Settings",
            padding=10,
        )

        self.columnconfigure(0, weight=1)

        self._inputs: tuple[ParameterInput, ...] = ()

        self._empty_label = ttk.Label(
            self,
            text="Select an algorithm to view its settings.",
            wraplength=220,
        )
        self._empty_label.grid(
            row=0,
            column=0,
            sticky="nw",
        )

    def set_inputs(
        self,
        inputs: tuple[ParameterInput, ...],
    ) -> None:
        self.clear()

        self._inputs = inputs

        if not inputs:
            self._show_empty_message(
                "This algorithm has no additional settings."
            )
            return

        for row, parameter_input in enumerate(inputs):
            parameter_input.render(
                parent=self,
                row=row,
            )

    def get_values(self) -> dict[str, object]:
        return {
            parameter_input.key: parameter_input.get_value()
            for parameter_input in self._inputs
        }

    def reset(self) -> None:
        for parameter_input in self._inputs:
            parameter_input.reset()

    def focus_first_input(self) -> None:
        if self._inputs:
            self._inputs[0].focus()

    def clear(self) -> None:
        for child in self.winfo_children():
            child.destroy()

        self._inputs = ()

    def show_no_selection(self) -> None:
        self.clear()

        self._show_empty_message(
            "Select an algorithm to view its settings."
        )

    def _show_empty_message(
        self,
        message: str,
    ) -> None:
        self._empty_label = ttk.Label(
            self,
            text=message,
            wraplength=220,
        )
        self._empty_label.grid(
            row=0,
            column=0,
            sticky="nw",
        )