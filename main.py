import pygame
import pokers
import random

WIDTH = 1000
HEIGHT = 600
TABLEWIDTH = 400
TABLEHEIGHT = 400
CARDSIZE = (50, 75)
GREEN = (0, 100, 0)
RED = (178, 34, 34)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TOP = 100
LEFT = 300
colors = ["spades", "clubs", "hearts", "diamonds"]
faces = ["A", "2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K"]
images = {c + f: pygame.transform.scale(pygame.image.load(f"Cards/{c+f}.png"), CARDSIZE)
          for c in colors for f in faces}
back_image = pygame.transform.scale(
    pygame.image.load(f"Cards/back.png"), CARDSIZE)


def draw_table(window):
    pygame.draw.rect(window, BLACK, pygame.Rect(
        LEFT, TOP-30, TABLEWIDTH, TABLEHEIGHT+60))
    pygame.draw.circle(window, BLACK, (LEFT, TOP + 0.5*TABLEHEIGHT), 230)
    pygame.draw.circle(window, BLACK, (LEFT + TABLEWIDTH,
                       TOP + 0.5*TABLEHEIGHT), 230)

    pygame.draw.rect(window, GREEN, pygame.Rect(
        LEFT, TOP, TABLEWIDTH, TABLEHEIGHT))
    pygame.draw.circle(window, GREEN, (LEFT, TOP + 0.5*TABLEHEIGHT), 200)
    pygame.draw.circle(window, GREEN, (LEFT + TABLEWIDTH,
                       TOP + 0.5*TABLEHEIGHT), 200)


def make_deck():
    deck = []
    for c in colors:
        for f in faces:
            deck.append((c, f))

    return deck


def draw_deck(window, cards):
    for card in cards:
        window.blit(back_image, (750, 150))


def draw_banker(window, cards):
    for i in range(len(cards)):
        card = cards[i]
        if not card.open:
            window.blit(back_image, (350 + 60*i, 150))
        else:
            window.blit(images[card.color+card.face], (350 + 60*i, 150))


def draw_player(window, cards):
    for i in range(len(cards)):
        card = cards[i]
        window.blit(images[card.color+card.face], (350 + 60*i, 350))


def draw_gamestate(window, cardp, cardb, deck):
    draw_deck(window, deck)
    draw_player(window, cardp)
    draw_banker(window, cardb)


def deal(deck, init=False):
    if init:
        pass


def animation(start: tuple, end: tuple, window, clock):
    fps = 60
    xmove = end[0] - start[0]
    ymove = end[1] - start[1]


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Black Jack")
    clock = pygame.time.Clock()
    window.fill(pygame.Color("burlywood"))
    deck = make_deck()
    random.shuffle(deck)
    cardb = []
    cardp = []

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cardb == []:
                    for i in range(2):
                        cardp.append(pokers.Card(deck[0][0], deck[0][1]))
                        cardb.append(pokers.Card(deck[1][0], deck[1][1]))
                        deck.pop(0)
                        deck.pop(0)
                    cardb[0].open = False
                else:
                    cardp.append(pokers.Card(deck[0][0], deck[0][1]))
                    deck.pop(0)
        draw_table(window)
        draw_gamestate(window, cardp, cardb, deck)
        pygame.display.update()


if __name__ == "__main__":
    main()
