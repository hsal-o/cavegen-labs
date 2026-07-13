from collections.abc import Iterable

from cavegenlabs.domain.generation import AlgorithmDefinition


class AlgorithmRegistry:
    def __init__(
            self,
            definitions: Iterable[AlgorithmDefinition[object]],
    ) -> None:
        definition_list = tuple(definitions)

        self._definitions = {
            definition.algorithm_id: definition for definition in definition_list
        }

        if len(self._definitions) != len(definition_list):
            raise ValueError("Algorithm IDs must be unique.")
        
    def get(
            self,
            algorithm_id: str 
    ) -> AlgorithmDefinition[object]:
        try:
            return self._definitions[algorithm_id]
        except KeyError as error:
            raise KeyError(f"Unknown algorithm ID: {algorithm_id}") from error 
        
    def get_all(
            self
    ) -> tuple[AlgorithmDefinition[object], ...]:
        return tuple(self._definitions.values())