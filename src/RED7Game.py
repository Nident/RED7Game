import random
from src.CardList import Deck
from src.Player import Player
from src.Card import Card

random.seed(10)


class RED7GAME:

    HAND_SIZE = 7

    def __init__(self):
        self.__deck: Deck = Deck([])    # deck
        self.__players: list = []    # players
        self.__player_index: int = -1    # current player index
        self.__central_card: Card = Card('red', 0)  # played rule
        self.__advanced: bool = False  # game mode
        self.__round: int = 1  # rounds
        self.__game_over: bool = False  #
        self.__lost_players: list = []

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, d: Deck):
        self.__deck = d

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, p: Player):
        self.__players = p

    @property
    def player_index(self):
        return self.__player_index

    @player_index.setter
    def player_index(self, i: int):
        self.__player_index = i

    @property
    def central_card(self):
        return self.__central_card

    @central_card.setter
    def central_card(self, card: Card):
        self.__central_card = card

    @property
    def advanced(self):
        return self.__advanced

    @advanced.setter
    def advanced(self, a: bool):
        self.__advanced = a

    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, r: int):
        if r not in list(range(0, 20)):
            print('Invalid value')
        else:
            self.__round = r

    @property
    def game_over(self):
        return self.__game_over

    @game_over.setter
    def game_over(self, g: bool):
        self.__game_over = g

    @property
    def lost_players(self):
        return self.__lost_players

    @lost_players.setter
    def lost_players(self, lp: list):
        self.__lost_players = lp

    @staticmethod
    def create(advanced, name_list: list[tuple[str, bool]], cards: list[Card] | None = None):
        """Create game"""
        game = RED7GAME()
        if cards is None:
            game.deck = Deck(Card.all_cards())  # Create deck
            game.deck.shuffle()
        else:
            game.deck = Deck(cards)

        game.players = [Player(name, [game.deck.draw() for _ in range(RED7GAME.HAND_SIZE - 1)],
                               [game.deck.draw()], ai) for name, ai in name_list]
        game.player_index = 0
        game.advanced = advanced

        return game

    @staticmethod
    def load(state: dict):
        """Load game"""
        game = RED7GAME()
        game.deck = Deck(Card.list_from_str(state['deck']))

        game.players = [Player(p['name'], Card.list_from_str(p['hand']),
                               Card.list_from_str(p['palette']), p['ai'], p['score']) for p in state['players']]

        game.player_index = state['player_index']
        game.central_card = state['central_card']
        game.round = state['round']
        return game

    @staticmethod
    def next_round(new_game_state: dict):
        """Create next round with saved last round data"""
        game = RED7GAME()
        game.deck = Deck(Card.all_cards())  # Создаем колоду
        game.deck.shuffle()

        game.players = [Player(p['name'], [game.deck.draw() for _ in range(RED7GAME.HAND_SIZE - 1)],
                               [game.deck.draw()], p['ai'], p['score'])
                        for p in new_game_state['lost_players'] + new_game_state['players']]

        game.player_index = 0
        game.advanced = new_game_state['advanced']
        game.game_over = new_game_state['game_over']

        return game

    def save(self) -> dict:
        """Save game"""
        save_dict = {
            'deck': self.deck,
            'players': [
                {
                    'name': player.name,
                    'ai': player.AI,
                    'hand': player.hand,
                    'palette': player.palette,
                    'score': player.score
                }
                for player in self.players
            ],
            'player_index': self.player_index,
            'central_card': self.central_card,
            'round': self.round,
            'advanced': self.advanced,
            'lost_players': [
                {
                    'name': player.name,
                    'ai': player.AI,
                    'hand': player.hand,
                    'palette': player.palette,
                    'score': player.score
                }
                for player in self.lost_players
            ],
            'game_over': self.game_over
        }

        return save_dict

    def run(self):
        is_running = True
        if self.advanced:
            while is_running:
                is_running = self.turn()
            self.add_scores()   # count scores
            self.save()   # make game save
            self.game_over = self.final_score()

        else:
            while is_running:
                is_running = self.turn()

        self.player_index = 0
        self.congratulation_winner()

    def turn(self) -> bool:
        """ Returns False, if the game over. """
        # print(self.central_card.color)

        current_player = self.current_player()  # игрок чей сейчас ход

        possible_plays = self.get_possible_plays(self.central_card)
        playable_cards = self.get_playable_cards(possible_plays)

        # print(playable_cards, 'it could be played')

        # if there are cards to play
        if len(playable_cards):
            if current_player.AI:
                r = random.randint(0, len(playable_cards)-1)
                in_center, in_palette = playable_cards[r]  # take any cards
            else:
                index = int(input('What to play?: \n'))
                in_center, in_palette = playable_cards[index-1]

            print(f'{current_player.name}: plays {in_center, in_palette}')

            # take_one = False
            # if in_center is not None:
            #     take_one = True if in_center.number > len(current_player.palette) else False
            #     self.central_card = in_center
            # if take_one:
            #     new_card = self.deck.draw()
            #     current_player.hand.add(new_card)

            current_player.add_to_palette(in_palette)

        else:
            # if there are no cards
            print(f'{current_player.name}: Retires')
            self.player_remove(current_player)
            self.player_index -= 1
            if len(self.players) == 1:
                return False

        # after drawing print player and divider
        print(current_player)
        print('-' * 20)

        # if there are no cards in someone's hand game is over
        if current_player.no_cards():
            return False

        # Next player move
        self.next_player()

        return True

    def get_possible_plays(self, central_card: Card) -> list:
        """ Returns suitable cards to play by rule or None. """
        possible_plays = []
        player = self.current_player()
        current_weight = player.palette.value(central_card.color)
        all_card_pairs = player.hand.all_card_pairs()

        for in_center, in_palette in all_card_pairs:
            new_palette = player.palette
            new_weight = (new_palette + in_palette).value(central_card.color)
            if new_weight > current_weight:
                possible_plays.append((in_center, in_palette))

        return possible_plays

    def get_playable_cards(self, possible_plays: list) -> list:
        playable = []
        for in_center, in_palette in possible_plays:
            new_palette = self.current_player().palette.new_palette(in_palette)
            in_center = in_center if in_center is not None else self.central_card
            new_palette_value = new_palette.value(in_center.color)
            if new_palette_value > max(self.players_value(in_center.color)):
                in_center = None if in_center is self.central_card else in_center
                playable.append((in_center, in_palette))

        return playable

    def players_value(self, color: str) -> list:
        value = [player.palette.value(color) for player in self.players]
        return value

    def congratulation_winner(self):
        self.round += 1
        print(f'Congrats, {self.current_player().name} won!')
        if self.advanced:
            print(f'Score: {self.current_player().score}')

    def add_scores(self):
        player = self.current_player()
        score = player.palette.score_count(self.central_card.color)
        player.add_score(score)

    def current_player(self):
        return self.players[self.player_index]

    def next_player(self):
        """ The move goes to the next player """
        size = len(self.players)
        self.player_index = (self.player_index + 1) % size

    def player_remove(self, current_player):
        self.lost_players.append(current_player)
        self.players.remove(current_player)

    def final_score(self):
        if self.current_player().score >= 40:
            return True
        return False


game_state = {
    'deck': 'y1 r2 y0 y1',
    'players': [
        {
            'name': 'Bob',
            'ai': True,
            'hand': 'r3 r5',
            'palette': 'y4 p2',
            'score': 0
        },
        {
            'name': 'Charley',
            'ai': False,
            'hand': 'b1 g2',
            'palette': 'l5 p6',
            'score': 0
        }
    ],
    'player_index': 0,
    'central_card': Card('red', 0),
    'round': 0
}


red7 = RED7GAME.create(True, [('ME', True), ('NOTME', True), ('OTHER', True)])
if red7.advanced:
    while not red7.game_over:
        red7.run()
        save = red7.save()
        red7 = RED7GAME.next_round(save)


else:
    red7.run()

print('Game over')
