import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("starting...")

for i in range(1,100):
    logging.debug(f"[{i}] i % 5 == {i % 5}")
    logging.debug(f"[{i}] i % 3 == {i % 3}")

    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

logging.info("finished.")
