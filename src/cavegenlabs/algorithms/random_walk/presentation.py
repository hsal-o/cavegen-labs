from cavegenlabs.domain.models.grid_position import GridPosition
from cavegenlabs.algorithms.random_walk.widgets.position_input import (
    PositionInput,
)
from cavegenlabs.presentation.inputs.decimal_parameter_input import (
    DecimalParameterInput,
)
from cavegenlabs.presentation.inputs.integer_parameter_input import (
    IntegerParameterInput,
)
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="walker_count",
            label="Walker Count",
            default=1,
            minimum=1,
        ),
        IntegerParameterInput(
            key="step_count",
            label="Step Count",
            default=100,
            minimum=1,
        ),
        IntegerParameterInput(
            key="thickness",
            label="Thickness",
            default=1,
            minimum=1,
        ),
        DecimalParameterInput(
            key="bias",
            label="Bias",
            default=0.00,
            minimum=0.0,
            maximum=1.0,
        ),
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
    )