from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.metaballs.generator import MetaballsGenerator
from cavegenlabs.algorithms.metaballs.presentation import create_inputs
from cavegenlabs.algorithms.metaballs.config import MetaballsConfig
from cavegenlabs.domain.generation.algorithm_definition import AlgorithmDefinition


def create_config(
    values: Mapping[str, Any]
) -> MetaballsConfig:
    return MetaballsConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        metaball_count=int(values["metaball_count"]),
        negative_metaball_count=int(values["negative_metaball_count"]),
        min_radius=int(values["min_radius"]),
        max_radius=int(values["max_radius"]),
        threshold=float(values["threshold"])
    )

METALBALLS_DEFINITION = AlgorithmDefinition(
    algorithm_id="metaballs",
    display_name="Metaballs",
    description="Carves organic, blobby caves by summing the influence of randomly placed metaballs.",
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=MetaballsGenerator()
)