from typing import Any


def is_numeric(*args: Any, **kwargs: Any) -> bool:
    data = list(args) + list(kwargs.values())

    if not data:
        return False

    for arg in data:
        if not isinstance(arg, (int, float)):
            return False

    return True
