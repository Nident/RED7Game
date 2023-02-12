import random
from src.Player import Player
from src.Card import Card
from random import shuffle

random.seed(10)

cards = Card.all_cards()
shuffle(cards)

hand = cards[:7]
palette = [cards[8]]  # p2

player = Player("ME", hand, palette)


def test_save():
    a = player.save()
    assert repr(a['hand']) == hand


def test_no_cards():
    a = player.no_cards()
    assert a == False


def test_add_to_palette():
    card = Card('blue', 3)
    print(card)
    player.add_to_palette(card)
    assert repr(player.palette) == 'p2 b3'

