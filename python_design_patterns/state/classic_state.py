# The state design pattern.
# The objects behaviour is determined by its state. An object transitions from one state to another.
# A formalized contruct which manages state and transitions is called a state machine.
from __future__ import annotations
from abc import ABC


class State(ABC):
    def on(self, switch: Switch):
        print("Light is already on.")

    def off(self, switch: Switch):
        print("Light is already off.")


class OnState(State):
    def __init__(self) -> None:
        print("Light turned on")

    def off(self, switch: Switch):
        print("Turning the light off.")
        switch.state = OffState()


class OffState(State):
    def __init__(self) -> None:
        print("Light turned off.")

    def on(self, switch: Switch):
        print("Turning the light on.")
        switch.state = OnState()


class Switch:
    def __init__(self) -> None:
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


# This is a classic example of a state machine but overall
# it is way to complicated and also you would not want to
# let the state regulate the transition of the state itself.
if __name__ == "__main__":
    switch = Switch()
    switch.on()
    switch.off()
    switch.off()