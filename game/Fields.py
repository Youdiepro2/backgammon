from game.Field import Field
from game.Pawn import Pawn
from game.Pawns import Pawns
from game.Player import Player
from game.Moves import Moves
from game.Move import Move
from game.Dices import Dices
from game.Constants import HOME_MOVE_FIELD_ID

class Fields():
    fields = []

    def __init__(self):
        self.fields = []

    def setInitialState(self):
        self.fields = [Field(x+1) for x in range(24)]

    def __iter__(self):
        return iter(self.fields)

    def getWinningMoves(self, player: Player, dices: Dices):
        moves = Moves()
        for result in dices.results:
            for field in self.getFieldsByPawns(player.pawns):
                pawn = field.getPawnOnTop()
                nextFieldId = self.__getFieldIdAfterMove(pawn.fieldId, result, player.direction)
                if nextFieldId > 24 or nextFieldId < 1:
                    moves.append(Move(HOME_MOVE_FIELD_ID, pawn.id, result))
        return moves

    def getBarPawnsMoves(self, barPawns: Pawns, dices: Dices, player: Player)-> Moves:
        moves = Moves()
        for result in dices.results:
            for pawn in barPawns:
                nextFieldId = self.__getFieldIdAfterMove(pawn.fieldId, result, player.direction)
                # print('nextFieldId', nextFieldId, player.__dict__)
                nextField = self.getFieldById(nextFieldId)
                if self.__pawnCanMoveTo(pawn, nextField):
                    moves.append(Move(nextFieldId, pawn.id, result))
        return moves

    def getMoves(self, dices: Dices, player: Player)-> Moves:
        fieldsForCheck = self.getFieldsByPawns(player.pawns)
        moves = Moves()
        for result in dices.results:
            for field in fieldsForCheck:
                nextFieldId = self.__getFieldIdAfterMove(field.id, result, player.direction)
                nextField = self.getFieldById(nextFieldId)
                pawn = field.getPawnOnTop()
                if self.__pawnCanMoveTo(pawn, nextField):
                        # print(pawn.__dict__, nextFieldId)
                        moves.append(Move(nextFieldId, pawn.id, result))
        return moves

    def __getFieldIdAfterMove(self, currentFieldId: int, result: int, direction):
        return currentFieldId + result * direction;

    def __pawnCanMoveTo(self, pawn, nextField)-> bool:
        return nextField and pawn and nextField.accepts(pawn)

    def getFieldsByPawns(self, pawns: Pawns):
        ids = pawns.getFieldIds()
        return self.getFieldsByIds(ids)

    def getFieldsByIds(self, ids: list):
        fields = Fields();
        for id in ids:
            field = self.getFieldById(id)
            if field:
                fields.addField(field)
        return fields

    def setPawnsAtStartPositions(self, pawns: Pawns, player: Player):
        playerPawns = pawns.getPawnsForPlayer(player)
        for i in range(24):
            id = i+1 if player.direction == 1 else 24 - i
            self.__addPawnsOnField(id, i, playerPawns, 1, 2)
            self.__addPawnsOnField(id, i, playerPawns, 12, 5)
            self.__addPawnsOnField(id, i, playerPawns, 17, 3)
            self.__addPawnsOnField(id, i, playerPawns, 19, 5)

    def getFieldById(self, id: int):
        for field in self.fields:
            if id == field.id:
                return field
        return None

    def addField(self, field: Field):
        self.fields.append(field)

    def __addPawnsOnField(self, id, i, playerPawns: Pawns,  fieldFromBegining: int, howManyPawns: int):
        if i+1 == fieldFromBegining:
            field = self.getFieldById(id)
            self.__addPawnsToFieldIfField(field, playerPawns, howManyPawns)

    def __addPawnsToFieldIfField(self, field, pawns: Pawns, quantity: int):
        if not field:
            return
        for i in range(quantity):
            pawn = pawns.getPawnOutOfBoard()
            if pawn:
                field.addPawn(pawn)
