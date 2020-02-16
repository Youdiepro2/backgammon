from game.Player import Player
from game.Fields import Fields
from game.Pawns import Pawns
from game.Dices import Dices
from game.Moves import Moves
from game.Move import Move
from game.Constants import HOME_MOVE_FIELD_ID
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
        self.moves = Moves()
        barPawns = self.turn.getPawnsFromBar()
        if 0 != len(barPawns):
            self.moves = self.fields.getBarPawnsMoves(barPawns, self.dices, self.turn)
            return

        # print(self.turn.redyForWinningMoves(), self.turn.__dict__)
        if self.turn.redyForWinningMoves():
            self.moves = self.fields.getWinningMoves(self.turn, self.dices)
            # for move in self.moves:
            #     print('winning move', move)

        self.moves.merge(self.fields.getMoves(self.dices, self.turn))

    def move(self, move: Move):
        if move not in self.moves:
            return

        pawn = self.pawns.getPawnById(move.pawnId)
        currentField = self.fields.getFieldById(pawn.fieldId)
        nextField = self.fields.getFieldById(move.fieldId)

        if nextField and nextField.hasOnePawnToBeat(pawn):
            beatedPawn = nextField.getPawnOnTop()
            nextField.removePawnFromTop()
            beatedPawn.fieldId = self.turn.getOppositeBarId()

        # bar is not included in fields
        if currentField:
            currentField.removePawnFromTop()
        if nextField:
            nextField.addPawn(pawn)

        pawn.fieldId = move.fieldId
        self.dices.removeResult(move.diceResult)

        if 0 == len(self.dices.results):
            self.changeTurn()

        self.getMoves()
        # for move in self.moves:
        #     print(move.__dict__)
        # return

        if 0 == len(self.moves):
            self.changeTurn()
            self.getMoves()

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
