# The flyweight design pattern.
# The flyweight design pattern is a space optimization techinque that uses less memory by storing the
# data associated with similar objects internally, only once.
import string
import random


class SimpleUser:
    def __init__(self, name):
        self.name = name


class EfficientUser:
    name_parts = []

    def __init__(self, name):
        self.names = [self.get_or_add(name_part) for name_part in name.split(" ")]

    def get_or_add(self, name_part: str):
        if name_part in self.name_parts:
            return self.name_parts.index(name_part)
        else:
            self.name_parts.append(name_part)
            return len(self.name_parts) - 1

    def __str__(self):
        return " ".join([self.name_parts[name_part] for name_part in self.names])


def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(8)])


if __name__ == "__main__":
    simple_users = []
    efficient_users = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first_name in first_names:
        for last_name in last_names:
            simple_users.append(SimpleUser(f"{first_name} {last_name}"))

    for first_name in first_names:
        for last_name in last_names:
            efficient_users.append(EfficientUser(f"{first_name} {last_name}"))

    print(efficient_users[10])