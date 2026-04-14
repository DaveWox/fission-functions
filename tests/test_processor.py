import pytest
from processor import process_numbers


def test_valid_numbers():
    result = process_numbers([1, 2, 3, 4])

    assert result["count"] == 4
    assert result["sum"] == 10
    assert result["min"] == 1
    assert result["max"] == 4
    assert result["average"] == 2.5



def test_empty_list():
    with pytest.raises(ValueError) as exc:
        process_numbers([])

    assert "empty" in str(exc.value)


def test_invalid_type():
    with pytest.raises(ValueError) as exc:
        process_numbers("oops")

    assert "must be a list" in str(exc.value)
