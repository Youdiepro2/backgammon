class Move():
    fieldId = None
    pawnId = None

    def __init__(self, fieldId: int, pawnId: int):
        self.fieldId = fieldId
        self.pawnId = pawnId
