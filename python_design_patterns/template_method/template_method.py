# The template method design pattern.
# As in the strategy pattern, algorithms are composed as common parts + specifics
# but where the strategy pattern implements this via composition, the template method
# uses inhertiance. More formally:
# The template method allows to define the skeleton of the algorithm with concrete
# implementations defined in subclass.
from abc import ABC


class Game(ABC):
    def __init__(
        self,
        n_players,
    ):
        self.n_players = n_players
        self.current_player = 0

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    def start(self):
        pass

    @property
    def have_winner(self):
        pass

    def take_turn(self):
        pass

    @property
    def winning_player(self):
        pass


class Chess(Game):
    def __init__(self):
        super().__init__(n_players=2)
        self.max_n_turns = 10
        self.turn = 1

    def start(self):
        print(f"Starting a game of chess with {self.n_players}.")

    @property
    def have_winner(self):
        return self.turn == self.max_n_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()