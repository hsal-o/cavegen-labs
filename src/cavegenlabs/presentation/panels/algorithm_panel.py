import tkinter as tk
from collections.abc import Callable
from tkinter import ttk

from cavegenlabs.domain.generation import AlgorithmDefinition


class AlgorithmPanel(ttk.LabelFrame):
    def __init__(
        self,
        parent: ttk.Widget,
    ) -> None:
        super().__init__(
            parent,
            text="Algorithms",
            padding=10,
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self._definitions: tuple[AlgorithmDefinition[object], ...] = ()
        self._selection_callback: Callable[[str], None] | None = None

        self._listbox = tk.Listbox(
            self,
            exportselection=False,
        )
        self._listbox.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self._scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self._listbox.yview,
        )
        self._scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        self._listbox.configure(
            yscrollcommand=self._scrollbar.set,
        )

        self._listbox.bind(
            "<<ListboxSelect>>",
            self._on_selection_changed,
        )

    def set_algorithms(
        self,
        definitions: tuple[AlgorithmDefinition[object], ...],
    ) -> None:
        self._definitions = definitions
        self._listbox.delete(0, tk.END)

        if not definitions:
            self._listbox.insert(
                tk.END,
                "No algorithms available.",
            )
            self._listbox.configure(state="disabled")
            return

        self._listbox.configure(state="normal")

        for definition in definitions:
            self._listbox.insert(
                tk.END,
                definition.display_name,
            )

    def set_selection_callback(
        self,
        callback: Callable[[str], None],
    ) -> None:
        self._selection_callback = callback

    def _on_selection_changed(
        self,
        event: tk.Event[tk.Misc],
    ) -> None:
        del event

        selection = self._listbox.curselection()

        if not selection or not self._definitions:
            return

        selected_index = selection[0]
        definition = self._definitions[selected_index]

        if self._selection_callback is not None:
            self._selection_callback(definition.algorithm_id)