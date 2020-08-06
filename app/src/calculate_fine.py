from app.constants import (
    ZERO_PERCENT,
    THREE_PERCENT,
    FIVE_PERCENT,
    SEVEN_PERCENT,
    ZERO_DAYS,
    THREE_DAYS,
    FIVE_DAYS,
)


def late_penalties(days: int) -> int:
    if days == ZERO_DAYS:
        return ZERO_PERCENT
    elif days <= THREE_DAYS:
        return THREE_PERCENT
    elif days <= FIVE_DAYS:
        return FIVE_PERCENT
    return SEVEN_PERCENT


def interest_per_day(days: int) -> float:
    if days == ZERO_DAYS:
        return 0.0
    elif days <= THREE_DAYS:
        return days * 0.2
    elif days <= FIVE_DAYS:
        return days * 0.4
    return days * 0.6


def calculate_fine(days):
    return late_penalties(days) + interest_per_day(days)
