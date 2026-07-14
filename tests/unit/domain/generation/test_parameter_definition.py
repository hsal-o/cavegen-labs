import pytest 

from cavegenlabs.domain.generation.parameter_definition import ParameterDefinition, ParameterValueType


def test_creates_valid_integer_parameter_definition() -> None:
    parameter = ParameterDefinition(
        key="iterations",
        label="Iterations",
        parameter_type=ParameterValueType.INTEGER,
        default=5,
        minimum=0,
        maximum=100
    )

    assert parameter.key == "iterations"
    assert parameter.default == 5

def test_rejects_empty_key() -> None:
    with pytest.raises(ValueError, match="Parameter key can not be empty"):
        ParameterDefinition(
            key="",
            label="Iterations",
            parameter_type=ParameterValueType.INTEGER,
            default=5,
        )

def test_rejects_empty_label() -> None:
    with pytest.raises(ValueError, match="Parameter label can not be empty"):
        ParameterDefinition(
            key="iterations",
            label="",
            parameter_type=ParameterValueType.INTEGER,
            default=5,
        )

def test_rejects_minimum_greater_than_maximum() -> None:
    with pytest.raises(ValueError, match="minimum can not be greater than maximum"):
        ParameterDefinition(
            key="iterations",
            label="Iterations",
            parameter_type=ParameterValueType.INTEGER,
            default=5,
            minimum=10,
            maximum=1,
        )

def test_rejects_choice_parameter_without_choices() -> None:
    with pytest.raises(ValueError, match="Choice parameters must define at least one choice"):
        ParameterDefinition(
            key="start_position",
            label="Start Position",
            parameter_type=ParameterValueType.CHOICE,
            default="center",
        )