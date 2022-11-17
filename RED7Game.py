import numpy as np
from CardDeck import CardDeck
from Player import Player


class RED7GAME:
    COLORS_STACK = np.array(['red', 'orange', 'yellow', 'green', 'lightBlue', 'blue', 'purple'])
    NUMBERS_STACK = np.array([1, 2, 3, 4, 5, 6, 7])
    DEFAULT_PLAYER_DECK_SIZE = 7
    DEFAULT_PLAYERS_NAMES = np.array(['ME'])
    PLAY_WITH_AI = 0

    def __init__(self, count=len(DEFAULT_PLAYERS_NAMES), colors_stack=COLORS_STACK, numbers_stack=NUMBERS_STACK,
                 players_names=DEFAULT_PLAYERS_NAMES, play_with_ai=PLAY_WITH_AI):

        self.game_deck = CardDeck(colors_stack, numbers_stack)
        self.game_deck.deck_shuffle()

        self.players_count = count
        self.players_decks = []
        self.players_stack = []

        self.play_with_AI = 1 if self.players_count == 1 else play_with_ai
        self.players_name_stack = np.append(['AI'], players_names) if self.play_with_AI == 1 \
            else np.array([players_names])

        self.cycle = self.players_count + self.play_with_AI

    def players_decks_filling(self):
        for i in range(self.cycle):
            one_player_deck = self.game_deck.card_deal()
            self.players_decks.append(one_player_deck)

        return self.players_decks

    def players_creation(self):
        # return (self.players_name_stack)
        # return self.cycle
        # return self.players_decks
        self.players_decks_filling()
        for i in range(self.cycle):
            player = Player(self.players_name_stack[i], self.players_decks[i])
            self.players_stack.append(player)
        return self.players_stack


game = RED7GAME()
print(game.players_creation())
# print(game.players_decks_filling()[1])
        # for i in self.players_count:
        #     player = Player(self.name_stack[i], self.)



