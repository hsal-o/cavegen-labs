import pytest

from cavegenlabs.domain.models import CaveMap, Tile


def test_get_tile_returns_tile_at_coordinates() -> None:
    cave_map = CaveMap(
        width=2,
        height=2,
        cells=(
            (Tile.SOLID, Tile.AIR),
            (Tile.AIR, Tile.SOLID)
        )
    )

    assert cave_map.get_tile(1, 1) is Tile.SOLID
    assert cave_map.get_tile(1, 0) is Tile.AIR
    assert cave_map.get_tile(0, 1) is Tile.AIR
    assert cave_map.get_tile(0, 0) is Tile.SOLID

def test_is_in_bounds_returns_true_for_valid_coordinates() -> None:
    cave_map = CaveMap(
        width=2,
        height=2,
        cells=(
            (Tile.SOLID, Tile.SOLID),
            (Tile.SOLID, Tile.SOLID),
        )
    )

    assert cave_map.is_in_bounds(0, 0)
    assert cave_map.is_in_bounds(1, 1)

def test_is_in_bounds_returns_false_for_invalid_coordinates() -> None:
    cave_map = CaveMap(
        width=2,
        height=2,
        cells=(
            (Tile.SOLID, Tile.SOLID),
            (Tile.SOLID, Tile.SOLID),
        )
    )

    assert not cave_map.is_in_bounds(-1, 0)
    assert not cave_map.is_in_bounds(2, 0)
    assert not cave_map.is_in_bounds(0, 2)    

def test_rejects_non_positive_width() -> None:
    with pytest.raises(ValueError, match="Width must be greater than zero"):
        CaveMap(
            width=0,
            height=1,
            cells=((Tile.SOLID,),)
        )

def test_rejects_non_positive_height() -> None:
    with pytest.raises(ValueError, match="Height must be greater than zero"):
        CaveMap(
            width=1,
            height=0,
            cells=()
        )

def test_rejects_incorrect_row_count() -> None:
    with pytest.raises(ValueError, match="Cell row count must match height"):
        CaveMap(
            width=2,
            height=2,
            cells=((Tile.SOLID, Tile.SOLID),)
        )


def test_rejects_incorrect_row_width() -> None:
    with pytest.raises(ValueError, match="Each cell row must match width"):
        CaveMap(
            width=2,
            height=1,
            cells=((Tile.SOLID,),)
        )


def test_get_tile_rejects_out_of_bounds_coordinates() -> None:
    cave_map = CaveMap(
        width=1,
        height=1,
        cells=((Tile.SOLID,),)
    )

    with pytest.raises(IndexError, match="Coordinates out of bounds"):
        cave_map.get_tile(1, 0)