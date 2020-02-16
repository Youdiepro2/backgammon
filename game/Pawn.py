class Pawn():
    id = None
    fieldId = None
    color = None

    def __init__(self, id, color):
        self.id = id
        self.color = color

    def __del__(self):
        del self
