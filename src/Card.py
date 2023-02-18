
class Card:
    COLORS = ['red', 'orange', 'yellow', 'green', 'lightBlue', 'blue', 'purple']
    NUMBERS = list(range(1, 8))
    SHORT_FORM = {color[0]: color for color in COLORS}

    def __init__(self, color: str, number: int):
        if color not in Card.COLORS:
            raise ValueError(f'Invalid color <{color}>')
        if number not in Card.NUMBERS and number != 0:
            raise ValueError(f'Invalid number <{number}>')

        self.__color = color
        self.__number = number

    @property
    def color(self):
        return self.__color

    @property
    def number(self):
        return self.__number

    def __repr__(self):
        """Returns string as r3"""
        return f"{self.color[0]}{self.number}"

    def __eq__(self, other):
        return self.color == other.color and self.number == other.number

    def tiebreaker(self):
        return abs(7 - self.COLORS.index(self.color))

    @staticmethod
    def create(short_form: str):
        """ From string 'r3' makes Card('red', 3) """
        color_letter = short_form[0]
        number = int(short_form[1])
        return Card(Card.SHORT_FORM[color_letter], number)

    @staticmethod
    def list_from_str(text: str):
        """ From string 'r3 y5 g0' makes [Card('red', 3), Card('yellow', 5), Card('green', 0)] """
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
