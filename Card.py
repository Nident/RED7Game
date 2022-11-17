
class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num

    def __repr__(self):
        return f"{self.color}, {self.num}"

    def __str__(self):
        return f'{self.color[0] + str(self.num)}'


