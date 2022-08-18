from divide_stuff import Divider, __version__


def test_version():
    assert __version__ == "0.1.0"


def test_divide_numbers():
    divider = Divider()
    val = divider.divide_numbers(20, 10)
    assert val == 2
