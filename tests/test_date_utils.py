from datetime import date
from utils.date_utils import (
    count_days_to_new_year,
    count_days_between,
    is_weekend
)


def test_count_days_to_new_year():
    d = date(2025, 12, 25)
    assert count_days_to_new_year(d) == 7


def test_count_days_between():
    d1 = date(2025, 12, 25)
    d2 = date(2026, 1, 1)
    assert count_days_between(d1, d2) == 7


def test_is_weekend():
    d = date(2025, 11, 23)
    assert is_weekend(d) is True

    d2 = date(2024, 11, 20)
    assert is_weekend(d2) is False
