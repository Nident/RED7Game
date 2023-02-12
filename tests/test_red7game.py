from src.RED7Game import RED7GAME
from src.Card import Card


# g = RED7GAME.create(['me', 'someone'])
game_state = {
    'deck': 'y1 r5 y0 y1',
    'players': [
        {
            'name': 'Bob',
            'hand': 'r3 r5',
            'palette': 'y4 p2'
        },
        {
            'name': 'Charley',
            'hand': 'b1 g2 r7',
            'palette': 'l5 p6'
        }
    ],
    'player_index': 0
}

g = RED7GAME.load(game_state)


def test_create():
    g = RED7GAME.create(['me', 'someone'])
    assert str(g.players) == '[me: g4 l6 p7 b1 r7 y2 || r5,' \
                             ' someone: g2 o3 l2 l7 g1 y5 || b3]'


def test_load():
    g = RED7GAME.load(game_state)
    assert str(g.current_player().hand) == 'r3 r5' \
        and str(g.current_player().palette) == 'y4 p2'


def test_get_possible_plays():
    central_card = Card('red', 0)
    possible_plays = g.get_possible_plays(central_card)
    assert str(possible_plays[0]) == '(None, r5)'


def test_players_value():
    ovs = g.players_value()
    g.players[1].add_to_palette(Card('red', 7))
    vs = g.players_value()
    assert vs == [405, 707] and vs > ovs


def test_next_player():
    g.next_player()
    assert g.current_player().name == 'someone'
