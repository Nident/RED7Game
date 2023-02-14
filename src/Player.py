from src.Card import Card
from src.CardList import Hand
from src.palette import Palette


class Player:
    SCORE = 0

    def __init__(self, name: str, for_hand: list[Card], for_palette: list[Card], ai: bool, score: int = SCORE):
        self.__name = name
        self.__palette = Palette(for_palette)
        self.__hand = Hand(for_hand)
        self.__AI = ai
        self.__score = score

    @property
    def name(self):
        return self.__name

    @property
    def palette(self):
        return self.__palette

    @property
    def hand(self):
        return self.__hand

    @property
    def AI(self):
        return self.__AI

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, s: int):
        if s is int:
            self.__score = s
        else:
            print('Invalid value')

    def __repr__(self):
        return f'{self.name}: {self.hand} || {self.palette}'

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': repr(self.hand),
            'palette': repr(self.palette)
        }

    def no_cards(self) -> bool:
        """ True, если в руке нет карт. """
        return len(self.hand) == 0

    def add_to_palette(self, card: Card):
        """Играем карту с руки в палитру"""
        card = self.hand.remove(card)
        self.palette.add(card)


