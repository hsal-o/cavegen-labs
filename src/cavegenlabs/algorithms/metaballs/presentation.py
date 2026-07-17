from cavegenlabs.presentation.inputs.decimal_parameter_input import DecimalParameterInput
from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="metaball_count",
            label="(+) Metaball Count",
            default=6,
            minimum=1
        ),
        IntegerParameterInput(
            key="negative_metaball_count",
            label="(-) Metaball Count",
            default=0,
            minimum=0
        ),
        IntegerParameterInput(
            key="min_radius",
            label="Min Radius",
            default=4,
            minimum=1
        ),
        IntegerParameterInput(
            key="max_radius",
            label="Max Radius",
            default=6,
            minimum=1
        ),
        DecimalParameterInput(
            key="threshold",
            label="Threshold",
            default=0.8,
            minimum=0.01
        ),
    )