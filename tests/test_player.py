import random
from RED7.Player import Player
from RED7.Card import Card
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

