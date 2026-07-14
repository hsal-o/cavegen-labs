import tkinter as tk

from cavegenlabs.presentation.main_window import MainWindow


def main() -> None:
    root = tk.Tk()

    MainWindow(root)

    root.mainloop()