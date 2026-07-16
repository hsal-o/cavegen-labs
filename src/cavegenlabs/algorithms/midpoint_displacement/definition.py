from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.midpoint_displacement.config import MidpointDisplacementConfig
from cavegenlabs.algorithms.midpoint_displacement.generator import MidpointDisplacementGenerator
from cavegenlabs.domain.generation.algorithm_definition import AlgorithmDefinition
from cavegenlabs.domain.models.grid_position import GridPosition
from cavegenlabs.algorithms.midpoint_displacement.presentation import create_inputs


def create_config(
    values: Mapping[str, Any]
) -> MidpointDisplacementConfig:
    return MidpointDisplacementConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        start_position=GridPosition(values["start_position"]),
        end_position=GridPosition(values["end_position"]),
        iteration_count=int(values["iteration_count"]),
        magnitude=int(values["magnitude"]),
        thickness=int(values["thickness"]),
        thickness_variation=tuple(values["thickness_variation"])
    )


MIDPOINT_DISPLACEMENT_DEFINITION = AlgorithmDefinition(
    algorithm_id="midpoint_displacement",
    display_name="Midpoint Displacement",
    description="Generates cave passages using recursive midpoint displacement.",
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=MidpointDisplacementGenerator()
)