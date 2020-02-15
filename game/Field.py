from game.Pawns import Pawns
from game.Pawn import Pawn
from game.Constants import GET_OPPOSITE_COLOR

class Field():
    id = None
    pawns = None

    def __init__(self, id):
        self.id = id
        self.pawns = Pawns()

    def addPawn(self, pawn: Pawn):
        pawn.fieldId = self.id
        self.pawns.append(pawn)

    def getPawnOnTop(self):
        return self.pawns.getLastPawnInList()

    def removePawnFromTop(self):
        self.pawns.pop()

    def accepts(self, pawn: Pawn)-> bool:
        color = GET_OPPOSITE_COLOR(pawn.color)
        return 2 > self.pawns.countPawnsInColor(color)
    # @staticmethod
    # def isValidFieldId(id: int)-> bool:
    #     return id >=1 and id <=24
