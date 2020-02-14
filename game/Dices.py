from random import randrange

class Dices():
    results = []

    def __init__(self):
        self.results = []

    def roll(self):
        self.results = [randrange(1,6), randrange(1,6)]
        return self.results
