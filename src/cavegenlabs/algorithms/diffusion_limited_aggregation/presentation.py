from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="particle_count",
            label="Particle Count",
            default=10,
            minimum=1,
        ),
    )