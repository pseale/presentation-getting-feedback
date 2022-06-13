import logging

def storeInEnterpriseDataWarehouse(i):
    # this exists only for demo purposes, so we can more clearly read the logs - don't actually do anything
    return ""

logging.basicConfig(level=logging.DEBUG)
logging.info("starting...")
for i in range(1,100 + 1):
    logging.debug(f"[{i}] i % 5 == {i % 5}")
    logging.debug(f"[{i}] i % 3 == {i % 3}")

    if i % 5 == 0 and i % 3 == 0:
        logging.debug(f"[{i}] fizzbuzz")
        storeInEnterpriseDataWarehouse("fizzbuzz")
    elif i % 3 == 0:
        logging.debug(f"[{i}] fizz")
        storeInEnterpriseDataWarehouse("fizz")
    elif i % 5 == 0:
        logging.debug(f"[{i}] buzz")
        storeInEnterpriseDataWarehouse("buzz")
    else:
        logging.debug(f"[{i}] neither fizz nor buzz")
        storeInEnterpriseDataWarehouse(i)
logging.info("finished.")
