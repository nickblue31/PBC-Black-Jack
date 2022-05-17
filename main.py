import pygame
import pokers
import random

# 定義基本全域變數
WIDTH = 1200
HEIGHT = 650
TABLEWIDTH = 400
TABLEHEIGHT = 400
CARDSIZE = (50, 75)
GREEN = (0, 100, 0)
RED = (178, 34, 34)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TOP = 200
LEFT = 500

# 牌的花色與牌面數字
colors = ["spades", "clubs", "hearts", "diamonds"]
faces = ["A", "2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K"]
pygame.font.init()
font = pygame.font.SysFont("consolas", 32)
chinese_font = pygame.font.Font("C:\Windows\Fonts\msjhbd.ttc", 48)
# 將cards資料夾中的圖片以字典形式儲存
images = {c + f: pygame.transform.scale(pygame.image.load(f"Cards/{c+f}.png"), CARDSIZE)
          for c in colors for f in faces}
back_image = pygame.transform.scale(
    pygame.image.load(f"Cards/back.png"), CARDSIZE)

hitimg = pygame.image.load("buttons\hitbutton.png")
standimg = pygame.image.load("buttons\standbutton.png")
backimg = pygame.image.load("buttons\\backbutton.png")
quitimg = pygame.image.load("buttons\quitbutton.png")
cheatimg = pygame.image.load("buttons\cheatbutton.png")
dealers = ["wu_suit", "yonghammer", "nicklunblue",
           "4j_police", "smoking_monkey", "polun_cry", "chika"]
dealerimgs = [pygame.transform.scale(pygame.image.load(
    f"dealers\{d}.png"), (200, 200)) for d in dealers]


def draw_table(window):
    """畫出遊戲背景的賭桌"""
    # 以矩形和兩個半圓畫出內圈的綠色桌面
    pygame.draw.rect(window, BLACK, pygame.Rect(
        LEFT, TOP-60, TABLEWIDTH, TABLEHEIGHT+60))
    pygame.draw.circle(window, BLACK, (LEFT, TOP + 0.5*TABLEHEIGHT-30), 230)
    pygame.draw.circle(window, BLACK, (LEFT + TABLEWIDTH,
                       TOP + 0.5*TABLEHEIGHT-30), 230)

    # 同樣的方式畫出黑色的賭桌外框
    pygame.draw.rect(window, GREEN, pygame.Rect(
        LEFT, TOP-30, TABLEWIDTH, TABLEHEIGHT))
    pygame.draw.circle(window, GREEN, (LEFT, TOP + 0.5*TABLEHEIGHT-30), 200)
    pygame.draw.circle(window, GREEN, (LEFT + TABLEWIDTH,
                       TOP + 0.5*TABLEHEIGHT-30), 200)


def make_deck():
    """產出遊戲需要的牌堆"""
    deck = []
    for c in colors:
        for f in faces:
            deck.append((c, f))

    return deck


def draw_deck(window, cards):
    """將牌堆中的牌以背面向上置於牌桌上"""
    for card in cards:
        window.blit(back_image, (900, 220))


def draw_banker(window, cards):
    """顯示莊家的牌面並且將第一張牌覆蓋"""
    for i in range(len(cards)):
        card = cards[i]
        if not card.open:
            window.blit(back_image, (550 + 60*i, 220))
        else:
            window.blit(images[card.color+card.face], (550 + 60*i, 220))


def draw_player(window, cards):
    """顯示莊家的牌面"""
    for i in range(len(cards)):
        card = cards[i]
        window.blit(images[card.color+card.face], (550 + 60*i, 420))


def draw_points(window, cardp, cardb):
    bankerpt = cardb.count()
    if cardb.showed:
        if bankerpt[-1] > 21:
            if bankerpt[0] > 21:
                bankerpt = "Busted"
            else:
                bankerpt = str(bankerpt[0])
            bankerpt = font.render(bankerpt, True, WHITE)

        else:
            bankerpt = list(map(str, set(bankerpt)))
            bankerpt = font.render("/".join(bankerpt), True, WHITE)
        window.blit(bankerpt, (WIDTH/2+100, HEIGHT/2-150))

    playerpt = cardp.count()
    if playerpt[-1] > 21:
        if playerpt[0] > 21:
            playerpt = "Busted"
        else:
            playerpt = str(playerpt[0])
        playerpt = font.render(playerpt, True, WHITE)

    else:
        playerpt = list(map(str, set(playerpt)))
        playerpt = font.render("/".join(playerpt), True, WHITE)
    window.blit(playerpt, (WIDTH/2+100, HEIGHT/2+200))


