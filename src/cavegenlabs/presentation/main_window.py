from tkinter import Menu, Tk, ttk

from cavegenlabs.presentation.generation_view_model import (
    GenerationViewModel,
)
from cavegenlabs.presentation.panels import (
    AlgorithmPanel,
    ParameterPanel,
    PreviewPanel,
    StatusPanel,
)


class MainWindow:
    def __init__(
        self,
        root: Tk,
        view_model: GenerationViewModel,
    ) -> None:
        self._root = root
        self._view_model = view_model

        self._configure_window()
        self._create_menu()

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
        self._bind_events()
        self._load_algorithms()

    def _configure_window(self) -> None:
        self._root.title("CaveGenLabs")
        self._root.geometry("1200x650")
        self._root.minsize(
            width=900,
            height=600,
        )

    def _create_menu(self) -> None:
        menu_bar = Menu(self._root)

        file_menu = Menu(
            menu_bar,
            tearoff=False,
        )
        file_menu.add_command(
            label="Exit",
            command=self._root.destroy,
        )
        menu_bar.add_cascade(
            label="File",
            menu=file_menu,
        )

        help_menu = Menu(
            menu_bar,
            tearoff=False,
        )
        help_menu.add_command(
            label="About CaveGenLabs",
        )
        menu_bar.add_cascade(
            label="Help",
            menu=help_menu,
        )

        self._root.configure(menu=menu_bar)

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
            weight=1,
            minsize=250,
        )

        self._main_frame.rowconfigure(
            index=0,
            weight=1,
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

    def _bind_events(self) -> None:
        self._algorithm_panel.set_selection_callback(
            self._on_algorithm_selected,
        )

        self._parameter_panel.set_generate_callback(
            self._on_generate_clicked,
        )

    def _load_algorithms(self) -> None:
        definitions = self._view_model.get_algorithms()
        self._algorithm_panel.set_algorithms(definitions)

        if not definitions:
            self._parameter_panel.disable_generate()

    def _on_algorithm_selected(
        self,
        algorithm_id: str,
    ) -> None:
        inputs = self._view_model.select_algorithm(
            algorithm_id,
        )

        self._parameter_panel.set_algorithm_inputs(inputs)
        self._status_panel.set_status(
            f"Selected algorithm: {algorithm_id}"
        )

    def _on_generate_clicked(self) -> None:
        try:
            result = self._view_model.generate(
                base_values=self._parameter_panel.get_base_values(),
                algorithm_values=(
                    self._parameter_panel.get_algorithm_values()
                ),
            )
        except (ValueError, TypeError) as error:
            self._status_panel.set_status(str(error))
            return

        self._preview_panel.display(result.cave_map)

        self._status_panel.set_status(
            f"Generated {result.algorithm_name} "
            f"with seed {result.seed} "
            f"in {result.duration_seconds:.4f} seconds."
        )