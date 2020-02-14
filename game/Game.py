from game.Player import Player
from game.Fields import Fields
from game.Pawns import Pawns
from game.Dices import Dices

class Game():
    players = None
    fields = None
    pawns = None
    dices = None
    turn = None
    winner = None

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

    def getMoves(self):
        # todo remeber to update pawns in Pawns, Player, every field
        self.dices.roll()
        moves = self.fields.getMoves(self.dices, self.turn)
        print('dices', self.dices.results)
        for move in moves:
            print(move.__dict__)
        # return
