import numpy as np


class CardDeck:

    def __init__(self, colors, numbers):
        self.color_stack = colors
        self.numbers_stack = numbers
        self.card_deck = np.array([])

    def deck_shuffle(self):
        np.random.seed(1)
        for i in self.color_stack:
            for j in self.numbers_stack:
                self.card_deck = np.append(self.card_deck, i + str(j))
        np.random.shuffle(self.card_deck)

        return self.card_deck

    def card_deal(self):
        deal = self.card_deck[:7]
        self.card_deck = self.card_deck[7:]
        return deal

    def __repr__(self):
        return f"{self.card_deck}"


