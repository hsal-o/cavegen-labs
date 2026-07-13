from random import Random
from typing import Protocol, TypeVar

from cavegenlabs.domain.models import CaveMap


ConfigT = TypeVar("ConfigT", contravariant=True)


class CaveGenerator(Protocol[ConfigT]):
    def generate(
            self,
            config: ConfigT,
            rng: Random
    ) -> CaveMap:
        ...