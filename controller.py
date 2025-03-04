from model import ScrabbleModel
from view import View
from classes import GameStatus, Player, Word

class Controller:

    def __init__(self, total_players: int, word_list: str, challenge_rule: str):
        self.view = View()
        names = []
        for i in range(total_players):
            names.append(self.view.request_player_name(i))
        players = []
        for name in names:
            players.append(Player(name))
        self.model = ScrabbleModel(players, word_list, challenge_rule)

    def start_game(self):

        while self.model.status != GameStatus.DONE:
            raise NotImplementedError









