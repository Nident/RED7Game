import random
from src.Player import Player
from src.Card import Card
from random import shuffle

random.seed(10)

cards = Card.all_cards()
shuffle(cards)
cards = cards[:7]
player = Player("ME", cards)


def test_add_to_palette():
    card = Card('blue', 3)
    print(card)
    player.add_to_palette(card)
    assert repr(player.palette) == 'p4 b3'

