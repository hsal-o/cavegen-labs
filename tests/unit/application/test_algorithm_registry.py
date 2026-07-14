from collections.abc import Mapping
from dataclasses import dataclass
from random import Random
from typing import Any

import pytest 

from cavegenlabs.application.algorithm_registry import AlgorithmRegistry
from cavegenlabs.domain.generation import AlgorithmDefinition
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


def create_definition(
        algorithm_id: str
) -> AlgorithmDefinition[ExampleConfig]:
    return AlgorithmDefinition(
        algorithm_id=algorithm_id,
        display_name=algorithm_id.title(),
        description="Example algorithm",
        parameters=(),
        config_factory=create_example_config,
        generator=ExampleGenerator()
    )


def test_get_returns_matching_definition() -> None:
    definition = create_definition("example")
    registry = AlgorithmRegistry((definition,))

    result = registry.get("example")

    assert result is definition


def test_get_all_returns_all_definitions() -> None:
    first = create_definition("first")
    second = create_definition("second")

    registry = AlgorithmRegistry((first, second))

    assert registry.get_all() == (first, second)


def test_rejects_duplicate_algorithm_ids() -> None:
    first = create_definition("duplicate")
    second = create_definition("duplicate")

    with pytest.raises(ValueError, match="Algorithm IDs must be unique"):
        AlgorithmRegistry((first, second))


def test_get_rejects_unknown_algorithm_id() -> None:
    registry = AlgorithmRegistry(())

    with pytest.raises(KeyError, match="Unknown algorithm ID: missing"):
        registry.get("missing")