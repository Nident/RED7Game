from src.Card import Card
import random
import itertools


class CardList:

    def __init__(self, cards: list[Card]):
        self.__cards = cards

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards: list[Card]):
        self.__cards = cards

    def __repr__(self):
        return ' '.join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def add(self, card: Card):
        """ Добавить карту в КОНЕЦ списка. """
        self.cards.append(card)


class Deck(CardList):
    def __init__(self, cards: list[Card]):
        super(Deck, self).__init__(cards)

    def draw(self) -> Card:
        """ Взять 1 карту"""
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card

    def shuffle(self):
        random.seed(2)
        random.shuffle(self.cards)

    def __repr__(self):
        return f'{self.cards}'


class Hand(CardList):
    def __init__(self, cards: list[Card]):
        super(Hand, self).__init__(cards)
        self.current_index = 0
        self.class_size = len(self.cards)

    def __iter__(self):
        # self.a = 0
        return iter(self.cards)

    def all_card_pairs(self) -> list:
        return list(itertools.combinations([None] + self.cards, 2))

    # def playable_cards_red(self, max_card: Card) -> list[Card]:
    #     return [card for card in self.cards if card.playable_red(max_card)]

    def remove(self, card: Card) -> Card:
        """Возвращает удаленную карту"""
        self.cards.remove(card)
        return card






