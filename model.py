# pyright: strict

from classes import Player, Letter

class ScrabbleModel:
    def __init__(self, player_list: [list[Player]], word_list_name: str, challenge_rule: str):
        if not 1 < len(player_list) <= 4:
            raise ValueError("The number of players should be between 1 and 4.")

        self.setup_board()
        with open(f"{word_list_name}") as f:
            line: str = f.readline()
            self.acceptable_words: set = set()
            while line:
                self.acceptable_words.add(line)

    def setup_board(self):
        with open("board.txt") as b:
            self.board = []
            line = b.readline()
            while line:
                self.board.append(line)

    def is_acceptable(self, word):
        return word in self.acceptable_words

