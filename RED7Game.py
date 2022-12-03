from CardList import Deck, Heap
from Player import Player
from Card import Card


class RED7GAME:

    HAND_SIZE = 7

    def __init__(self):
        self.deck = None    # колода
        self.heap = None    # верхняя карта
        self.players = None    # игроки
        self.player_index = None    # индекс текущего игрока
        self.rule = ('red', 'старшая карта')  # верхняя карта палитры(правило игры)

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

        cards = self.get_playable_card(self.rule)
        print(cards, "GOT CARDS")

        if len(cards):
            card = cards[0]
            print(f'{current_player.name}: Играет {card}')
            # current_player.heap.add(card)
        # else:
        #     # Если подходящей карты нет, берет карту из колоды
        #     print('Берет карту из колоды')
        #     card = self.deck.draw()
        #     if card.playable(top):
        #         print(f'Играет {card}')
        #     else:
        #         print('Пас!')
        #         current_player.add_card_to_hand(card)
        #
        # # после розыгрыша карт печатаем руку игрока и разделитель
        # print(current_player)
        # print('-' * 20)
        #
        # # если все карты с руки сыграны, игра окончена
        # if current_player.no_cards():
        #     return False
        #
        # # Ход переходит другому игроку.
        # self.next_player()
        # # игра продолжается

        return False

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
        print("RED")
        other_palettes = []
        maximum_current_card = None

        for i in self.players:
            other_palettes.append(i.palette)

        other_palettes.pop(self.player_index)  # Удаляем палитру текущего игрока
        max_card = Card.max_card(other_palettes)  # Находим максимальную карту во всех палитрах(кроме играющего)
        print(max_card)

        playable_hand = self.current_player().hand
        playable_cards = self.current_player().hand.playable_cards(max_card)  # карты которыми можо сыграть

        print(playable_cards)
        return playable_cards



    def orange_rule(self):
        print("Orange")
        get_all_hands = self.players
        print(get_all_hands)

    def yellow_rule(self):
        print("yellow")
        get_all_hands = self.players
        print(get_all_hands)

    def green_rule(self):
        print("green")
        get_all_hands = self.players
        print(get_all_hands)

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

    def rule(self):
        self.heap[0]


game = RED7GAME.create(['ME', 'NOTME', 'OTHER'])
game.run()
