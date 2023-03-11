from src.Card import Card
from src.CardList import Hand
from src.palette import Palette
from abc import ABC, abstractmethod
# import random


class Player(ABC):
    SCORE = 0

    def __init__(self, name: str, for_hand: list[Card], for_palette: list[Card],
                 ai: str = 'random', score: int = SCORE):
        self.__name = name
        self.__palette = Palette(for_palette)
        self.__hand = Hand(for_hand)
        self.__score = score
        self.AI = ai

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
    def score(self):
        return self.__score

    @score.setter
    def score(self, s: int):
        if type(s) == int:
            self.__score = s
        else:
            print('Invalid value')

    @abstractmethod
    def play_playable_cards(self, playable_cards):
        pass

    @abstractmethod
    def take_card_from_deck(self, from_deck):
        pass

    def __repr__(self):
        return f'{self.name}: {self.hand} || {self.palette}'

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': repr(self.hand),
            'palette': repr(self.palette)
        }

    def no_cards(self) -> bool:
        """ True, if there is no cards in hand. """
        return len(self.hand) == 0

    def add_to_palette(self, card: Card):
        """Play card from hand to palette"""
        card = self.hand.remove(card)
        self.palette.add(card)

    def add_to_hand(self, card: Card):
        """Play card from deck to palette"""
        self.hand.add(card)

    def add_score(self, score: int):
        self.score += score

