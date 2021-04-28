# The chain of responsibility design pattern.
# A chain of components who all get a chance to process a command or a query, optionally having default
# processing implementation and an ability to terminate the processing chain.


class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()
        return self


class DoubleDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack >= 2:
            print(f"Doubling {self.creature.name}'s defense")
            self.creature.defense *= 2
        super().handle()


class NoBonusModifier(CreatureModifier):
    def handle(self):
        print("No bonus for you!")


if __name__ == "__main__":
    goblin = Creature("Goblin", 1, 1)
    print(goblin)
    root_modifier = CreatureModifier(goblin)
    root_modifier.add_modifier(DoubleDefenseModifier(goblin))
    root_modifier.add_modifier(DoubleAttackModifier(goblin))
    root_modifier.add_modifier(NoBonusModifier(goblin))
    root_modifier.add_modifier(DoubleAttackModifier(goblin))

    root_modifier.handle()
    print(goblin)
