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
    """Sub function."""
    return c - b


def main():
    """Add and sub function."""
    print(add(1, 2))
    print(sub(1, 2))


if __name__ == "__main__":
    main()
