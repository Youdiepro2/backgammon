from random import randrange

class Dices():
    results = []

    def __init__(self):
        self.results = []

    def roll(self):
        self.results = [randrange(1,6), randrange(1,6)]
        self.handleDubletWasThrown()
        return self.results

    def removeResult(self, result: int):
        for number in self.results:
            if number == result:
                self.results.remove(number)
                return

    def handleDubletWasThrown(self)-> bool:
        if len(self.results) == 2 and self.results[0] == self.results[1]:
            result = self.results[0]
            self.results = [result for i in range(4)]
