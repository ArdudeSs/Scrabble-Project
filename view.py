from classes import Player, Cell, Premium, Tile


class View:

    def __init__(self):
        return None

    def player_win_msg(self, Player: Player):
        print(f"Player {Player} wins!")
        print(f"Score: {Player.score}")

    def display_scores(self, list_players: list[Player]):
        for p in list_players:
            print(f"{p.name}: {p.score}")

    def request_player_name(self, p_number: int):
        return str(input(f"What is the name of Player {p_number}? "))

    def display_board(self, board: list[list[Cell]]):
        for i in range(len(board)):
            curr_row = []
            for Cell in board[i]:
                curr_row.append(Cell.rep)
            print(curr_row)

    def display_player_turn(self, player: Player):
        print(f"It is now {player}'s turn.")

    def display_rack(self, rack: list[Tile]):
        display: list[str] = []
        for t in rack:
            display.append(t.letter)
        while len(display) < 7:
            display.append("_")

        print(display)

    def take_player_action(self, valid_actions: list[str]):
        for i in range(1, len(valid_actions) + 1):
            print(f"{i} - {valid_actions[i-1]}")
        choice = int(input())
        try:
            return valid_actions[choice-1]
        except IndexError:
            print("Invalid Input!")

    def take_word_start_row(self):
        start_row: int = int(input("What row will your word start in?"))
        return start_row

    def take_word_start_col(self):
        start_col: int = int(input("What column will your word start in?"))
        return start_col

    def take_word_start_direction(self):
        direction: str = str(input("Which direction (down or right) do you want to extend your word?"))
        return direction

    def choose_tile_for_blank(self, p: Player):
        for i in range(1, len(p.rack)+1):
            print(f"{i} - {p.rack[i-1]}")
        inp: int = int(input())

        if p.rack[inp].letter == '?':
            res = str(input("What letter would you like this tile to be?"))
            if res.upper() in {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}:
                tile = p.rack[inp]
                tile.letter = res
                return tile
        else:
            return p.rack[inp]

    def display_tiles(self, tiles: list[Tile]):
        print(f"Selected tiles: {tiles}")

    def choose_tile_from_rack(self, player: Player):
        for i in range(len(player.rack)):
            print(f"{i} - {player.rack[i]}")
        return (input("Input a number to select tiles, or type anything else when you're finished picking tiles."))
