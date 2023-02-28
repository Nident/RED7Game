from src.Card import Card
from src.CardList import Hand
from src.palette import Palette
# from src.abstractPlayer import PlayerHuman, PlayerRandom, PlayerMaxMin
# from src.abstractPlayer import PlayerMaxMin
import random


class Player:
    SCORE = 0

    def __init__(self, name: str, for_hand: list[Card], for_palette: list[Card], ai: bool = True, score: int = SCORE):
        self.__name = name
        self.__palette = Palette(for_palette)
        self.__hand = Hand(for_hand)
        # self.__AI = self.set_ai(ai)
        self.__AI = ai
        self.__score = score

    # @staticmethod
    # def set_ai(ai):
    #     cl = [False, PlayerMaxMin]
    #     r = random.randint(0, len(cl) - 1)
    #     return cl[r] if ai else False

    # def choose_turn(self):
    #     return self.ai.choose_turn()

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

    @AI.setter
    def AI(self, a):
        self.__AI = a

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, s: int):
        if type(s) == int:
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
        """ True, if there is no cards in hand. """
        return len(self.hand) == 0

    def add_to_palette(self, card: Card):
        """Play card from hand to palette"""
        card = self.hand.remove(card)
        self.palette.add(card)

    def add_score(self, score: int):
        self.score += score


