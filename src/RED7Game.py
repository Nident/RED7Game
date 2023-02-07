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
        self.rule = ('orange', '')  # верхняя карта палитры(правило игры)

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
        # elif rule[0] == 'yellow':
        #     cards = self.yellow_rule()
        # elif rule[0] == 'green':
        #     cards = self.green_rule()
        # elif rule[0] == 'lightblue':
        #     cards = self.lightBlue_rule()
        # elif rule[0] == 'blue':
        #     cards = self.blue_rule()
        # elif rule[0] == 'purple':
        #     cards = self.purple_rule()

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

        """Наибольшая последовательность цветов у игроков"""
        highest_palette = {'purple': 1}
        for palette in other_palettes:
            for item, value in palette.items():
                if value > list(highest_palette.values())[0]:
                    highest_palette = {item: value}
                elif value == list(highest_palette.values())[0] \
                        and Card.COLORS.index(item) < Card.COLORS.index(list(highest_palette.keys())[0]):
                    highest_palette = {item: value}

        """Если разница в последовательностях больше 1, 
        то игрок не сможет за 1 ход набрать более длинную последовательность"""
        if max(current_palette.values()) - max(highest_palette.values()) < 0:
            return playable_cards

        max_color = max(current_palette.keys())
        playable_cards = self.current_player().hand.playable_cards_yellow(max_color)  # карты которыми можно сыграть

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

        max_equal = max(other_palettes)
        if current_palette >= max_equal:
            playable_cards = self.current_player().hand.playable_cards_green()

        return playable_cards

    def lightBlue_rule(self):
        print("LIGHTBLUE")
        other_palettes = []
        playable_cards = []

        for player in self.players:
            """Считываем последовательность с разными цветами"""
            palettes = []
            for card in player.palette:
                palettes.append(card.color)
            other_palettes.append(set(palettes))

        current_palette = other_palettes.pop(self.player_index)
        my_max = len(current_palette)  # последовательность игрока

        # самая длинная последовательность у соперников
        other_max = []
        for i in other_palettes:
            other_max.append(len(i))

        if my_max >= max(other_max):
            playable_cards = self.current_player().hand.playable_cards_lightBlue(current_palette)

        return playable_cards

    def blue_rule(self):
        print("BLUE RULE")
        other_palettes = []
        playable_cards = []

        for player in self.players:
            palettes = []
            for card in player.palette:
                palettes.append(card.number)
            other_palettes.append(sorted(palettes))

        # Поиск длин последовательностей всех игроков
        other_lengths = []
        for cards in other_palettes:
            k = 1
            max_k = 0
            lengths = []
            if len(cards) == 1:
                other_lengths.append([k])
                continue
            for i in range(1, len(cards)):
                if cards[i-1] - cards[i] == 1:
                    k += 1
                if max_k < k:
                    max_k = k
                if cards[i-1] - cards[i] != 1:
                    k = 0

            lengths.append(max_k)
            other_lengths.append(lengths)

        current_palette = sorted(other_palettes.pop(self.player_index))  # Сортированная палитра игрока
        current_length = len(other_lengths.pop(self.player_index))  # длина сортированной палитры игрока

        """Если длинна палитры удовл. условию больше или равно максимальной длине палитры удовл. условию то играем"""
        if current_length >= max(list(map(max, other_lengths))):
            palette_order = []  # Срез карт идущих последовательно в палитре
            palette_order_2 = []

            if current_length == 1:
                playable_cards = self.current_player().hand.playable_cards_blue(current_palette[0])
                return playable_cards

            palette_order.append(current_palette[0])
            for i in range(1, current_length-1):
                if current_palette[i-1]-current_palette[i] == 1:
                    palette_order.append(current_palette[i])
                else:
                    palette_order_2.extend(palette_order)
                    palette_order = []
            
            #  не дописал ()
            playable_cards = self.current_player().hand.playable_cards_blue(max(current_palette))

        return playable_cards

    def purple_rule(self):
        print("PURPLE RULE")
        other_palettes = []
        playable_cards = []

        for player in self.players:
            """Считываем последовательность номиналом меньше 4 у игроков"""
            for card in player.palette:
                palettes = []
                if card.number < 4:
                    palettes.append(card)
            other_palettes.append(len(palettes))

        current_palette = other_palettes.pop(self.player_index)  # Палитра игрока

        max_less_four = max(other_palettes)
        if current_palette >= max_less_four:
            playable_cards = self.current_player().hand.playable_cards_purple()

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
