from game.Pawns import Pawns
from game.Constants import DIRECTION_BLACK, DIRECTION_WHITE, COLOR_BLACK, COLOR_WHITE, PLAYER_HOME_BLACK, PLAYER_HOME_WHITE

class Player():
    direction = None
    color = None
    home = None
    pawns = None
    bar = None

    def __init__(self, direction, color, home):
        self.direction = direction
        self.color = color
        self.home = home
        self.pawns = Pawns()
        self.bar = 0 if direction == 1 else 25

    def getOppositeBarId(self):
        return 0 if self.bar == 25 else 25

    def getPawnsFromBar(self):
        pawns = Pawns()
        for pawn in self.pawns:
            if pawn.fieldId in (0, 25):
                pawns.append(pawn)
        return pawns

    @staticmethod
    def createBlackPlayer():
        return Player(DIRECTION_BLACK, COLOR_BLACK, PLAYER_HOME_BLACK)

    @staticmethod
    def createWhitePlayer():
        return Player(DIRECTION_WHITE, COLOR_WHITE, PLAYER_HOME_WHITE)
