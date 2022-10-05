import dataclasses


@dataclasses.dataclass
class Event:
    f: int


def doctest():
    """
    >>> x = Event(33)
    """
    pass
