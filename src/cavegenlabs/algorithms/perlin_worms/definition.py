from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.perlin_worms.config import PerlinWormsConfig
from cavegenlabs.algorithms.perlin_worms.generator import PerlinWormsGenerator
from cavegenlabs.domain.generation.algorithm_definition import AlgorithmDefinition
from cavegenlabs.algorithms.perlin_worms.presentation import create_inputs

def create_config(
    values: Mapping[str, Any]
) -> PerlinWormsConfig:
    return PerlinWormsConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        octaves=int(values["octaves"]),
        threshold=tuple(values["threshold"])
    )

PERLIN_WORMS_DEFINITION = AlgorithmDefinition(
    algorithm_id="perlin_worms",
    display_name="Perlin Worms",
    description="Generates cave systems using Perlin noise.",
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=PerlinWormsGenerator()
)