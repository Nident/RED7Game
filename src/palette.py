from src.CardList import CardList
from src.Card import Card

# red: старшая карта
# orange: больше всего карт одного номинала.
# yellow: больше всего карт одного цвета.
# green: больше всего чётных карт.
# lightBlue: больше всего карт разных цветов
# blue: больше всего карт, идущих по порядку
# purple: больше всего карт номиналом меньше 4


class Palette(CardList):
    COLORS = ['red', 'orange', 'yellow', 'green', 'lightBlue', 'blue', 'purple']

    def __init__(self, cards):
        super(Palette, self).__init__(cards)
        self.value_function = {
            'red': self.value_red(),
            'orange': self.value_orange(),
            'yellow': self.value_yellow(),
            'green': self.value_green(),
            'lightBlue': self.value_lightblue(),
            'blue': self.value_blue(),
            'purple': self.value_purple()
        }

    def __add__(self, card):
        return Palette(self.cards + [card])

    def value(self, color):
        return self.value_function[color]

    # def new_palette(self, card, color):
    #     new_palette = self.cards.copy()
    #
    #     new_palette.append(card)
    #     value = self.value(color)
    #     new_palette.remove(card)
    #
    #     return value

    def value_red(self) -> int:
        value = 0
        max_card_number = 0
        for card in self.cards:
            if card.number > max_card_number:
                max_card_number = card.number
                tiebreaker_card = card
                value = max_card_number * 100 + tiebreaker_card.tiebreaker()
        return value

    def value_orange(self) -> list:
        nums = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0]}
        for card in self.cards:
            tiebreaker_card = card
            nums[card.number][0] += 1
            nums[card.number][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        value = max(nums.values())
        return value

    def value_yellow(self) -> list:
        nums = {'red': [0, 0], 'orange': [0, 0], 'yellow': [0, 0], 'green': [0, 0],
                'lightBlue': [0, 0], 'blue': [0, 0], 'purple': [0, 0]}
        for card in self.cards:
            tiebreaker_card = card
            nums[card.color][0] += 1
            nums[card.color][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        value = max(nums.values())
        return value

    def value_green(self) -> list:
        nums = {2: [0, 0], 4: [0, 0], 6: [0, 0]}
        for card in self.cards:
            if card.number in nums.keys():
                tiebreaker_card = card
                nums[card.number][0] += 1
                nums[card.number][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        count = sum([a[0] for a in nums.values()])
        score = max([a[1] for a in nums.values()])
        value = [count, score]

        return value

    def value_lightblue(self) -> list:
        nums = {'red': [0, 0], 'orange': [0, 0], 'yellow': [0, 0], 'green': [0, 0],
                'lightBlue': [0, 0], 'blue': [0, 0], 'purple': [0, 0]}
        for card in self.cards:
            tiebreaker_card = card
            nums[card.color][0] = 1
            nums[card.color][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        count = sum([a[0] for a in list(nums.values())])
        score = max([a[1] for a in list(nums.values())])

        value = [count, score]
        return value

    def value_blue(self) -> list:
        sorted_palette = sorted(self.cards, key=lambda x: (x.number, x.color))
        k = 1
        value = 0
        for x in range(1, len(sorted_palette)):
            tiebreaker_card = sorted_palette[x]
            if sorted_palette[x].number - sorted_palette[x - 1].number == 1:
                value = sorted_palette[x].number * 100 + tiebreaker_card.tiebreaker()
                k += 1
            else:
                k = 1

        if len(self.cards) == 1:
            value = self.cards[0].number * 100 + self.cards[0].tiebreaker()
        value = [k, value]
        return value

    def value_purple(self) -> list:
        nums = {1: [0, 0], 2: [0, 0], 3: [0, 0]}
        for card in self.cards:
            if card.number in nums.keys():
                tiebreaker_card = card
                nums[card.number][0] += 1
                nums[card.number][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        count = sum([a[0] for a in nums.values()])
        score = max([a[1] for a in nums.values()])

        value = [count, score]
        return value



