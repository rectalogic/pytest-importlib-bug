from ..google_workspace import getclass
from ..integration import Event


print(f"{__file__} {id(Event)}")


def test_it():
    assert getclass() is Event
