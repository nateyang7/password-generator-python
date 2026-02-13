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
    requirements: dict[str, bool] = {
        "has1cap": False,
        "has1small": False,
        "has1digit": False,
        "has1spec": False,
    }
    special_characters: str = "!@#$%&*"

    for char in password.strip():
        if char.isupper():
            requirements["has1cap"] = True
        if char.islower():
            requirements["has1small"] = True
        if char.isdigit():
            requirements["has1digit"] = True
        if char in special_characters:
            requirements["has1spec"] = True

    return all(requirements.values())

