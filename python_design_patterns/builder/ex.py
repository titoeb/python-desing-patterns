class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def add_field(self, type, name):
        self.fields.append((type, name))
        return self

    def __str__(self):
        return f"class {self.root_name}:\n\tdef __init__(self):\n" + "\n".join(
            [f"\t\tself.{name} = {content}" for name, content in self.fields]
        )


if __name__ == "__main__":
    code_builder = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
    print(code_builder)