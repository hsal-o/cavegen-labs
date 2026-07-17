from cavegenlabs.presentation.inputs.boolean_parameter_input import BooleanParameterInput
from cavegenlabs.presentation.inputs.integer_pair_parameter_input import IntegerPairParameterInput
from cavegenlabs.presentation.inputs.integer_parameter_input import IntegerParameterInput
from cavegenlabs.presentation.inputs.parameter_input import ParameterInput


def create_inputs() -> tuple[ParameterInput, ...]:
    return (
        IntegerParameterInput(
            key="iteration_count",
            label="Max Iterations",
            default=3
        ),
        IntegerParameterInput(
            key="min_width",
            label="Mininum Cut Width",
            default=8
        ),
        IntegerParameterInput(
            key="min_height",
            label="Mininum Cut Height",
            default=8
        ),

        BooleanParameterInput(
            key="do_connect_rooms",
            label="Connect Rooms?",
            default=True
        ),
        IntegerParameterInput(
            key="hallway_stroke_thickness",
            label="Connecting Thickness",
            default=2
        ),
    )