"""CrossHair symbolic-execution fixture: functions with pre/post condition
contracts in their docstrings, per PEP 316 / CrossHair's contract syntax."""
from typing import List


def clamp(value: int, low: int, high: int) -> int:
    """
    pre: low <= high
    post: low <= __return__ <= high
    """
    if value < low:
        return low
    if value > high:
        return high
    return value


def total(values: List[int]) -> int:
    """
    post: __return__ >= 0 if all(v >= 0 for v in values) else True
    """
    result = 0
    for v in values:
        result += v
    return result
