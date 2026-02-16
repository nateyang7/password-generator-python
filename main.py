from src.password_generator.password_generator import *


def main() -> int:
    password: str = generate_password()
    print(f"Your password: {password}")
    return 0


if __name__ == "__main__":
    main()

