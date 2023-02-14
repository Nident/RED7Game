import random
from src.CardList import Deck
from src.Player import Player
from src.Card import Card


class RED7GAME:

    HAND_SIZE = 7

    def __init__(self):
        self.__deck = None    # колода
        self.__players = None    # игроки
        self.__player_index = None    # индекс текущего игрока
        self.__central_card = Card('red', 0)  #
        self.__advanced = None
        self.__round = 1

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

    @staticmethod
    def create(advanced, name_list: list[tuple[str, bool]], cards: list[Card] | None = None):
        """Создаю игру"""
        game = RED7GAME()
        if cards is None:
            game.deck = Deck(Card.all_cards())  # Создаем колоду
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
        game = RED7GAME()
        game.deck = Deck(Card.list_from_str(state['deck']))

        game.players = [Player(p['name'], Card.list_from_str(p['hand']),
                               Card.list_from_str(p['palette']), p['ai'], p['score']) for p in state['players']]

        game.player_index = state['player_index']
        game.central_card = state['central_card']
        game.round = state['round']
        return game

    def run(self):
        is_running = True
        while is_running:
            is_running = self.turn()
        self.__player_index = 0
        self.congratulation_winner()
        self.add_scores()

    def turn(self) -> bool:
        # print(self.central_card.color)
        """ Возвращает False, если игра закончена. """

        current_player = self.current_player()  # игрок чей сейчас ход

        possible_plays = self.get_possible_plays(self.central_card)
        playable_cards = self.get_playable_cards(possible_plays)

        # print(playable_cards, 'it could be playeed')

        # Если существуют карты которыми можно сыграть по данному правилу
        if len(playable_cards):
            if current_player.AI:
                r = random.randint(0, len(playable_cards)-1)
                in_center, in_palette = playable_cards[r]  # беру любую карту
            else:
                index = int(input('What to play?: \n'))
                in_center, in_palette = playable_cards[index-1]

            print(f'{current_player.name}: Играет {in_palette}')
            take_one = False
            if in_center is not None:
                take_one = True if in_center.number > len(current_player.palette) else False
                self.central_card = in_center

            current_player.add_to_palette(in_palette)

            if take_one:
                new_card = self.deck.draw()
                current_player.hand.add(new_card)
        else:
            # Если подходящей карты нет...
            print(f'{current_player.name}: Выбывает')
            self.players.remove(current_player)
            self.player_index -= 1
            if len(self.players) == 1:
                return False

        # после розыгрыша карт печатаем руку игрока и разделитель
        print(current_player)
        print('-' * 20)

        # если все карты с руки сыграны, игра окончена
        if current_player.no_cards():
            return False

        # Ход переходит другому игроку.
        self.next_player()

        return True

    def get_possible_plays(self, central_card: Card) -> list:
        """ Возвращаем первую подходящую карту для игры по правилу(rule) или None, если подходящих карт нет. """
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
        print(f'Поздравляем, {self.current_player().name} выиграл!')

    def add_scores(self):
        player = self.current_player
        player.score = player.palette.score_count(self.central_card.color)

    def current_player(self):
        """Текущий игрок"""
        return self.players[self.player_index]

    def next_player(self):
        """ Ход переходит к следующему игроку. """
        size = len(self.players)
        self.player_index = (self.player_index + 1) % size


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


game = RED7GAME.create(False, [('ME', True), ('NOTME', True), ('OTHER', True)])
game.run()
