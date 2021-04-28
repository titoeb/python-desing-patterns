# The proxy design pattern.
# A class that functions as an interface to a resource. That resource may be remote, expensive to construct or may require
# logging or some other added functionality.
from __future__ import annotations


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f"The car is driven by {self.driver.name}")


class Driver:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# Now we can use the car and drive with it.
if __name__ == "__main__":
    driver = Driver("John", 16)
    car = Car(driver)
    car.drive()


# Now we build our protection proxy. Typically this is used to check whether a user is logged-in
# or similar. But for the time beeing let's simply check if the driver has the correct age. Of course
# the interface should be the same as in `Car`, otherwise it would not be a proxy.
class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print("Driver too young!")


# Everything we have to do, in order to use the proxy class, is to replace the original
# class.
if __name__ == "__main__":
    driver = Driver("John", 16)
    car = CarProxy(driver)
    car.drive()