from app.src.calculate_fine import (
    late_penalties,
    interest_per_day,
    calculate_fine,
)


def test_late_penalties_to_zero_days():
    expected = 0
    days = 0
    assert late_penalties(days=days) == expected


def test_late_penalties_to_one_days():
    expected = 3
    days = 1
    assert late_penalties(days=days) == expected


def test_late_penalties_to_two_days():
    expected = 3
    days = 2
    assert late_penalties(days=days) == expected


def test_late_penalties_to_three_days():
    expected = 3
    days = 3
    assert late_penalties(days=days) == expected


def test_late_penalties_to_four_days():
    expected = 5
    days = 4
    assert late_penalties(days=days) == expected


def test_late_penalties_to_five_days():
    expected = 7
    days = 6
    assert late_penalties(days=days) == expected


def test_interest_per_day_to_zero_days():
    expected = 0.0
    days = 0
    assert interest_per_day(days=days) == expected


def test_interest_per_day_to_one_days():
    days = 1
    expected = 0.2 * days
    assert interest_per_day(days=days) == expected


def test_interest_per_day_to_two_days():
    days = 2
    expected = 0.2 * days
    assert interest_per_day(days=days) == expected


def test_interest_per_day_to_three_days():
    days = 3
    expected = 0.2 * days
    assert interest_per_day(days=days) == expected


def test_interest_per_day_to_four_days():
    days = 4
    expected = 0.4 * days
    assert interest_per_day(days=days) == expected


def test_interest_per_day_to_five_days():
    days = 5
    expected = 0.4 * days
    assert interest_per_day(days=days) == expected


def test_interest_per_day_to_fix_days():
    days = 6
    expected = 0.6 * days
    assert interest_per_day(days=days) == expected


def test_calculete_fine_to_zero_days():
    days = 0
    expected = 0
    assert calculate_fine(days=days) == expected


def test_calculete_fine_to_one_days():
    days = 1
    expected = 3.2
    assert calculate_fine(days=days) == expected


def test_calculete_fine_to_three_days():
    days = 3
    expected = 3.6
    assert calculate_fine(days=days) == expected


def test_calculete_fine_to_fix_days():
    days = 6
    expected = 10.6
    assert calculate_fine(days=days) == expected
