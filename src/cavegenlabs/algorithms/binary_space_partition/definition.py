from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.binary_space_partition.config import BinarySpacePartitionConfig
from cavegenlabs.algorithms.binary_space_partition.generator import BinarySpacePartitionGenerator
from cavegenlabs.algorithms.binary_space_partition.presentation import create_inputs
from cavegenlabs.domain.generation.algorithm_definition import AlgorithmDefinition


def create_config(
    values: Mapping[str, Any]
) -> BinarySpacePartitionConfig:
    return BinarySpacePartitionConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        iteration_count=int(values["iteration_count"]),
        min_width=int(values["min_width"]),
        min_height=int(values["min_height"]),

        do_connect_rooms=bool(values["do_connect_rooms"]),
        hallway_stroke_thickness=int(values["hallway_stroke_thickness"])
    )

BINARY_SPACE_PARTITION_DEFINITION = AlgorithmDefinition(
    algorithm_id="binary_space_partition",
    display_name="Binary Space Partition",
    description="Generates cave rooms by recursively dividing the given area into sections.",
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=BinarySpacePartitionGenerator()
)