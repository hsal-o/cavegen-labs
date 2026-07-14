from abc import ABC, abstractmethod
from typing import Any 


class ParameterInput(ABC):

    @property
    @abstractmethod
    def key(self) -> str:
        ...

    @abstractmethod
    def get_value(self) -> Any:
        ...

    @abstractmethod
    def set_value(self, value: Any) -> None:
        ...

    @abstractmethod
    def validate(self) -> bool:
        ...

    @abstractmethod
    def reset(self) -> None:
        ...

    @abstractmethod
    def focus(self) -> None:
        ...

    @abstractmethod
    def show_error(self, message: str) -> None:
        ...

    @abstractmethod
    def clear_error(self) -> None:
        ...