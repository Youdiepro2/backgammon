from game.Player import Player
from game.Fields import Fields
from game.Pawns import Pawns
from game.Dices import Dices
from game.Moves import Moves
from game.Move import Move
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
        self.players = None
        self.fields = None
        self.pawns = None
        self.dices = None
        self.turn = None
        self.winner = None
        self.moves = None

    def createInInitialState(self):
        self.dices = Dices()
        self.pawns = Pawns.createInitial()
        self.players = [Player.createWhitePlayer(), Player.createBlackPlayer()]
        self.fields = Fields()
        self.turn = self.players[0]
        self.winner = None
        self.moves = Moves()
        self.moveCountPerPlayer = 0
        self.fields.setInitialState()
        for player in self.players:
            self.fields.setPawnsAtStartPositions(self.pawns, player)
            player.pawns = self.pawns.getPawnsForPlayer(player)
        self.dices.roll()
        self.getMoves()

    def getMoves(self):
        barPawns = self.turn.getPawnsFromBar()
        for pawn in barPawns:
            print('barPawns', pawn.__dict__)
        if 0 != len(barPawns):
            self.moves = self.fields.getBarPawnsMoves(barPawns, self.dices, self.turn)
            return


        self.moves = self.fields.getMoves(self.dices, self.turn)
        # print('dices', self.dices.results)
        # for move in self.moves:
        #     print(move.__dict__)
        # return

    def move(self, move: Move):
        if move not in self.moves:
            return

        pawn = self.pawns.getPawnById(move.pawnId)
        currentField = self.fields.getFieldById(pawn.fieldId)
        nextField = self.fields.getFieldById(move.fieldId)

        if nextField.hasOnePawnToBeat(pawn):
            beatedPawn = nextField.getPawnOnTop()
            nextField.removePawnFromTop()
            beatedPawn.fieldId = self.turn.getOppositeBarId()

        # bar is not included in fields
        if currentField:
            currentField.removePawnFromTop()
        pawn.fieldId = nextField.id
        nextField.addPawn(pawn)

        # handle winning moves

        self.dices.removeResult(move.diceResult)

        if 0 == len(self.dices.results):
            self.changeTurn()

        self.getMoves()

        if 0 == len(self.moves):
            self.changeTurn()
            self.getMoves()

        # for move in self.moves:
        #     print(move.__dict__)

    def changeTurn(self):
        self.turn = self.getSecondPlayer()
        self.dices.roll()

    def getSecondPlayer(self):
        for player in self.players:
            if player.color != self.turn.color:
                return player;

    def toJSON(self)->str:
        return json.dumps(
            self,
            default=lambda o: o.__dict__ if hasattr(o, '__dict__') else None,
            sort_keys=True,
            indent=4
        )
