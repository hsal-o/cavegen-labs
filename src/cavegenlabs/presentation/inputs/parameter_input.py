from abc import ABC, abstractmethod
from typing import Any 
from tkinter.ttk import Frame


class ParameterInput(ABC):

    @property
    @abstractmethod
    def parameter_key(self) -> str:
        ...

    @abstractmethod
    def render(self, parent: Frame, row: int) -> None:
        ...

    @abstractmethod
    def get_value(self) -> Any:
        ...

    @abstractmethod
    def set_value(self, value: Any) -> None:
        ...

    @abstractmethod
    def reset(self) -> None:
        ...

    @abstractmethod
    def focus(self) -> None:
        ...