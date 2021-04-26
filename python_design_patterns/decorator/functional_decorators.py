# The decorator design patter.
# A decorator facilitates the addition of behaviors to individual objects
# without inheriting from them.
import time
from typing import Callable


# In python the functional decorator is part of the language:
def time_it(fun: Callable) -> Callable:
    def wrapper():
        start = time.time()
        result = fun()
        end = time.time()
        print(f"{fun.__name__} took {int(end - start) * 1000}ms.")
        return result

    return wrapper


@time_it
def some_operation():
    print("Starting the Operation.")
    time.sleep(1)
    print("Wer are done.")
    return 123


if __name__ == "__main__":
    some_operation()