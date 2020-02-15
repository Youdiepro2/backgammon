from flask import request

class Move():
    fieldId = None
    pawnId = None
    diceResult = None

    def __init__(self, fieldId: int, pawnId: int, diceResult: int):
        self.fieldId = fieldId
        self.pawnId = pawnId
        self.diceResult = diceResult

    def __eq__(self, move):
        return self.fieldId == move.fieldId \
         and self.pawnId == move.pawnId \
         and self.diceResult == move.diceResult

    @staticmethod
    def fromRequest(request: request):
        fieldId = request.get('fieldId')
        pawnId = request.get('pawnId')
        diceResult = request.get('diceResult')
        if not (fieldId or pawnId or diceResult):
            return None

        return Move(fieldId, pawnId, diceResult)
