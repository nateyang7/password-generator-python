import random


SPECIAL_CHARACTERS: str = "!@#$%&*"

def is_strong(password: str) -> bool:
    """
    Tests if a password is strong.

    Args:
        password (str): Password to test.

    Returns:
        bool: True if password is strong else False.

    Examples:
        >>> is_strong("Qwerty41!")
        True
        >>> is_strong("1234")
        False

    Notes:
        A password is strong if it validates this requirements:
        - >= 8 characters
        - At least 1 capital letter
        - At least 1 small letter
        - At least 1 digit
        - At least 1 special character (!@#$%&*)
    """
    global SPECIAL_CHARACTERS
    requirements: dict[str, bool] = {
        "has1cap": False,
        "has1small": False,
        "has1digit": False,
        "has1spec": False,
    }

    for char in password.strip():
        if char.isupper():
            requirements["has1cap"] = True
        if char.islower():
            requirements["has1small"] = True
        if char.isdigit():
            requirements["has1digit"] = True
        if char in SPECIAL_CHARACTERS:
            requirements["has1spec"] = True

    return all(requirements.values())


def generate_char() -> str:
    """
    Returns a character in upper or lower case.

    Returns:
        str: Random character in upper or lower case.
    """
    lower_alpha: list[str] = [chr(ascii_code) for ascii_code in range(65, 91)]
    upper_alpha: list[str] = [chr(ascii_code) for ascii_code in range(97, 123)]
    return random.choice(lower_alpha + upper_alpha)


def generate_digit() -> str:
    """
    Returns a digit.

    Returns:
        str: Digit from 0 to 9.
    """
    return str(random.randint(0, 10))


def generate_special_char() -> str:
    """
    Returns a special character.

    Returns:
        str: Special character.
    """
    global SPECIAL_CHARACTERS
    return random.choice(SPECIAL_CHARACTERS)


def generate_passchar() -> str:
    """
    Returns a letter, digit or a special character.

    Returns:
        str: Letter, digit or a special character.
    """
    char: str = generate_char()
    digit: str = generate_digit()
    special_char: str = generate_special_char()
    return random.choice((char, digit, special_char))


def generate_password() -> str:
    """
    Returns a strong password.

    Returns:
        str: Random generated password.
    """
    length: int = random.randint(8, 16)
    password: str = ''.join(
            char for char in [generate_passchar() for char in range(length)]
            )
    while not is_strong(password):
        password = ''.join(
                char for char in [generate_passchar() for char in range(length)]
                )
    return password

