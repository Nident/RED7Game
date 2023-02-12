from src.CardList import Deck
from src.Player import Player
from src.Card import Card


class RED7GAME:

    HAND_SIZE = 7

    def __init__(self):
        self.deck = None    # колода
        self.players = None    # игроки
        self.player_index = None    # индекс текущего игрока
        self.central_card = Card('red', 0)  # (правило игры)

    @staticmethod
    def create(name_list: list[str], cards: list[Card] | None = None):
        """Создаю игру"""
        game = RED7GAME()
        if cards is None:
            game.deck = Deck(Card.all_cards())  # Создаем колоду
            game.deck.shuffle()
        else:
            game.deck = Deck(cards)

        game.players = [Player(name, [game.deck.draw() for _ in range(RED7GAME.HAND_SIZE - 1)], [game.deck.draw()])
                        for name in name_list]
        game.player_index = 0
        # game.heap = Heap([game.deck.draw()])  # верхняя карта

        return game

    @staticmethod
    def load(state: dict):
        game = RED7GAME()
        game.deck = Deck(Card.list_from_str(state['deck']))

        game.players = [Player(p['name'], Card.list_from_str(p['hand']), Card.list_from_str(p['palette']))
                        for p in state['players']]
        game.player_index = state['player_index']
        return game

    def run(self):
        is_running = True
        while is_running:
            is_running = self.turn()
        self.congratulation_winner()

    def turn(self) -> bool:
        """ Возвращает False, если игра закончена. """

        current_player = self.current_player()  # игрок чей сейчас ход
        possible_plays = self.get_possible_plays(self.central_card)
        print(possible_plays, "GOT CARDS")

        playable_cards = self.get_playable_cards(possible_plays)

        print(playable_cards, 'it could be playeed')

        # playable_cards = self.get_playable_cards(possible_plays)
        print(self.players_value(self.central_card.color))
        # Если существуют карты которыми можно сыграть по данному правилу
        if len(playable_cards):
            play = playable_cards[1]  # беру Первую карту
            print(f'{current_player.name}: Играет {play}')
            self.central_card = play[0] if play[0] is not None else self.central_card
            current_player.add_to_palette(play[-1])
        else:
            # Если подходящей карты нет...
            print(f'{current_player.name}: Выбывает')
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
        print(f'Поздравляем, {self.current_player().name} выиграл!')

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
            'hand': 'r3 r5',
            'palette': 'y4 p2'
        },
        {
            'name': 'Charley',
            'hand': 'b1 g2',
            'palette': 'l5 p6'
        }
    ],
    'player_index': 0
}


game = RED7GAME.create(['ME', 'NOTME', 'OTHER'])
game.run()
