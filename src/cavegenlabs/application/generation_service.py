from random import Random
from time import perf_counter
from typing import TypeVar

from cavegenlabs.application.algorithm_registry import AlgorithmRegistry
from cavegenlabs.application.generation_result import GenerationResult


ConfigT = TypeVar("ConfigT")


class GenerationService:
    def __init__(
            self,
            registry: AlgorithmRegistry
    ) -> None:
        self._registry = registry

    def generate(
            self,
            algorithm_id: str,
            config: ConfigT,
            seed: int
    ) -> GenerationResult[ConfigT]:
        definition = self._registry.get(algorithm_id)

        rng = Random(seed)

        start_time = perf_counter()

        cave_map = definition.generator.generate(
            config=config,
            rng=rng
        )

        duration_seconds = perf_counter() - start_time

        return GenerationResult(
            algorithm_id=definition.algorithm_id,
            algorithm_name=definition.display_name,
            config=config,
            seed=seed,
            cave_map=cave_map,
            duration_seconds=duration_seconds
        )