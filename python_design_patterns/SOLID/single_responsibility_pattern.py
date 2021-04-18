# The single responsibility principle pattern.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos: int) -> str:
        del self.entries[pos]

    def __str__(self)-> str:
        return '\n'.join(self.entries)

    # So far so good. All the methods above should be in the responsibility of the `Journal`-class.
    # Let's now add method that should not be part of the class, a method to write itself to a file:
    def save(self, filename: str):
        with open(file_name, "w") as file_handler:
            file_handler.write(str(self))

    # So why is that bad?
    # -> Typically, there wil be multiple classes like `Journal`. All of them need to be saved.
    # -> Now if you create a `save`-method for all these classes it will be very hard to change
    # -> and maintain them constistently!


if __name__ == "__main__": 
    j = Journal()
    j.add_entry("I cried today")
    j.add_entry("I ate a bug" )
    print(f"Journal entries: \n{j}")



