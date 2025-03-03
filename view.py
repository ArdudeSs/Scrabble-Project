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

    def request_player_name(self):
        raise NotImplementedError

    def display_board(self, board: list[list[Cell]]):
        for row in board:
            curr_row = []
            for Cell in row:
                curr_row.append(Cell.rep)
            print(curr_row)

    def show_rack(self, rack: list[Tile | str]):
        display: list[str] = []
        for t in rack:
            if isinstance(t, Tile):
                display.append(str(t))
            else:
                display.append("_")
        print(display)

        # display: list[str] = [t.letter for t in rack if isinstance(t, Tile) else "_"]


    