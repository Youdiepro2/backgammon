from game.Pawn import Pawn
from game.Constants import COLOR_BLACK, COLOR_WHITE

class Pawns():
    pawns = []

    def __init__(self):
        self.pawns = []

    def __iter__(self):
        return iter(self.pawns)

    def __len__(self):
        return len(self.pawns)

    def removePawnById(self, pawnId):
        for pawn in self.pawns: #range(len(self.pawns)-1):
            # pawn = self.pawns[i];
            if pawn.id == pawnId:
                del pawn

    def getPawnById(self, id: int):
        for pawn in self.pawns:
            if pawn.id == id:
                return pawn
        return None

    def pop(self):
        self.pawns.pop()

    def countPawnsInColor(self, color: str)-> int:
        count = 0;
        for pawn in self.pawns:
            if color == pawn.color:
                count+=1
        return count

    def getLastPawnInList(self):
        lastIndex = len(self.pawns)-1
        if lastIndex < 0:
            return None
        return self.pawns[lastIndex]

    def append(self, pawn: Pawn):
        self.pawns.append(pawn)

    def getFieldIds(self)-> list:
        ids = []
        for pawn in self.pawns:
            if pawn.fieldId not in ids:
                ids.append(pawn.fieldId)
        return ids

    def getPawnOutOfBoard(self):
        for pawn in self.pawns:
            if pawn.fieldId is None \
            or (pawn.fieldId < 1 or pawn.fieldId > 24):
                return pawn
        return None

    def getPawnsForPlayer(self, player):
        pawns = Pawns()
        for pawn in self.pawns:
            if pawn.color == player.color:
                pawns.append(pawn)
        return pawns

    @staticmethod
    def createInitial():
        pawns = Pawns()
        for i in range(30):
            id = i+1;
            color = COLOR_BLACK if i< 15 else COLOR_WHITE
            pawns.pawns.append(Pawn(id, color))
        return pawns
