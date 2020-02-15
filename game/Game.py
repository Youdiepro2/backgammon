from game.Player import Player
from game.Fields import Fields
from game.Pawns import Pawns
from game.Dices import Dices
from game.Moves import Moves
import json

class Game():
    players = None
    fields = None
    pawns = None
    dices = None
    turn = None
    winner = None
    moves = None

    def __init__(self):
        self.dices = Dices()
        self.pawns = Pawns.createInitial()
        self.players = [Player.createWhitePlayer(), Player.createBlackPlayer()]
        self.fields = Fields()
        self.fields.setInitialState()
        # todo change later
        self.turn = self.players[0]
        self.winner = None
        for player in self.players:
            self.fields.setPawnsAtStartPositions(self.pawns, player)
            player.pawns = self.pawns.getPawnsForPlayer(player)
        self.moves = Moves()

    def getMoves(self):
        # todo remeber to update pawns in Pawns, Player, every field
        self.dices.roll()
        self.moves = self.fields.getMoves(self.dices, self.turn)
        print('dices', self.dices.results)
        for move in self.moves:
            print(move.__dict__)
        # return

    def toJSON(self)->str:
        return json.dumps(
            self,
            default=lambda o: o.__dict__ if hasattr(o, '__dict__') else None,
            sort_keys=True,
            indent=4
        )
