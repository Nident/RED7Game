
class Card:
    COLORS = ['red', 'orange', 'yellow', 'green', 'lightBlue', 'blue', 'purple']
    NUMBERS = list(range(1, 8))

    # COLORSnRULES = [('red', 'старшая карта'), ('orange', 'больше всего карт одного номинала'),
    #                 ('yellow', 'больше всего карт одного цвета'), ('green', 'больше всего чтных карт'),
    #                 ('lightBlue', ' больше всего карт разных цветов'),
    #                 ('blue', ' больше всего карт, идущих по порядку'),
    #                 ('purple', 'больше всего карт номиналом меньше 4')]

    SHORT_FORM = {color[0]: color for color in COLORS}

    def __init__(self, color: str, number: int):
        if color not in Card.COLORS:
            raise ValueError(f'Invalid color <{color}>')
        if number not in Card.NUMBERS and number != 0:
            raise ValueError(f'Invalid number <{number}>')

        self.color = color
        self.number = number

    def __repr__(self):
        """Возвращает сроку вида r3"""
        return f"{self.color[0]}{self.number}"

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number

    def tiebreaker(self):
        return abs(7 - self.COLORS.index(self.color))

    # def playable_red(self, max_card) -> bool:
    #     """ Возвращает True, если self можно сыграть по правилу. """
    #     if self.number > max_card.number:
    #         return max_card
    #     elif self.number == max_card.number and Card.COLORS.index(self.color) < Card.COLORS.index(max_card.color):
    #         return max_card
    #
    # def playable_orange(self, max_number):
    #     return self.number == max_number
    #
    # def playable_yellow(self, max_color):
    #     return self.color == max_color
    #
    # def playable_green(self):
    #     return self.number % 2 == 0
    #
    # def playable_lightBlue(self, current_palette):
    #     return self.number not in current_palette
    #
    # def playable_blue(self, current_palette):
    #     return abs(self.number - current_palette) == 1
    #
    # def playable_purple(self):
    #     return self.number < 4

    @staticmethod
    def create(short_form: str):
        """ Из строки 'r3' делает карту Card('red', 3) """
        color_letter = short_form[0]
        number = int(short_form[1])
        return Card(Card.SHORT_FORM[color_letter], number)

    @staticmethod
    def list_from_str(text: str):
        """ Из строки 'r3 y5 g0' делает [Card('red', 3), Card('yellow', 5), Card('green', 0)] """
        return [Card.create(s) for s in text.split()]

    @classmethod
    def all_cards(cls, colors=COLORS, numbers=NUMBERS):
        return [Card(color, number) for color in colors for number in numbers]

    @staticmethod
    def max_card(cards):
        max_card = Card('purple', 1)
        for i in cards:
            if max_card.number < i.number:
                max_card = i
            elif max_card.number == i.number:
                if Card.COLORS.index(max_card.color) > Card.COLORS.index(i.color):
                    max_card = i
        return max_card
