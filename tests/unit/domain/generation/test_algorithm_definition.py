from collections.abc import Mapping
from dataclasses import dataclass
from random import Random
from typing import Any

import pytest

from cavegenlabs.domain.generation import AlgorithmDefinition, ParameterDefinition, ParameterValueType
from cavegenlabs.domain.models import CaveMap, Tile

@dataclass(frozen=True)
class ExampleConfig:
    width: int
    height: int

class ExampleGenerator:
    def generate(
            self,
            config: ExampleConfig,
            rng: Random
    ) -> CaveMap:
        del rng
        
        cells = tuple(
            tuple(Tile.SOLID for _ in range(config.width))
            for _ in range(config.height)
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=cells
        )
    
def create_example_config(
        values: Mapping[str, Any]
) -> ExampleConfig:
    return ExampleConfig(
        width=int(values["width"]),
        height=int(values["height"])
    )

def test_creates_valid_algorithm_definition() -> None:
    parameters = (
        ParameterDefinition(
            key="width",
            label="Width",
            parameter_type=ParameterValueType.INTEGER,
            default=80
        ),
        ParameterDefinition(
            key="height",
            label="Height",
            parameter_type=ParameterValueType.INTEGER,
            default=60
        ),
    )

    definition = AlgorithmDefinition(
        algorithm_id="example",
        display_name="Example",
        description="Example algorithm.",
        parameters=parameters,
        config_factory=create_example_config,
        generator=ExampleGenerator()
    )

    assert definition.algorithm_id == "example"
    assert definition.display_name == "Example"
    assert definition.parameters == parameters


def test_rejects_empty_algorithm_id() -> None:
    with pytest.raises(ValueError, match="Algorithm ID can not be empty"):
        AlgorithmDefinition(
            algorithm_id="",
            display_name="Example",
            description="Example algorithm.",
            parameters=(),
            config_factory=create_example_config,
            generator=ExampleGenerator(),
        )


def test_rejects_empty_display_name() -> None:
    with pytest.raises(ValueError, match="Algorithm display name can not be empty"):
        AlgorithmDefinition(
            algorithm_id="example",
            display_name="",
            description="Example algorithm.",
            parameters=(),
            config_factory=create_example_config,
            generator=ExampleGenerator(),
        )


def test_rejects_duplicate_parameter_keys() -> None:
    parameters = (
        ParameterDefinition(
            key="width",
            label="Width",
            parameter_type=ParameterValueType.INTEGER,
            default=80,
        ),
        ParameterDefinition(
            key="width",
            label="Other Width",
            parameter_type=ParameterValueType.INTEGER,
            default=100,
        ),
    )

    with pytest.raises(ValueError, match="Algorithm parameter keys must be unique"):
        AlgorithmDefinition(
            algorithm_id="example",
            display_name="Example",
            description="Example algorithm.",
            parameters=parameters,
            config_factory=create_example_config,
            generator=ExampleGenerator(),
        )