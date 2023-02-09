from src.Card import Card
import random
import itertools


class CardList:

    def __init__(self, cards: list[Card]):
        self.cards = cards

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


# class Heap(CardList):
#     def __init__(self, cards: list[Card]):
#         super(Heap, self).__init__(cards)
#
#     def __str__(self):
#         return str(self.top())
#
#     def top(self) -> Card:
#         """ Верхняя карта """
#         return self.cards[-1]


class Hand(CardList):
    def __init__(self, cards: list[Card]):
        super(Hand, self).__init__(cards)
        self.current_index = 0
        self.class_size = len(self.cards)

    def __iter__(self):
        # self.a = 0
        return iter(self.cards)

    def all_card_pairs(self):
        return list(itertools.combinations([None] + self.cards, 2))

    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    def playable_cards_red(self, max_card: Card) -> list[Card]:
        return [card for card in self.cards if card.playable_red(max_card)]


    # def playable_cards_orange(self, max_number):
    #     return [card for card in self.cards if card.playable_orange(max_number)]
    #
    # def playable_cards_yellow(self, max_color):
    #     return [card for card in self.cards if card.playable_yellow(max_color)]
    #
    # def playable_cards_green(self):
    #     return [card for card in self.cards if card.playable_green()]
    #
    # def playable_cards_lightBlue(self, current_palette):
    #     return [card for card in self.cards if card.playable_lightBlue(current_palette)]
    #
    # def playable_cards_blue(self, current_palette):
    #     return [card for card in self.cards if card.playable_blue(current_palette)]
    #
    # def playable_cards_purple(self):
    #     return [card for card in self.cards if card.playable_purple()]
    #
    # def possible_rules(self):
    #     colors = []
    #     cards = []
    #     for i in self.cards:
    #         if i.color not in colors:
    #             colors.append(i.color)
    #             cards.append(i)
    #
    #     return cards

    def remove(self, card: Card):
        """Возвращает удаленную карту"""
        self.cards.remove(card)
        return card






