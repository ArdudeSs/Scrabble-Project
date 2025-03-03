# pyright: strict

from classes import Player, Tile, Cell, GameStatus
from random import randint

class ScrabbleModel:
    def __init__(self, player_list: list[Player], word_list_name: str, challenge_rule: str):
        if not 1 < len(player_list) <= 4:
            raise ValueError("The number of players should be between 1 and 4.")

        self.setup_board()
        self.setup_tile_bag()
        self.setup_word_list(word_list_name)
        self.curr_player_idx: int = 0
        self.status: GameStatus = GameStatus.ONGOING
        self.challenge_rule: str = challenge_rule
        self.players = self.decide_turn_order(player_list)
        # print("board setup done")

    def draw_tile(self, player: Player):
        rack = player.rack
        if all(isinstance(t, Tile) for t in rack):
            raise ValueError('The rack is already full and there was an attempt to draw tiles.')

        if len(self.tile_bag) == 0:
            raise ValueError('The tile bag is already empty!')

        else:
            rng: int = randint(0, len(self.tile_bag)-1)
            drawn: Tile = self.tile_bag.pop(rng)
            self.tile_counts[drawn.letter] -= 1
            # print(f"rng: {rng}, tile: {drawn}")

            for i in range(0, 7):
                if not isinstance(player.rack[i], Tile):
                    player.rack[i] = drawn
                    break

            if all(isinstance(space, Tile) for space in rack):
                print(f"player {player.name}'s rack is now full.")
            
            return None

    def decide_turn_order(self, players: list[Player]):
        res: list[Player] = []
        for p in players:
            self.draw_tile(p)
            res.append(p)

        res.sort(key = lambda x: str(x.rack[0]))
        for pl in res:
            rm: Tile = pl.rack.pop(0)
            self.tile_bag.append(rm) 
            # Pyright's mad at me because of the above line;
            # rm is always a tile, but since racks are list[Tile | str]
            # Pyright thinks rm could be a str.
            # Not sure what to do about it.
            pl.rack.append("_")

        return res


    def setup_word_list(self, word_list: str) -> None:
        self.acceptable_words: set[str] = set()
        with open(f"{word_list}.txt") as f:
            line: str = f.readline()
            while line:
                self.acceptable_words.add(line)
                line: str = f.readline()

        # print("word list setup done")

    def setup_tile_bag(self):
        self.tile_counts: dict[str, int] = {}
        self.tile_bag: list[Tile] = []
        with open("tile_bag.txt") as bag:
            letters: str = bag.readline().strip()
            while letters:
                for letter in letters:
                    self.tile_bag.append(Tile(letter))

                self.tile_counts.update({letters[0]:len(letters)})
                letters: str = bag.readline().strip()
        # print("tile bag setup done")

    def setup_board(self) -> None:
        self.board: list[list[Cell]] = []
        with open("board.txt") as b:
            row = b.readline().split()
            r: int = 0
            while row:
                res_row: list[Cell] = [Cell(row[c], r, c) for c in range(len(row))]
                self.board.append(res_row)
                row = b.readline().split()

    def is_acceptable(self, word: str) -> bool:
        return word in self.acceptable_words

# ====== TESTING STUFF ====== #
from view import View
Ardi = Player("Ardi")
Renee = Player("Renee")
Model = ScrabbleModel([Ardi, Renee], "CSW2019", "5pt")
# print(len(Model.tile_bag))
v = View()

v.show_rack(Ardi.rack)
v.show_rack(Renee.rack)

for pl in Model.players:
    print(pl)
# for tile in Model.tile_bag:
#     print(tile)

# Model.draw_tile(Ardi)
# v.show_rack(Ardi.rack)

# print(len(Model.tile_bag))
# Model.draw_tile(Ardi)
# v.show_rack(Ardi.rack)
# print(len(Model.tile_bag))

# print(Model.tile_counts)