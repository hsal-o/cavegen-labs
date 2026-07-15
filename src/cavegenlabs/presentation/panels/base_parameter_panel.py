from tkinter import StringVar, ttk


class BaseParameterPanel(ttk.LabelFrame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(
            parent,
            text="Base Settings",
            padding=10,
        )

        self.columnconfigure(1, weight=1)

        self._width = StringVar(value="64")
        self._height = StringVar(value="64")
        self._seed = StringVar(value="")

        ttk.Label(
            self,
            text="Width",
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 5),
            pady=2,
        )

        ttk.Entry(
            self,
            textvariable=self._width,
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            pady=2,
        )

        ttk.Label(
            self,
            text="Height",
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 5),
            pady=2,
        )

        ttk.Entry(
            self,
            textvariable=self._height,
        ).grid(
            row=1,
            column=1,
            sticky="ew",
            pady=2,
        )

        ttk.Label(
            self,
            text="Seed",
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(0, 5),
            pady=2,
        )

        ttk.Entry(
            self,
            textvariable=self._seed,
        ).grid(
            row=2,
            column=1,
            sticky="ew",
            pady=2,
        )

    def get_width(self) -> int:
        return int(self._width.get())

    def get_height(self) -> int:
        return int(self._height.get())

    def get_seed(self) -> int | None:
        value = self._seed.get().strip()

        if not value:
            return None

        return int(value)