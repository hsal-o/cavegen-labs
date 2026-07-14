from dataclasses import dataclass
from typing import Generic, TypeVar

from cavegenlabs.domain.models import CaveMap


ConfigT = TypeVar("ConfigT")


@dataclass(frozen=True)
class GenerationResult(Generic[ConfigT]):
    algorithm_id: str
    algorithm_name: str
    config: ConfigT
    seed: int
    cave_map: CaveMap
    duration_seconds: float