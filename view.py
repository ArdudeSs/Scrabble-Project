from classes import Player, Cell, Premium, Tile


class View:

    def __init__(self):
        return None

    def player_win_msg(self, Player: Player):
        print(f"Player {Player} wins!")
        print(f"Score: {Player.score}")

    def show_scores(self, list_players: list[Player]):
        for p in list_players:
            print(f"{p.name}: {p.score}")

    def request_player_name(self, p_number: int):
        return str(input(f"What is the name of Player {p_number}?"))

    def display_board(self, board: list[list[Cell]]):
        for row in board:
            curr_row = []
            for Cell in row:
                curr_row.append(Cell.rep)
            print(curr_row)

    def show_rack(self, rack: list[Tile]):
        display: list[str] = []
        for t in rack:
            display.append(t.letter)
        while len(display) < 7:
            display.append("_")

        print(display)

    def take_word_start_location_and_direction(self, p: Player):
        start_row: int = int(input("What row will your word start in?"))
        start_col: int = int(input("What column will your word start in?"))
        direction: str = str(input("Which direction (down or right) do you want to extend your word?"))
        return start_row, start_col, direction.lower()

    def choose_tile(self, p: Player):
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




    