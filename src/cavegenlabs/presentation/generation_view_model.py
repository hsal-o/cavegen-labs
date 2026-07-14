from collections.abc import Mapping
from secrets import randbits
from typing import Any

from cavegenlabs.application import (
    AlgorithmRegistry,
    GenerationResult,
    GenerationService,
)
from cavegenlabs.domain.generation import AlgorithmDefinition
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class GenerationViewModel:
    def __init__(
        self,
        registry: AlgorithmRegistry,
        generation_service: GenerationService,
    ) -> None:
        self._registry = registry
        self._generation_service = generation_service
        self._selected_algorithm_id: str | None = None

    @property
    def selected_algorithm_id(self) -> str | None:
        return self._selected_algorithm_id

    def get_algorithms(
        self,
    ) -> tuple[AlgorithmDefinition[object], ...]:
        return self._registry.get_all()

    def select_algorithm(
        self,
        algorithm_id: str,
    ) -> tuple[ParameterInput, ...]:
        definition = self._registry.get(algorithm_id)

        self._selected_algorithm_id = algorithm_id

        return definition.create_inputs()
    
    def generate(
        self,
        base_values: Mapping[str, int | None],
        algorithm_values: Mapping[str, object],
    ) -> GenerationResult[object]:
        if self._selected_algorithm_id is None:
            raise ValueError("An algorithm must be selected.")

        definition = self._registry.get(
            self._selected_algorithm_id,
        )

        seed = base_values["seed"]

        if seed is None:
            seed = randbits(32)

        config_values: dict[str, Any] = {
            "width": base_values["width"],
            "height": base_values["height"],
            **algorithm_values,
        }

        config = definition.config_factory(config_values)

        return self._generation_service.generate(
            algorithm_id=definition.algorithm_id,
            config=config,
            seed=seed,
        )