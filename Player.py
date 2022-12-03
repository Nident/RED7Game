from Card import Card
from CardList import Hand


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.palette = cards[-1]
        self.hand = Hand(cards[:-1])
        # print(self.hand, 'HAND IN PLAYER')
        # print(self.first_palette_card, 'first_palette_card IN PLAYER')

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

    # def add_card_to_hand(self, card: Card):
    #     self.hand.add(card)


