from collections.abc import Mapping
from typing import Any

from cavegenlabs.algorithms.cellular_automata.config import CellularAutomataConfig
from cavegenlabs.domain.generation.algorithm_definition import AlgorithmDefinition
from cavegenlabs.algorithms.cellular_automata.presentation import create_inputs
from cavegenlabs.algorithms.cellular_automata.generator import CellularAutomataGenerator

def create_config(
        values: Mapping[str, Any]
) -> CellularAutomataConfig:
    return CellularAutomataConfig(
        width=int(values["width"]),
        height=int(values["height"]),
        iteration_count=int(values["iteration_count"]),
        nonsolid_odds=float(values["nonsolid_odds"]),
        solidify_threshold=int(values["solidify_threshold"]),
        nonsolidify_threshold=int(values["nonsolidify_threshold"])
    )

CELLULAR_AUTOMATA_DEFINITION = AlgorithmDefinition(
    algorithm_id="cellular_automata",
    display_name="Cellular Automata",
    description="Generate organic cave layouts by repeatdely updating cells based on their neighbors.",
    create_inputs=create_inputs,
    config_factory=create_config,
    generator=CellularAutomataGenerator()
)