# pyright: strict

from classes import Player, Tile, Cell, GameStatus, Word
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
        self.is_first_turn = True


    def place_tile(self, tile: Tile, r: int, c: int):
        self.board[r][c].tile = tile

    def detect_words(self, r: int, c: int) -> list[Word]:
        raise NotImplementedError

    @property
    def is_endgame(self):
        return len(self.tile_bag) == 0

    def goto_next_player(self):
        if self.curr_player_idx == len(self.players):
            self.curr_player_idx = 0
        else:
            self.curr_player_idx += 1

    def get_word_value(self, word: list[Tile]) -> int:
        curr_sum: int = 0
        for t in word:
            curr_sum += t.value

        return curr_sum

    def score_turn(self, words: list[list[Tile]]) -> int:
        turn_sum: int = 0
        for word in words:
            turn_sum += self.get_word_value(word)

        return turn_sum

    def draw_tile(self, player: Player):
        rack = player.rack
        if len(rack) == 7:
            raise ValueError('The rack is already full and there was an attempt to draw tiles.')

        if len(self.tile_bag) == 0:
            raise ValueError('The tile bag is already empty!')

        else:
            rng: int = randint(0, len(self.tile_bag)-1)
            drawn: Tile = self.tile_bag.pop(rng)
            self.tile_counts[drawn.letter] -= 1
            # print(f"rng: {rng}, tile: {drawn}")
            rack.append(drawn)
            return None

    def return_tiles(self, tiles: list[Tile]):
        for tile in tiles:
            self.tile_bag.append(tile)
            self.tile_counts[tile.letter] += 1

    def decide_turn_order(self, players: list[Player]):
        res: list[Player] = []
        for p in players:
            self.draw_tile(p)
            res.append(p)
        res.sort(key = lambda x: str(x.rack[0]))
        for pl in res:
            rm: Tile = pl.rack.pop(0)
            self.tile_bag.append(rm)
        return res

    def setup_word_list(self, word_list: str) -> None:
        self.acceptable_words: set[str] = set()
        with open(f"{word_list}.txt") as f:
            line: str = f.readline().strip()
            while line:
                self.acceptable_words.add(line)
                line: str = f.readline().strip()
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
        return word.upper() in self.acceptable_words

# ====== TESTING STUFF ====== #
if __name__ == "__main__":
    from view import View
    Ardi = Player("Ardi")
    Renee = Player("Renee")
    Model = ScrabbleModel([Ardi, Renee], "CSW2019", "5pt")
    # print(len(Model.tile_bag))
    v = View()

    v.show_rack(Ardi.rack)
    v.show_rack(Renee.rack)


    # v.display_board(Model.board)


    # for tile in Model.tile_bag:
    #     print(tile)

    # Model.draw_tile(Ardi)
    # v.show_rack(Ardi.rack)

    # print(len(Model.tile_bag))
    # Model.draw_tile(Ardi)
    # v.show_rack(Ardi.rack)
    # print(len(Model.tile_bag))

    # print(Model.tile_counts)