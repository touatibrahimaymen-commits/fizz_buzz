from src.fizz_buzz import fizz_buzz


def test()-> None:
    fizz_buzz()

def test_fizzbuzz_returns_num_1():

    assert fizz_buzz(9) == "fizz"