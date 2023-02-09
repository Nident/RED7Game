from src.palette import Palette
from src.Card import Card
from src.Player import Player
from src.CardList import Hand


def test_value():
    p1 = [Card('orange', 3), Card('yellow', 6), Card('orange', 6)]
    P1 = Palette(p1)
    print(P1.value('green'))


def test_value_red():
    # RED
    p1 = [Card('purple', 3), Card('yellow', 1), Card('orange', 6)]

    p2 = [Card('red', 2), Card('yellow', 3)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value('red') for palette in [P1, P2]]
    assert value[0] == 606 and value[-1] == 305


def test_value_orange():
    # Orange
    p1 = [Card('purple', 3), Card('yellow', 1), Card('orange', 6)]

    p2 = [Card('red', 3), Card('yellow', 3)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value('orange') for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1] and value[1][0] == 2


def test_value_yellow():
    # Yellow
    p1 = [Card('purple', 3), Card('yellow', 3), Card('orange', 6)]

    p2 = [Card('purple', 3), Card('purple', 2)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    v = [palette.value('yellow') for palette in [P1, P2]]
    print(v)
    assert v[0] < v[1] and v[1][0] == 2


def test_value_green():
    # Yellow
    p1 = [Card('purple', 2), Card('yellow', 3), Card('orange', 5)]

    p2 = [Card('purple', 3), Card('purple', 4), Card('yellow', 4), Card('orange', 6)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value('green') for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1]


def test_players_value():
    py1 = Player('alesh', [Card('red', 4), Card('lightBlue', 7)])
    py2 = Player('tim', [Card('red', 7)])
    py3 = Player('kus', [Card('green', 2)])
    players = [py1, py2, py3]
    value = [player.palette.value('red') for player in players]
    # max_value = max(value)
    print(value)
