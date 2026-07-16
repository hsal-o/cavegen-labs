from cavegenlabs.presentation.inputs.decimal_parameter_input import DecimalParameterInput
from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="iteration_count",
            label="Iteration Count",
            default=5
        ),
        DecimalParameterInput(
            key="nonsolid_odds",
            label="Nonsolid Odds",
            default=0.65
        ),
        IntegerParameterInput(
            key="solidify_threshold",
            label="Solidify Threshold",
            default=4
        ),
        IntegerParameterInput(
            key="nonsolidify_threshold",
            label="Nonsolidify Threshold",
            default=3
        ),
    )