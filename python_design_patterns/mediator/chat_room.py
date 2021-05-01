# The mediator design pattern.
# A component that ficilitates communication between other components without
# them necessarily being aware of each other or having direct (reference) access to each other.
from __future__ import annotations
from typing import List


class Person:
    def __init__(self, name: str):
        self.name = name
        self.chat_log: List = []
        self.room: ChatRoom = None

    def receive(self, sender: str, message: str):
        message_formatted = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {message_formatted}")
        self.chat_log.append(message_formatted)

    def private_message(self, who: str, message: str) -> None:
        self.room.message(self.name, who, message)

    def say(self, message: str) -> None:
        self.room.broadcast(self.name, message)


class ChatRoom:
    def __init__(self) -> None:
        self.people: List[Person] = []

    def join(self, person: Person):
        join_msg = f"{person.name} joins the chat."
        self.broadcast("room", join_msg)
        self.people.append(person)
        person.room = self

    def broadcast(self, source: str, message: str):
        for person in self.people:
            if person.name != source:
                person.receive(source, message)

    def message(self, source: str, destination: str, message: str):
        for person in self.people:
            if person.name == destination:
                person.receive(source, message)


if __name__ == "__main__":
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")
    peter = Person("Person")

    room.join(john)
    room.join(jane)

    john.say("Hi room!")
    jane.say("Oh, hey John!")

    peter = Person("Peter")
    room.join(peter)
    peter.say("Hey everyone!")

    jane.private_message("Peter", "glad to see you!")
