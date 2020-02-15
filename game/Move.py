from flask import request

class Move():
    fieldId = None
    pawnId = None

    def __init__(self, fieldId: int, pawnId: int):
        self.fieldId = fieldId
        self.pawnId = pawnId

    @staticmethod
    def fromRequest(request: request):
        return Move(request.get('fieldId'), request.get('pawnId'))
