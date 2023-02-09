from src.palette import Palette
from src.Card import Card



def test_value_red():
    P1 = Palette([Card('red', 5)])
    P2 = Palette([Card('lightBlue', 6)])
    P3 = Palette([Card('red', 4), Card('lightBlue', 7)])
    assert (P3.value('red') == P2.value('red'))

