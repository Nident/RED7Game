from src.Card import Card
from src.CardList import Hand
from src.palette import Palette


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.palette = Palette([cards[-1]])
        self.hand = Hand(cards[:-1])
    
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


