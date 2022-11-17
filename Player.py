
class Player:
    def __init__(self, name, hand_deck):
        self.name = name
        self.hand_deck = hand_deck

    def __repr__(self):
        return f"Player name: {self.name},\n Player hand: {self.hand_deck}"


