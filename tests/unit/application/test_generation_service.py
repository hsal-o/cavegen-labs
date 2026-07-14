from collections.abc import Mapping
from dataclasses import dataclass
from random import Random
from typing import Any

import pytest

from cavegenlabs.application import AlgorithmRegistry
from cavegenlabs.application.generation_service import GenerationService
from cavegenlabs.domain.generation import AlgorithmDefinition
from cavegenlabs.domain.models import CaveMap, Tile

pytestmark = pytest.mark.skip(reason="AlgorithmDefinition is being redesigned")

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
        tile = Tile.AIR if rng.random() < 1.0 else Tile.SOLID

        cells = tuple(
            tuple(tile for _ in range(config.width))
            for _ in range(config.height)
        )

        return CaveMap(
            width=config.width,
            height=config.height,
            cells=cells
        )
    
def create_example_config(
    values: Mapping[str, Any],
) -> ExampleConfig:
    return ExampleConfig(
        width=int(values["width"]),
        height=int(values["height"]),
    )

def create_definition() -> AlgorithmDefinition[ExampleConfig]:
    return AlgorithmDefinition(
        algorithm_id="example",
        display_name="Example",
        description="Example algorithm.",
        parameters=(),
        config_factory=create_example_config,
        generator=ExampleGenerator(),
    )

def test_generates_cave_and_returns_result() -> None:
    definition = create_definition()
    registry = AlgorithmRegistry((definition,))
    service = GenerationService(registry)

    config = ExampleConfig(
        width=2,
        height=2,
    )

    result = service.generate(
        algorithm_id="example",
        config=config,
        seed=123,
    )

    assert result.algorithm_id == "example"
    assert result.algorithm_name == "Example"
    assert result.config is config
    assert result.seed == 123
    assert result.cave_map.width == 2
    assert result.cave_map.height == 2
    assert result.duration_seconds >= 0.0

def test_same_seed_produces_same_map() -> None:
    definition = create_definition()
    registry = AlgorithmRegistry((definition,))
    service = GenerationService(registry)

    config = ExampleConfig(
        width=2,
        height=2,
    )

    first = service.generate(
        algorithm_id="example",
        config=config,
        seed=12345,
    )

    second = service.generate(
        algorithm_id="example",
        config=config,
        seed=12345,
    )

    assert first.cave_map == second.cave_map