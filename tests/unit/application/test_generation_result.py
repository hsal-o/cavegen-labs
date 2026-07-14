from dataclasses import dataclass

from cavegenlabs.application.generation_result import GenerationResult
from cavegenlabs.domain.models import CaveMap, Tile


@dataclass(frozen=True)
class ExampleConfig:
    width: int
    height: int

def test_stores_generation_date() -> None:
    config = ExampleConfig(
        width=2,
        height=2
    )

    cave_map = CaveMap(
        width=2,
        height=2,
        cells=(
            (Tile.SOLID, Tile.AIR),
            (Tile.AIR, Tile.SOLID)
        )
    )

    result = GenerationResult(
        algorithm_id="example",
        algorithm_name="Example",
        config=config,
        seed=123,
        cave_map=cave_map,
        duration_seconds=0.01
    )

    assert result.algorithm_id == "example"
    assert result.algorithm_name == "Example"
    assert result.config is config
    assert result.seed == 123
    assert result.cave_map is cave_map
    assert result.duration_seconds == 0.01