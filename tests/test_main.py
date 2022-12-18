"""Your tests goes here."""


from pypackage import main


def test_hello_world(example_fixture) -> None:
    """Test hello_world()."""

    print(example_fixture)

    assert main.hello_world() == "Hello, World!"
