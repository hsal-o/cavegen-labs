from tkinter import Tk, ttk
from cavegenlabs.presentation.panels import AlgorithmPanel, ParameterPanel, PreviewPanel, StatusPanel


class MainWindow:
    def __init__(
        self,
        root: Tk,
    ) -> None:
        self._root = root

        self._configure_window()

        self._main_frame = ttk.Frame(
            self._root,
            padding=10,
        )
        self._main_frame.pack(
            fill="both",
            expand=True,
        )

        self._configure_layout()
        self._create_panels()

    def _configure_window(self) -> None:
        self._root.title("CaveGenLabs")
        self._root.geometry("1200x800")
        self._root.minsize(
            width=900,
            height=600,
        )

    def _configure_layout(self) -> None:
        self._main_frame.columnconfigure(
            index=0,
            weight=1,
            minsize=180,
        )
        self._main_frame.columnconfigure(
            index=1,
            weight=1,
            minsize=250,
        )
        self._main_frame.columnconfigure(
            index=2,
            weight=3,
            minsize=400,
        )

        self._main_frame.rowconfigure(
            index=0,
            weight=1,
        )
        self._main_frame.rowconfigure(
            index=1,
            weight=0,
        )

    def _create_panels(self) -> None:
        self._algorithm_panel = AlgorithmPanel(
            self._main_frame,
        )
        self._algorithm_panel.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 5),
        )

        self._parameter_panel = ParameterPanel(
            self._main_frame,
        )
        self._parameter_panel.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=5,
        )

        self._preview_panel = PreviewPanel(
            self._main_frame,
        )
        self._preview_panel.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(5, 0),
        )

        self._status_panel = StatusPanel(
            self._main_frame,
        )
        self._status_panel.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="ew",
            pady=(10, 0),
        )