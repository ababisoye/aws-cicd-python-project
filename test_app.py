import pytest

from app import calculate_rental_cost


def test_calculate_rental_cost():
    assert calculate_rental_cost(6, 5000) == 30000


def test_calculate_rental_cost_for_12_hours():
    assert calculate_rental_cost(12, 5000) == 60000


def test_reject_zero_hours():
    with pytest.raises(ValueError):
        calculate_rental_cost(0, 5000)


def test_reject_negative_rate():
    with pytest.raises(ValueError):
        calculate_rental_cost(6, -5000)
