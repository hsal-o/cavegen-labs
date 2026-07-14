from cavegenlabs.application import AlgorithmRegistry
from cavegenlabs.domain.generation import AlgorithmDefinition
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


class GenerationViewModel:
    def __init__(
        self,
        registry: AlgorithmRegistry,
    ) -> None:
        self._registry = registry
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