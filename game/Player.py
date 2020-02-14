from game.Pawns import Pawns
from game.Constants import DIRECTION_BLACK, DIRECTION_WHITE, COLOR_BLACK, COLOR_WHITE, PLAYER_HOME_BLACK, PLAYER_HOME_WHITE

class Player():
    direction = None
    color = None
    home = None
    pawns = None
    allPawnsInHome = False
    hasPawnInBar = False

    def __init__(self, direction, color, home):
        self.direction = direction
        self.color = color
        self.home = home
        self.allPawnsInHome = False
        self.hasPawnInBar = False
        self.pawns = Pawns()

    @staticmethod
    def createBlackPlayer():
        return Player(DIRECTION_BLACK, COLOR_BLACK, PLAYER_HOME_BLACK)

    @staticmethod
    def createWhitePlayer():
        return Player(DIRECTION_WHITE, COLOR_WHITE, PLAYER_HOME_WHITE)
