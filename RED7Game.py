from CardList import Deck, Heap
from Player import Player
from Card import Card
from collections import Counter


class RED7GAME:

    HAND_SIZE = 7

    def __init__(self):
        self.deck = None    # колода
        self.heap = None    # верхняя карта
        self.players = None    # игроки
        self.player_index = None    # индекс текущего игрока
        self.rule = ('green', '')  # верхняя карта палитры(правило игры)

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
        # print(game.players)
        game.player_index = 0
        # print('DECKSHUF:' + repr(game.deck))
        game.heap = Heap([game.deck.draw()])
        # print(game.heap)
        # print(game.rule[-1])
        return game

    def run(self):
        is_running = True
        while is_running:
            is_running = self.turn()
        self.congratulation_winner()

    def turn(self) -> bool:
        """ Возвращает False, если игра закончена. """

        current_player = self.current_player()  # игрок чей сейчас ход

        playable_cards = self.get_playable_card(self.rule)
        print(playable_cards, "GOT CARDS")
        print(current_player)

        if len(playable_cards):
            card = playable_cards[0]
            print(f'{current_player.name}: Играет {card}')
            current_player.add_to_palette(card)
        else:
            # Если подходящей карты нет...
            print(f'{current_player.name}: либо меняет правила либо пас')
            # self.players.pop(self.player_index)  # Выбывет игрок
            # self.player_index = 0
            return False

        # после розыгрыша карт печатаем руку игрока и разделитель
        print(current_player)
        print('-' * 20)

        # если все карты с руки сыграны, игра окончена
        if current_player.no_cards():
            return False

        # Ход переходит другому игроку.
        self.next_player()
        # игра продолжается
        return True

    def get_playable_card(self, rule) -> Card:
        """ Возвращаем первую подходящую карту для игры по правилу(rule) или None, если подходящих карт нет. """
        # red: старшая карта
        # orange: больше всего карт одного номинала
        # yellow: больше всего карт одного цвета
        # green: больше всего чётных карт
        # lightBlue: больше всего карт разных цветов
        # blue: больше всего карт, идущих по порядку
        # purple:  больше всего карт номиналом меньше 4
        cards = []
        if rule[0] == 'red':
            cards = self.red_rule()
        elif rule[0] == 'orange':
            cards = self.orange_rule()
        elif rule[0] == 'yellow':
            cards = self.yellow_rule()
        elif rule[0] == 'green':
            cards = self.green_rule()
        elif rule[0] == 'lightBlue':
            cards = self.lightBlue_rule()
        elif rule[0] == 'blue':
            cards = self.blue_rule()
        elif rule[0] == 'purple':
            cards = self.purple_rule()

        return cards

    def red_rule(self):
        print("RED RULE")
        other_palettes = []

        for player in self.players:
            # print(player.palette)
            other_palettes.extend(player.palette)

        other_palettes.pop(self.player_index)  # Удаляем палитру текущего игрока
        # print(other_palettes)

        max_card = Card.max_card(other_palettes)  # Находим максимальную карту во всех палитрах(кроме играющего)
        print('Max Card in players palettes:', max_card)

        playable_cards = self.current_player().hand.playable_cards_red(max_card)  # карты которыми можо сыграть

        return playable_cards

    def orange_rule(self):
        print("ORANGE RULE")
        other_palettes = []
        playable_cards = []

        for player in self.players:
            """Считываем последовательности номеров игроков"""
            numbers = []
            for i in player.palette:
                numbers.append(i.number)
            c = Counter(numbers)
            other_palettes.append(c)

        # print(next(iter(other_palettes[0].items())))

        current_palette = other_palettes.pop(self.player_index)  # последовательность играющего

        """Наибольшая последовательность игроков"""
        highest_palette = {1: 1}
        for palette in other_palettes:
            for item, value in palette.items():
                if value > list(highest_palette.values())[0]:
                    highest_palette = {item: value}
                elif value == list(highest_palette.values())[0] and item > list(highest_palette.keys())[0]:
                    highest_palette = {item: value}

        print(highest_palette, 'highest_NUMBER')

        # highest_palette = highest_palette.items()
        # print(highest_palette.items())

        """Если разница в последовательностях больше 1, то игрок не сможет за 1 ход набрать более длинную последовательность
            или
        Если номинал карты соперника больше, то игрок не сможет за 1 ход набрать более длинную последовательность"""
        # print(current_palette)
        if max(current_palette.values()) - max(highest_palette.values()) < 0:
            return playable_cards
        # elif max(current_palette.values()) - max(highest_palette.values()) <= -1 \
        #         and max(current_palette.keys()) - max(highest_palette.keys()) < 0:
        #     return []

        max_number = max(current_palette.keys())
        playable_cards = self.current_player().hand.playable_cards_orange(max_number)  # карты которыми можо сыграть

        return playable_cards

    def yellow_rule(self):
        print("YELLOW RULE")
        other_palettes = []
        playable_cards = []

        for player in self.players:
            """Считываем последовательности номеров у игроков"""
            colors = []
            for i in player.palette:
                colors.append(i.color)
            c = Counter(colors)
            other_palettes.append(c)

        current_palette = other_palettes.pop(self.player_index)  # последовательность играющего
        # print(current_palette)
        # print(other_palettes)


        """Наибольшая последовательность цветов у игроков"""
        highest_palette = {'purple': 1}
        for palette in other_palettes:
            for item, value in palette.items():
                if value > list(highest_palette.values())[0]:
                    highest_palette = {item: value}
                elif value == list(highest_palette.values())[0] \
                        and Card.COLORS.index(item) < Card.COLORS.index(list(highest_palette.keys())[0]):
                    highest_palette = {item: value}

        print(highest_palette, 'highest_COLORS')

        # highest_palette = highest_palette.items()

        """Если разница в последовательностях больше 1, то игрок не сможет за 1 ход набрать более длинную последовательность
            или
        Если цвет карты соперника старше(индекс младше), то игрок не сможет за 1 ход набрать более длинную последовательность"""
        if max(current_palette.values()) - max(highest_palette.values()) < 0:
            return playable_cards
        # elif Card.COLORS.index(max(current_palette.keys())) > Card.COLORS.index(max(highest_palette.keys())):

        max_color = max(current_palette.keys())
        playable_cards = self.current_player().hand.playable_cards_yellow(max_color)  # карты которыми можо сыграть

        return playable_cards

    def green_rule(self):
        print("GREEN RULE")
        other_palettes = []
        playable_cards = []

        for player in self.players:
            """Считываем последовательности номеров у игроков"""
            for card in player.palette:
                palettes = []
                if card.number % 2 == 0:
                    palettes.append(card)
            other_palettes.append(len(palettes))

        current_palette = other_palettes.pop(self.player_index)
        print(current_palette)
        max_equal = max(other_palettes)
        if current_palette >= max_equal:
            playable_cards = self.current_player().hand.playable_cards_green()
        print(max_equal)
        print(playable_cards)

        return playable_cards

    def lightBlue_rule(self):
        print("lightblue")
        get_all_hands = self.players
        print(get_all_hands)

    def blue_rule(self):
        print("blue")
        get_all_hands = self.players
        print(get_all_hands)

    def purple_rule(self):
        print("purple")
        get_all_hands = self.players
        print(get_all_hands)


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
