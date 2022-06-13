def fizzbuzz(i):
    if i % 5 == 0 and i % 3 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str(i)

# pytest .\fizzbuzz.py -v
def test_nonfizzbuzz_numbers():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(1048576) == "1048576"

def test_fizz_numbers():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(6) == "fizz"

def test_buzz_numbers():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(10) == "buzz"

def test_fizzbuzz_numbers():
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(30) == "fizzbuzz"

