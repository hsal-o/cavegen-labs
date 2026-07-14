from tkinter import StringVar, ttk
from tkinter.ttk import Frame

from cavegenlabs.domain.generation import ParameterDefinition
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class IntegerParameterInput(ParameterInput):
    def __init__(
        self,
        definition: ParameterDefinition,
    ) -> None:
        self._definition = definition

        self._variable: StringVar = StringVar(
            value=str(definition.default)
        )

        self._label: ttk.Label | None = None
        self._entry: ttk.Entry | None = None

    @property
    def key(self) -> str:
        return self._definition.key

    def render(
        self,
        parent: Frame,
        row: int,
    ) -> None:
        self._label = ttk.Label(
            parent,
            text=self._definition.label,
        )

        self._entry = ttk.Entry(
            parent,
            textvariable=self._variable,
        )

        self._label.grid(
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

    def get_value(self) -> int:
        return int(self._variable.get())

    def set_value(
        self,
        value: int,
    ) -> None:
        self._variable.set(str(value))

    def reset(self) -> None:
        self._variable.set(
            str(self._definition.default)
        )

    def focus(self) -> None:
        if self._entry is not None:
            self._entry.focus_set()
