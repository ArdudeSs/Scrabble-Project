from classes import Player


class View:

    def player_win_msg(self, Player: Player):
        print(f"Player {Player} wins!")
        print(f"Score: {Player.score}")

    def show_scores(self, list_players: list[Player]):
        for p in list_players:
            print(f"{p.name}: {p.score}")

    def request_player_name(self):
        raise NotImplementedError

    def display_board(self, board: list[list[str]]):
        for row in board:
            print(row)


    