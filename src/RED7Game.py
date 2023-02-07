from src.CardList import Deck, Heap
from src.Player import Player
from src.Card import Card
from src.palette import Palette
from collections import Counter


class RED7GAME:

    HAND_SIZE = 7

    def __init__(self):
        self.deck = None    # колода
        self.heap = None    # верхняя карта
        self.players = None    # игроки
        self.player_index = None    # индекс текущего игрока
        self.rule = ('blue', '')  # верхняя карта палитры(правило игры)

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
        game.heap = Heap([game.deck.draw()])  # верхняя карта

        return game

    def run(self):
        is_running = True
        while is_running:
            is_running = self.turn()
        self.congratulation_winner()

    def turn(self) -> bool:
        """ Возвращает False, если игра закончена. """

        current_player = self.current_player()  # игрок чей сейчас ход
        # print(self.players)

        playable_cards = self.get_playable_cards(self.rule)
        print(playable_cards, "GOT CARDS")

        # Если существуют карты которыми можно сыграть по данному правилу
        if len(playable_cards):
            card = playable_cards[0]  # беру Первую карту
            print(f'{current_player.name}: Играет {card}')
            current_player.add_to_palette(card)
        else:
            # Если подходящей карты нет...
            # print(f'{current_player.name}: либо меняет правила либо пас')
            # playable_cards = self.new_rule()
            # if len(playable_cards):
            #     print(f'{current_player.name}: Выбывает')
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

    def get_playable_cards(self, rule) -> Card:
        """ Возвращаем первую подходящую карту для игры по правилу(rule) или None, если подходящих карт нет. """
        # red: старшая карта
        # orange: больше всего карт одного номинала.
        # yellow: больше всего карт одного цвета.
        # green: больше всего чётных карт.
        # lightBlue: больше всего карт разных цветов
        # blue: больше всего карт, идущих по порядку
        # purple: больше всего карт номиналом меньше 4
        cards = []
        if rule[0] == 'red':
            cards = self.red_rule()
        elif rule[0] == 'orange':
            cards = self.orange_rule()
        elif rule[0] == 'yellow':
            cards = self.yellow_rule()
        elif rule[0] == 'green':
            cards = self.green_rule()
        elif rule[0] == 'lightblue':
            cards = self.lightBlue_rule()
        elif rule[0] == 'blue':
            cards = self.blue_rule()
        elif rule[0] == 'purple':
            cards = self.purple_rule()

        return cards

    def red_rule(self):
        print("RED RULE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            palettes.extend([player.palette.value_red()])

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу

        for card in self.current_player().hand:
            value = self.current_player().palette.red_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                playable_cards.append(card)

        return playable_cards

    def orange_rule(self):
        print("ORANGE RULE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            # print(player.palette)
            palettes.extend([player.palette.value_orange()])

        print(palettes)

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу
        # print(self.current_player().hand)
        for card in self.current_player().hand:
            value = self.current_player().palette.orange_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                # print(value, card)
                playable_cards.append(card)

        return playable_cards

    def yellow_rule(self):
        print("YELLOW RULE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            # print(player.palette)
            palettes.extend([player.palette.value_yellow()])

        print(palettes)

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу
        # print(self.current_player().hand)
        for card in self.current_player().hand:
            value = self.current_player().palette.yellow_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                # print(value, card)
                playable_cards.append(card)

        return playable_cards

    def green_rule(self):
        print("GREEN RULE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            # print(player.palette)
            palettes.extend([player.palette.value_green()])

        print(palettes)

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу

        for card in self.current_player().hand:
            value = self.current_player().palette.green_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                # print(value, card)
                playable_cards.append(card)

        return playable_cards

    def lightBlue_rule(self):
        print("LIGHTBLUE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            # print(player.palette)
            palettes.extend([player.palette.value_lightblue()])

        print(palettes)

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу

        print(self.current_player().hand)
        for card in self.current_player().hand:
            value = self.current_player().palette.lightblue_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                # print(value, card)
                playable_cards.append(card)

        return playable_cards

    def blue_rule(self):
        print("BLUE RULE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            # print(player.palette)
            palettes.extend([player.palette.value_blue()])

        print(palettes)

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу

        print(self.current_player().hand)
        for card in self.current_player().hand:
            value = self.current_player().palette.blue_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                # print(value, card)
                playable_cards.append(card)

        return playable_cards

    def purple_rule(self):
        print("PURPLE RULE")
        palettes = []
        playable_cards = []

        for player in self.players:  # Собираю палитры всех игроков
            # print(player.palette)
            palettes.extend([player.palette.value_purple()])

        print(palettes)

        # ВОЗМОЖНО тут должно быть условие если в начале игы игрок изначально ведет по правилу

        print(self.current_player().hand)
        for card in self.current_player().hand:
            value = self.current_player().palette.purple_new_palette(card)  # Ценность каждой карты
            if value > max(palettes):
                # print(value, card)
                playable_cards.append(card)

        return playable_cards

    def new_rule(self):
        """Изменяем правила игры если это возможно иначе []"""
        current_palette = self.current_player().palette
        possible_rules = self.current_player().hand.possible_rules()
        playable_cards = []

        for i in possible_rules:
            rule = i.color
            removed = self.current_player().hand.remove(i)  # Удаляем карту которой изменяем правила

            playable_cards = self.get_playable_cards(rule)
            self.current_player().hand.add(removed)  # Добавляем обратно
            if len(playable_cards) != 0:
                self.rule = rule
                print(playable_cards, 'aaaaaaaaaaaaaaaaaa')

        print(playable_cards, "AAAAAAAAa")
        return playable_cards

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
