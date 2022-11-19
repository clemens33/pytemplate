import sys


def my_function(**kwargs) -> int:
    r = 0

    for k, v in kwargs.items():
        r += v

    return r


def main():
    x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}

    print(my_function(**x))


if __name__ == '__main__':
    main()
