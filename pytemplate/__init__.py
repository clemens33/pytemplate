"""my test module"""


def my_function(**kwargs) -> int:
    """asdfasdf

    Returns:
        int: asdf
    """
    ret = 0

    for _, val in kwargs.items():
        ret += val

    return ret


def my_bad_function() -> int:
    """my bad function"""
    aaa = 0
    bbb = 2
    ccc = 3

    for i in range(10):
        aaa += i
        bbb += i
        ccc += i

    return aaa + bbb + ccc


def func() -> str:
    """a random function"""

    return "hello world"


def main():
    """main function"""
    x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}

    print(my_function(**x))


if __name__ == "__main__":
    main()
