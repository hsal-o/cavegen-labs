from cavegenlabs.presentation.inputs.decimal_pair_parameter_input import DecimalPairParameterInput
from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="octaves",
            label="Octaves",
            default=3
        ),
        DecimalPairParameterInput(
            key="threshold",
            label="Threshold Range",
            default=(-0.12, 0.12)
        )
    )