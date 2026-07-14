from abc import ABC, abstractmethod
from typing import Any 
from tkinter.ttk import Frame


class ParameterInput(ABC):
    def __init__(
        self,
        key: str,
        label: str,
    ) -> None:
        self._key = key
        self._label = label

    @property
    def key(self) -> str:
        return self._key

    @property
    def label(self) -> str:
        return self._label

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