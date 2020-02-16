from game.Move import Move

class Moves():
    moves = []

    def __init__(self):
        self.moves = []

    def __iter__(self):
        return iter(self.moves)

    def __len__(self):
        return len(self.moves)

    def merge(self, moves):
        self.moves = self.moves + moves.moves

    def append(self, move: Move):
        self.moves.append(move)
