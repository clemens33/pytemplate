"""My Module."""


def add(c: int, b: int) -> int:
    """Add function.

    Args:
        c (int): first number
        b (int): second number

    Returns:
        int: the added number
    """

    return c + b


def sub(c: int, b: int) -> int:
    """_summary_.

    Args:
        c (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """

    return c - b


def main():
    """Add and sub function."""
    print(add(1, 2))
    print(sub(1, 2))


if __name__ == "__main__":
    main()
