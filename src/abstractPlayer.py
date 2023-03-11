from src.Player import Player
from src.Card import Card
import random


class PlayerHuman(Player):
    def __init__(self, name, for_hand, for_palette, ai, score=Player.SCORE):
        super(PlayerHuman, self).__init__(name, for_hand, for_palette, ai, score)

    def play_playable_cards(self, playable_cards):
        index = int(input('what to play?: \n'))
        return playable_cards[index - 1]

    def take_card_from_deck(self, from_deck):
        take = input('do you want to take a card from deck?: \n')
        if take in ('y', 'Y'):
            print(f'{self.name} took {from_deck}')
            self.add_to_hand(from_deck)
        else:
            return False


class PlayerRandom(Player):
    def __init__(self, name, for_hand, for_palette, ai, score=Player.SCORE):
        super(PlayerRandom, self).__init__(name, for_hand, for_palette, ai, score)

    def play_playable_cards(self, playable_cards: list):
        index = random.randint(0, len(playable_cards) - 1)
        return playable_cards[index]

    def take_card_from_deck(self, from_deck):
        return False


class PlayerMaxMin(Player):
    def __init__(self, name, for_hand, for_palette, ai, score=Player.SCORE):
        super(PlayerMaxMin, self).__init__(name, for_hand, for_palette, ai, score)

    def play_playable_cards(self, playable_cards: list):
        return self.get_max_value_play(playable_cards)

    def take_card_from_deck(self, from_deck):
        return False

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

