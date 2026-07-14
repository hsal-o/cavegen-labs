from tkinter import ttk


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
        self.rowconfigure(0, weight=1)

        self._input_frame = ttk.Frame(self)
        self._input_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self._empty_label = ttk.Label(
            self._input_frame,
            text="Select an algorithm to view its parameters.",
            wraplength=220,
        )
        self._empty_label.grid(
            row=0,
            column=0,
            sticky="nw",
        )

        self._generate_button = ttk.Button(
            self,
            text="Generate",
            state="disabled",
        )
        self._generate_button.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(10, 0),
        )