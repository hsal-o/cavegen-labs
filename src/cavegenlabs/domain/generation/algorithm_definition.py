from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from cavegenlabs.domain.generation.generator import CaveGenerator
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


ConfigT = TypeVar("ConfigT")

ConfigFactory = Callable[[Mapping[str, Any]], ConfigT]


@dataclass(frozen=True)
class AlgorithmDefinition(Generic[ConfigT]):
    algorithm_id: str
    display_name: str
    description: str 
    create_inputs: Callable[[], tuple[ParameterInput, ...]]
    config_factory: ConfigFactory[ConfigT]
    generator: CaveGenerator[ConfigT]

    def __post_init__(self) -> None:
        if not self.algorithm_id:
            raise ValueError("Algorithm ID can not be empty.")
        
        if not self.display_name:
            raise ValueError("Algorithm display name can not be empty.")
        
        parameter_keys = [parameter.key for parameter in self.parameters]
        if len(self.parameters) != len(set(parameter_keys)):
            raise ValueError("Algorithm parameter keys must be unique.")