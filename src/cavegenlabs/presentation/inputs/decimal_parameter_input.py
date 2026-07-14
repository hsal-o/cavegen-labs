from tkinter import StringVar, ttk
from tkinter.ttk import Frame

from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class DecimalParameterInput(ParameterInput):
    def __init__(
        self,
        key: str,
        label: str,
        default: float,
        minimum: float | None = None,
        maximum: float | None = None,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
        )

        self._default = default
        self._minimum = minimum
        self._maximum = maximum

        self._variable: StringVar = StringVar(
            value=str(default),
        )

        self._label_widget: ttk.Label | None = None
        self._entry: ttk.Entry | None = None

    def render(
        self,
        parent: Frame,
        row: int,
    ) -> None:
        self._label_widget = ttk.Label(
            parent,
            text=self.label,
        )

        self._entry = ttk.Entry(
            parent,
            textvariable=self._variable,
        )

        self._label_widget.grid(
            row=row,
            column=0,
            sticky="w",
            padx=5,
            pady=2,
        )

        self._entry.grid(
            row=row,
            column=1,
            sticky="ew",
            padx=5,
            pady=2,
        )

    def get_value(self) -> float:
        return float(self._variable.get())

    def set_value(
        self,
        value: float,
    ) -> None:
        self._variable.set(str(value))

    def reset(self) -> None:
        self._variable.set(str(self._default))

    def focus(self) -> None:
        if self._entry is not None:
            self._entry.focus_set()