from src.Player import Player
import random


class PlayerHuman(Player):
    def __init__(self, name, for_hand, for_palette):
        super(PlayerHuman, self).__init__(name, for_hand, for_palette)

    @staticmethod
    def play_playable_cards(playable_cards: list[tuple]):
        index = int(input('what to play?: \n'))
        return playable_cards[index-1]


class PlayerRandom(Player):
    def __init__(self, name, for_hand, for_palette):
        super(PlayerRandom, self).__init__(name, for_hand, for_palette)

    @staticmethod
    def play_playable_cards(playable_cards):
        index = random.randint(0, len(playable_cards) - 1)
        return playable_cards[index]


class PlayerMaxMin(Player):
    def __init__(self, name, for_hand, for_palette):
        super(PlayerMaxMin, self).__init__(name, for_hand, for_palette)

    def play_playable_cards(self, playable_cards):
        return self.get_max_value_play(playable_cards)

    def get_max_value_play(self, playable_cards):
        playable_cards = sorted(playable_cards, key=self.sort_plays, reverse=True)
        return playable_cards[0]

    @staticmethod
    def sort_plays(tup):
        # lambda x: (x[1].number, x[1].color)
        x = (tup[1].number, tup[1].tiebreaker())
        if tup[0] is not None:
            y = (tup[0].number, tup[0].tiebreaker())
        else:
            y = (0, 0)

        return x, y
