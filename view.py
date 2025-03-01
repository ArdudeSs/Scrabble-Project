from classes import Player


class View:

    def player_win_msg(self, Player: Player):
        print(f"Player {Player} wins!")
        print(f"Score: {Player.score}")

    def show_scores(self, list_players: list[Player]):
        for p in list_players:
            print(f"{p.name}: {p.score}")

    