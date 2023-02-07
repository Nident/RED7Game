from src.CardList import CardList
# from src.Card import Card


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

    def red_new_palette(self, card):
        self.cards.append(card)
        value = self.value_red()
        self.cards.remove(card)
        return value

    def value_orange(self) -> list:
        nums = {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0], 6: [0, 0], 7: [0, 0]}
        for card in self.cards:
            tiebreaker_card = card
            nums[card.number][0] += 1
            nums[card.number][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        # print(nums)
        value = max(nums.values())
        return value

    def orange_new_palette(self, card):
        self.cards.append(card)
        value = self.value_orange()
        self.cards.remove(card)
        return value

    def value_yellow(self) -> list:
        nums = {'red': [0, 0], 'orange': [0, 0], 'yellow': [0, 0], 'green': [0, 0],
                'lightBlue': [0, 0], 'blue': [0, 0], 'purple': [0, 0]}

        for card in self.cards:
            tiebreaker_card = card
            nums[card.color][0] += 1
            nums[card.color][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        print(nums)
        value = max(nums.values())
        return value

    def yellow_new_palette(self, card):
        self.cards.append(card)
        value = self.value_yellow()
        self.cards.remove(card)
        return value

    def value_green(self) -> list:
        nums = {2: [0, 0], 4: [0, 0], 6: [0, 0]}
        for card in self.cards:
            if card.number in nums.keys():
                tiebreaker_card = card
                nums[card.number][0] += 1
                nums[card.number][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        print(nums)
        value = max(nums.values())
        return value

    def green_new_palette(self, card):
        self.cards.append(card)
        value = self.value_green()
        self.cards.remove(card)
        return value

    def value_lightblue(self) -> list:
        nums = {'red': [0, 0], 'orange': [0, 0], 'yellow': [0, 0], 'green': [0, 0],
                'lightBlue': [0, 0], 'blue': [0, 0], 'purple': [0, 0]}
        for card in self.cards:
            tiebreaker_card = card
            nums[card.color][0] = 1
            nums[card.color][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        print(nums)

        s = sum([a[0] for a in list(nums.values())])
        m = max([a[1] for a in list(nums.values())])

        value = [s, m]
        return value

    def lightblue_new_palette(self, card):
        self.cards.append(card)
        value = self.value_lightblue()
        self.cards.remove(card)
        return value

    def value_blue(self) -> list:
        sorted_palette = sorted(self.cards, key=lambda x: (x.number, x.color))
        k = 1
        value = 0
        for x in range(1, len(sorted_palette)):
            tiebreaker_card = sorted_palette[x]
            if sorted_palette[x].number - sorted_palette[x-1].number == 1:
                value = sorted_palette[x].number * 100 + tiebreaker_card.tiebreaker()
                k += 1
            else:
                k = 1

        if len(self.cards) == 1:
            value = self.cards[0].number * 100 + self.cards[0].tiebreaker()

        value = [k, value]

        return value

    def blue_new_palette(self, card):
        self.cards.append(card)
        value = self.value_blue()
        self.cards.remove(card)
        return value

    def value_purple(self) -> list:
        nums = {1: [0, 0], 2: [0, 0], 3: [0, 0]}
        for card in self.cards:
            if card.number in nums.keys():
                tiebreaker_card = card
                nums[card.number][0] += 1
                nums[card.number][1] = card.number * 100 + tiebreaker_card.tiebreaker()

        print(nums)
        value = max(nums.values())
        return value

    def purple_new_palette(self, card):
        self.cards.append(card)
        value = self.value_purple()
        self.cards.remove(card)
        return value
