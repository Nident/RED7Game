from src.CardList import CardList, Deck, Hand
from src.Card import Card

import random

random.seed(10)

cards = Card.all_cards()
random.shuffle(cards)
cards = cards[:7]


def test_add():
    cl = CardList(cards)
    cl.add(Card('red', 5))
    assert str(cl) == 'y3 l5 b1 b3 y5 b4 p4 r5'

def test_draw():
    pass