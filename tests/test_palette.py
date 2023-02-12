from src.palette import Palette
from src.Card import Card
from src.Player import Player
from src.CardList import Hand


def test_value():
    color = 'green'
    p1 = [Card('orange', 3), Card('yellow', 6), Card('orange', 6)]
    P1 = Palette(p1)
    print(P1.value(color))


def test_value_red():
    # RED
    p1 = [Card('purple', 3), Card('yellow', 1), Card('orange', 6)]

    p2 = [Card('red', 6), Card('yellow', 3), Card('blue', 7)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value_red() for palette in [P1, P2]]
    assert value[0] < value[-1]


def test_value_orange():
    # Orange
    p1 = [Card('purple', 3), Card('yellow', 6), Card('orange', 6)]

    p2 = [Card('red', 3), Card('yellow', 3), Card('blue', 3)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value_orange() for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1]


def test_value_yellow():
    # Yellow
    p1 = [Card('purple', 3), Card('orange', 3), Card('orange', 6)]

    p2 = [Card('purple', 3), Card('purple', 2), Card('blue', 3)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    v = [palette.value_yellow() for palette in [P1, P2]]
    print(v)
    assert v[0] > v[1]


def test_value_green():
    # Yellow
    p1 = [Card('purple', 2), Card('yellow', 3), Card('orange', 5)]

    p2 = [Card('purple', 3), Card('purple', 4), Card('yellow', 4), Card('orange', 6)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value_green() for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1] and value[1][0] == 3


def test_value_lightblue():
    # LightBlue
    p1 = [Card('yellow', 2), Card('yellow', 3), Card('orange', 5)]

    p2 = [Card('purple', 3), Card('purple', 4), Card('yellow', 4), Card('orange', 6)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value_green() for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1] and value[1][0] == 3


def test_value_blue():
    # Blue
    p1 = [Card('yellow', 2), Card('yellow', 3), Card('orange', 5)]

    p2 = [Card('purple', 3), Card('purple', 4), Card('yellow', 5), Card('orange', 6)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value_blue() for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1] and value[1][0] == 4


def test_value_purple():
    # Purple
    p1 = [Card('yellow', 2), Card('yellow', 4), Card('orange', 5)]

    p2 = [Card('purple', 1), Card('purple', 2), Card('yellow', 3), Card('orange', 6)]

    P1 = Palette(p1)
    P2 = Palette(p2)

    value = [palette.value_purple() for palette in [P1, P2]]
    print(value)
    assert value[0] < value[1] and value[1][0] == 3

