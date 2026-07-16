from tkinter import BooleanVar, ttk

from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class BooleanParameterInput(ParameterInput):
    def __init__(
        self,
        key: str,
        label: str,
        default: bool,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
        )

        self._default = default
        self._variable = BooleanVar(value=default)

        self._label_widget: ttk.Label | None = None
        self._checkbox: ttk.Checkbutton | None = None

    def render(
        self,
        parent: ttk.Frame,
        row: int,
    ) -> None:
        self._label_widget = ttk.Label(
            parent,
            text=self.label,
        )

        self._checkbox = ttk.Checkbutton(
            parent,
            variable=self._variable,
        )

        self._label_widget.grid(
            row=row,
            column=0,
            sticky="w",
            padx=5,
            pady=2,
        )

        self._checkbox.grid(
            row=row,
            column=1,
            sticky="w",
            padx=5,
            pady=2,
        )

    def get_value(self) -> bool:
        return self._variable.get()

    def set_value(
        self,
        value: bool,
    ) -> None:
        self._variable.set(value)

    def reset(self) -> None:
        self._variable.set(self._default)

    def focus(self) -> None:
        if self._checkbox is not None:
            self._checkbox.focus_set()