class Card:
    def __init__(self, color, face, state="open"):
        self.color = color
        self.face = face
        self.open = True if state == "open" else False