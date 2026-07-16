from tkinter import StringVar, ttk

from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class DecimalPairParameterInput(ParameterInput):
    def __init__(
        self,
        key: str,
        label: str,
        default: tuple[float, float]
    ) -> None:
        super().__init__(
            key=key,
            label=label
        )
        self._default = default

        self._left_variable  = StringVar(value=str(default[0]))
        self._right_variable = StringVar(value=str(default[1]))

        self._label_widget: ttk.Label | None = None
        self._left_entry: ttk.Entry | None = None
        self._right_entry: ttk.Entry | None = None

    def render(
        self,
        parent: ttk.Frame,
        row: int
    ) -> None:
        self._label_widget = ttk.Label(
            parent,
            text=self.label
        )

        container = ttk.Frame(parent)

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        self._left_entry = ttk.Entry(
            container,
            textvariable=self._left_variable,
            width=10,
        )

        self._right_entry = ttk.Entry(
            container,
            textvariable=self._right_variable,
            width=10,
        )

        self._label_widget.grid(
            row=row,
            column=0,
            sticky="w",
            padx=5,
            pady=2,
        )

        container.grid(
            row=row,
            column=1,
            sticky="ew",
            padx=5,
            pady=2,
        )

        self._left_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 2),
        )

        self._right_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(2, 0),
        )

    def get_value(self) -> tuple[float, float]:
        return (
            float(self._left_variable.get()),
            float(self._right_variable.get()),
        )
    
    def set_value(
        self,
        value: tuple[float, float],
    ) -> None:
        self._left_variable.set(str(value[0]))
        self._right_variable.set(str(value[1]))

    def reset(self) -> None:
        self.set_value(self._default)

    def focus(self) -> None:
        if self._left_entry is not None:
            self._left_entry.focus_set()