from dataclasses import dataclass
from enum import Enum
from typing import Any

class ParameterValueType(Enum):
    INTEGER = "integer"
    DECIMAL = "decimal"
    BOOLEAN = "boolean"
    CHOICE = "choice"

@dataclass(frozen=True)
class ParameterDefinition:
    key: str
    label: str
    parameter_type: ParameterValueType
    default: Any
    minimum: int | float | None = None
    maximum: int | float | None = None
    choices: tuple[Any, ...] = ()
    description: str | None = None
    required: bool = True

    def __post_init__(self) -> None:
        if not self.key:
            raise ValueError("Parameter key can not be empty.")
        
        if not self.label:
            raise ValueError("Parameter label can not be empty.")
        
        if self.minimum is not None and self.maximum is not None:
            if self.minimum > self.maximum:
                raise ValueError("Parameter minimum can not be greater than maximum.")
            
        if self.parameter_type is ParameterValueType.CHOICE and not self.choices:
            raise ValueError("Choice parameters must define at least one choice.")