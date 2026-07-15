from tkinter import StringVar, ttk
from tkinter.ttk import Frame

from cavegenlabs.domain.models.grid_position import GridPosition
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class PositionInput(ParameterInput):
    def __init__(
        self,
        key: str,
        label: str,
        default: GridPosition,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
        )

        self._default = default
        self._variable = StringVar(value=default.value)

        self._label_widget: ttk.Label | None = None
        self._combobox: ttk.Combobox | None = None

    def render(
        self,
        parent: Frame,
        row: int,
    ) -> None:
        self._label_widget = ttk.Label(
            parent,
            text=self.label,
        )
        self._label_widget.grid(
            row=row,
            column=0,
            sticky="w",
            padx=5,
            pady=2,
        )

        self._combobox = ttk.Combobox(
            parent,
            textvariable=self._variable,
            values=tuple(position.value for position in GridPosition),
            state="readonly",
        )
        self._combobox.grid(
            row=row,
            column=1,
            sticky="ew",
            padx=5,
            pady=2,
        )

    def get_value(self) -> GridPosition:
        return GridPosition(self._variable.get())

    def set_value(
        self,
        value: GridPosition,
    ) -> None:
        self._variable.set(value.value)

    def reset(self) -> None:
        self._variable.set(self._default.value)

    def focus(self) -> None:
        if self._combobox is not None:
            self._combobox.focus_set()