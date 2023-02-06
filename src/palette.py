from src.CardList import CardList


class Palette(CardList):
    COLORS = ['red', 'orange', 'yellow', 'green', 'lightBlue', 'blue', 'purple']

    def __init__(self, cards):
        super(Palette, self).__init__(cards)

    def value_red(self) -> int:
        value = 0
        max_card_number = 0
        for card in self.cards:
            if card.number > max_card_number:
                max_card_number = card.number
                tiebreaker_card = card
                value = max_card_number * 100 + tiebreaker_card.tiebreaker()
        return value

    def new_palette(self, card):
        self.cards.append(card)
        value = self.value_red()
        self.cards.remove(card)
        return value



