
from cavegenlabs.domain.models.grid_position import GridPosition
from cavegenlabs.presentation.inputs.integer_pair_parameter_input import IntegerPairParameterInput
from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput
from cavegenlabs.presentation.inputs.position_input import PositionInput


def create_input() -> tuple[ParameterInput, ...]:
    return (
        PositionInput(
            key="start_position",
            label="Start Position",
            default=GridPosition.CENTER,
        ),
        PositionInput(
            key="end_position",
            label="End Position",
            default=GridPosition.CENTER,
        ),
        IntegerParameterInput(
            key="iteration_count",
            label="Iteration Count",
            default=5
        ),
        IntegerParameterInput(
            key="magnitude",
            label="Magnitude",
            default=6
        ),
        IntegerParameterInput(
            key="thickness",
            label="Thickness",
            default=3
        ),
        IntegerPairParameterInput(
            key="thickness_variation",
            label="ΔThickness (+/-)",
            default=(0,0)
        )
    )