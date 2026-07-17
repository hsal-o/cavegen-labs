from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="particle_count",
            label="Particle Count",
            default=150,
            minimum=1,
        ),
        IntegerParameterInput(
            key="stroke_thickness",
            label="Stroke Thickness",
            default=3,
            minimum=1
        )
    )