def draw_gamestate(window, cardp, cardb, deck):
    """顯示當前賭桌上的所有牌以及點數"""
    draw_deck(window, deck)
    draw_player(window, cardp.cards)
    draw_banker(window, cardb.cards)
    draw_points(window, cardp, cardb)


def initialize(deck, cardp, cardb):
    for i in range(2):
        cardp.cards.append(
            pokers.Card(deck[0][0], deck[0][1]))
        cardb.cards.append(
            pokers.Card(deck[1][0], deck[1][1]))
        deck.pop(0)
        deck.pop(0)
    cardb.cards[1].open = False


def deal(deck, cards):
    cards.cards.append(pokers.Card(deck[0][0], deck[0][1]))
    deck.pop(0)


def animation(start: tuple, end: tuple, window, clock):
    # to be finished
    fps = 60
    xmove = end[0] - start[0]
    ymove = end[1] - start[1]


def main():
    """遊戲主程式"""
    # 建立pygame遊戲視窗
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Black Jack")
    clock = pygame.time.Clock()
    dealer = menu()
    window.fill(pygame.Color("burlywood"))

    # 建立全新的牌堆並洗牌
    deck = make_deck()
    random.shuffle(deck)

    hitbutton = pokers.Button(50, 120, hitimg)
    hitbutton.draw(window)

    standbutton = pokers.Button(50, 220, standimg)
    standbutton.draw(window)

    backbutton = pokers.Button(50, 20, backimg)
    backbutton.draw(window)

    quitbutton = pokers.Button(50, HEIGHT-80, quitimg)
    quitbutton.draw(window)

    cheatbutton = pokers.Button(50, 320, cheatimg)
    cheatbutton.draw(window)
    if dealer != None:
        window.blit(dealer, (600, 0))
    else:
        return 0

    # 定義兩空串列用以儲存莊家與玩家的牌
    cardb = pokers.Hand([])
    cardp = pokers.Hand([])

    players_turn = True
    get_caught = False
    run = True
    leave = False
    while run:
        if cardb.cards == []:
            initialize(deck, cardp, cardb)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                leave = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pressed = pygame.mouse.get_pressed()
                # 發牌(暫時測試用)
                if hitbutton.act(pos, pressed):
                    if players_turn:
                        deal(deck, cardp)
                        hitbutton.clicked = False
                elif standbutton.act(pos, pressed):
                    if players_turn:
                        players_turn = False
                elif backbutton.act(pos, pressed):
                    run = False
                elif quitbutton.act(pos, pressed):
                    run = False
                    leave = True
                elif cheatbutton.act(pos, pressed):
                    if players_turn:
                        for card in deck:
                            point = pokers.Hand(
                                [pokers.Card(card[0], card[1])])
                            if point.count()[0] + cardp.count()[1] == 21:
                                cardp.cards.append(
                                    pokers.Card(card[0], card[1]))
                                players_turn = False
                        get_caught = random.choices(
                            [True, False], weights=[0.8, 0.2])[0]

        playerpt = cardp.count()
        bankerpt = cardb.count()

        if all(p > 21 for p in playerpt):
            players_turn = False

        if not players_turn:
            if not cardb.showed:
                cardb.showdown()
            while any(p < 17 for p in bankerpt):

                deal(deck, cardb)
                bankerpt = cardb.count()

        # 更新賭桌桌面
        draw_table(window)
        draw_gamestate(window, cardp, cardb, deck)
        if get_caught:
            window.fill(BLACK)
            window.blit(dealerimgs[3], (WIDTH/2-100, HEIGHT/2-200))
            msg = chinese_font.render("黃警官已介入調查", True, WHITE)
            window.blit(msg, ((WIDTH-msg.get_width())/2, HEIGHT/2))
            backbutton.draw(window)
        pygame.display.update()
    if not leave:
        main()


def menu():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(BLACK)
    msg = font.render("Choose a dealer you want to play with.", True, WHITE)
    window.blit(msg, ((WIDTH-msg.get_width())/2, 20))
    run = True
    dealer_btns = []
    for i in range(len(dealerimgs)):
        dealer_btns.append(pokers.Button(
            i % 4 * 300+100, (i//4) * 250+100, dealerimgs[i]))

    for dealer in dealer_btns:
        dealer.draw(window)
        pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for dealer in dealer_btns:
                    if dealer.act(pos, pygame.mouse.get_pressed()):

                        return dealer.image


if __name__ == "__main__":
    main()
