import pytest
import random
from password_generator.password_generator import *

random.seed(0)

def test_is_strong():
    assert is_strong("Qwerty41!")
    assert not is_strong("1234")
    assert is_strong(" Azerty41@ ")


def test_generate_letter():
    assert generate_letter() == 'Y'


def test_generate_digit():
    assert generate_digit() == '6'


def test_generate_special_char():
    assert generate_special_char() == '!'


def test_generate_char():
    assert generate_char() == '8'


def test_generate_password():
    assert generate_password() == "eg19*V#3cz&0"    

