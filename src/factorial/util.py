import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def factorial(n):
    if n == 0:
        return 1
    else:
        result= n * factorial(n - 1)
        return result
        logging.debug(result)
