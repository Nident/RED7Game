from src.Card import Card
from src.abstractPlayer import PlayerMaxMin
from random import shuffle

cards = Card.all_cards()
shuffle(cards)

hand = cards[:7]
palette = [cards[8]]  # p2

player = PlayerMaxMin("ME", hand, palette)

pc = [(None, Card('red', 7)), (None, Card('green', 6)),
      (Card('blue', 5), Card('red', 2)), (Card('purple', 5), Card('red', 2))]


pc1 = [(None, Card('red', 7)), (None, Card('green', 6)),
       (Card('blue', 5), Card('red', 7)), (Card('purple', 5), Card('red', 2))]


def test_possible_plays():
    print(player.play_playable_cards(pc))
    assert 1 == 1


def test_get_max_value_play():
    # print(pc)
    res1 = player.get_max_value_play(pc1)
    assert res1 == (Card.create('b5'), Card.create('r7'))
