def fizzbuzz(i):
    # preconditions
    # carefully validate inputs - use these in place of proper type systems
    # also useful for validating things like e.g. does file exist, does environment variable exist
    if type(i) != int:
        raise Exception(f"{i} is not an integer")
    if i < 1:
        raise Exception(f"{i} is < 1")
    if i > 100:
        raise Exception(f"{i} is > 100")

    # rest of the function is unlikely to have confusing errors
    if i % 5 == 0 and i % 3 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return str(i)