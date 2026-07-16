from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.random_walk.config import RandomWalkConfig
from cavegenlabs.algorithms.random_walk.generator import RandomWalkGenerator
from cavegenlabs.domain.models.grid_position import GridPosition
from cavegenlabs.algorithms.random_walk.presentation import create_inputs
from cavegenlabs.domain.generation import AlgorithmDefinition


def create_config(
    values: Mapping[str, Any],
) -> RandomWalkConfig:
    return RandomWalkConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        walker_count=int(values["walker_count"]),
        step_count=int(values["step_count"]),
        thickness=int(values["thickness"]),
        bias=float(values["bias"]),
        start_position=GridPosition(values["start_position"]),
        end_position=GridPosition(values["end_position"]),
    )


RANDOM_WALK_DEFINITION = AlgorithmDefinition(
    algorithm_id="random_walk",
    display_name="Random Walk",
    description=(
        "Carves paths through a solid grid using one or more randomly moving walkers."
    ),
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=RandomWalkGenerator(),
)