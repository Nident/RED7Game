def red_new_palette(self, card):
    self.cards.append(card)
    value = self.value_red()
    self.cards.remove(card)
    return value

def orange_new_palette(self, card):
    self.cards.append(card)
    value = self.value_orange()
    self.cards.remove(card)
    return value


def yellow_new_palette(self, card):
    self.cards.append(card)
    value = self.value_yellow()
    self.cards.remove(card)
    return value


 def green_new_palette(self, card):
        self.cards.append(card)
        value = self.value_green()
        self.cards.remove(card)
        return value


def lightblue_new_palette(self, card):
    self.cards.append(card)
    value = self.value_lightblue()
    self.cards.remove(card)
    return value

    def blue_new_palette(self, card):
        self.cards.append(card)
        value = self.value_blue()
        self.cards.remove(card)
        return value


    def purple_new_palette(self, card):
        self.cards.append(card)
        value = self.value_purple()
        self.cards.remove(card)
        return value



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