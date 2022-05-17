class Card:
    def __init__(self, color, face, state="open"):
        self.color = color
        self.face = face
        self.open = True if state == "open" else False
        self.busted = False


class Hand:
    def __init__(self, cards: list):
        self.cards = cards
        self.showed = False

    def count(self):
        point = [0, 0]
        for card in self.cards:
            if card.face == "A":
                point[0] += 1
                point[1] += 11
            elif card.face.isnumeric():
                point[0] += int(card.face)
                point[1] += int(card.face)
            else:
                point[0] += 10
                point[1] += 10

        return point

    def showdown(self):
        self.cards[1].open = True
        self.showed = True

    def isblackjack(self):
        if len(self.cards) == 2:
            if 21 in self.count():
                return True
        return False


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, window):
        # draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))

    def act(self, pos, get_pressed):
        action = False
        if self.rect.collidepoint(pos):
            if get_pressed[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if get_pressed[0] == 0:
            self.clicked = True
        return action
