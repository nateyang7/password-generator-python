import pytest
from password_generator.password_generator import is_strong

def test_is_strong():
    assert is_strong("Qwerty41!")
    assert not is_strong("1234")
    assert is_strong(" Azerty41@ ")

