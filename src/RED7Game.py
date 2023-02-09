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

        game.players = [Player(name, [game.deck.draw() for _ in range(RED7GAME.HAND_SIZE)]) for name in name_list]
        game.player_index = 0
        # game.heap = Heap([game.deck.draw()])  # верхняя карта

        return game

    def run(self):
        is_running = True
        while is_running:
            is_running = self.turn()
        self.congratulation_winner()

    def turn(self) -> bool:
        """ Возвращает False, если игра закончена. """
        print(self.central_card.color)

        current_player = self.current_player()  # игрок чей сейчас ход

        # print(self.players)
        # print([player.palette for player in self.players])
        # print(self.players_value())
        # print(current_player.palette)

        possible_plays = self.get_possible_plays(self.central_card)
        print(possible_plays, "GOT CARDS")

        # playable_cards = self.get_playable_cards(possible_plays)
        # Если существуют карты которыми можно сыграть по данному правилу
        if len(possible_plays):
            play = possible_plays[0]  # беру Первую карту
            print(f'{current_player.name}: Играет {play}')
            self.central_card = play[0] if play[0] is not None else self.central_card
            current_player.add_to_palette(play[-1])
        # else:
        #     # Если подходящей карты нет...
        #     print(f'{current_player.name}: Выбывает')
        #     return False

        # после розыгрыша карт печатаем руку игрока и разделитель
        print(current_player)
        print('-' * 20)

        # если все карты с руки сыграны, игра окончена
        if current_player.no_cards():
            return False

        # Ход переходит другому игроку.
        self.next_player()

        return True

    def get_possible_plays(self, central_card):
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

    def players_value(self):
        value = [player.palette.value(self.central_card.color) for player in self.players]
        # max_value = max(value)
        return value

    def new_rule(self):
        """Изменяем правила игры если это возможно иначе []"""
        # current_palette = self.current_player().palette
        # possible_rules = self.current_player().hand.possible_rules()
        # playable_cards = []
        #
        # for i in possible_rules:
        #     rule = i.color
        #     removed = self.current_player().hand.remove(i)  # Удаляем карту которой изменяем правила
        #
        #     playable_cards = self.get_playable_cards(rule)
        #     self.current_player().hand.add(removed)  # Добавляем обратно
        #     if len(playable_cards) != 0:
        #         self.rule = rule
        #         print(playable_cards, 'aaaaaaaaaaaaaaaaaa')
        #
        # print(playable_cards, "AAAAAAAAa")
        return

    def congratulation_winner(self):
        print(f'Поздравляем, {self.current_player().name} выиграл!')

    def current_player(self):
        """Текущий игрок"""
        return self.players[self.player_index]

    def next_player(self):
        """ Ход переходит к следующему игроку. """
        size = len(self.players)
        self.player_index = (self.player_index + 1) % size


game = RED7GAME.create(['ME', 'NOTME', 'OTHER'])
game.run()
