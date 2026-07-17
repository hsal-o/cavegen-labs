from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.diffusion_limited_aggregation.generator import DiffusionLimitedAggregationGenerator
from cavegenlabs.algorithms.diffusion_limited_aggregation.presentation import create_inputs
from cavegenlabs.algorithms.diffusion_limited_aggregation.config import DiffusionLimitedAggregationConfig
from cavegenlabs.domain.generation.algorithm_definition import AlgorithmDefinition


def create_config(
    values: Mapping[str, Any]
) -> DiffusionLimitedAggregationConfig:
    return DiffusionLimitedAggregationConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        particle_count=int(values["particle_count"]),
        stroke_thickness=int(values["stroke_thickness"])
    )

DIFFUSION_LIMITED_AGGREGATION_DEFINITION = AlgorithmDefinition(
    algorithm_id="diffusion_limited_aggregation",
    display_name="Diffusion-Limited Aggregation (DLA)",
    description="Creates branching caves my simulating randomly moving particles that attach to a structure.",
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=DiffusionLimitedAggregationGenerator()
)