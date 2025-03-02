# pyright: strict

from classes import Player, Tile

class ScrabbleModel:
    def __init__(self, player_list: list[Player], word_list_name: str, challenge_rule: str):
        if not 1 < len(player_list) <= 4:
            raise ValueError("The number of players should be between 1 and 4.")

        self.setup_board()
        # print("board setup done")
        self.acceptable_words: set[str] = set()
        with open(f"{word_list_name}.txt") as f:
            line: str = f.readline()
            while line:
                self.acceptable_words.add(line)
                line: str = f.readline()

        # print("word list setup done")

        self.tile_counts: dict[Tile, int] = {}
        self.tile_bag: list[Tile] = []
        with open("tile_bag.txt") as bag:
            letters: str = bag.readline()
            while letters:
                for letter in letters:
                    self.tile_bag.append(Tile(letter))

                self.tile_counts.update({Tile(letters[0]):len(letters)})
                letters: str = bag.readline()
        # print("tile bag setup done")

    def setup_board(self) -> None:
        self.board: list[list[str]] = []
        with open("board.txt") as b:
            line: list[str] = b.readline()
            while line:
                self.board.append(line.split())
                line: list[str] = b.readline()

    def is_acceptable(self, word: str) -> bool:
        raise NotImplementedError
        return word in self.acceptable_words





# Ardi = Player("Ardi")
# Renee = Player("Renee")
# Model = ScrabbleModel([Ardi, Renee], "CSW2019", "5pt")
# print(Model.board)
# for row in Model.board:
#     print(isinstance(row, list))
