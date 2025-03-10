from model import ScrabbleModel
from view import View
from classes import GameStatus, Player, Word, Tile

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
        self.plist = self.model.players

    def start_game(self):

        while self.model.status != GameStatus.DONE:
            cpi = self.model.curr_player_idx
            print(f"cpi: {cpi}")
            curr_player = self.model.players[cpi]
            self.view.display_board(self.model.board)
            self.view.display_player_turn(curr_player)


            while len(curr_player.rack) < 7 and not self.model.is_endgame:
                self.model.draw_tile(curr_player)
            self.view.display_rack(curr_player.rack)

            player_action = self.view.take_player_action(self.model.valid_turn_actions)

            match player_action:
                case "challenge":
                    if self.model.last_word_played is not None and self.model.is_acceptable(self.model.last_word_played[0]):
                        self.model.challenge_rule.resolve_unsuccessful_challenge(curr_player, self.model.players[cpi-1])
                    else:
                        self.model.remove_last_word(self.model.players[cpi-1])

                case "play word":

                    raise NotImplementedError

                    # main_word: Word = Word([])
                    # incidental_words: list[Word] = []
                    # prem_cells_occupied: list[Cell] = []
                    # start_row: int = self.view.take_word_start_row()
                    # start_col: int = self.view.take_word_start_col()
                    # direction: str = self.view.take_word_start_direction()

                    # showboard = self.model.create_display_board()

                    # curr_row = start_row
                    # curr_col = start_col

                    # player_choice = self.view.choose_tile_from_rack(curr_player)


                    # while isinstance(player_choice, int):
                    #     showboard[curr_row][curr_col].rep = 'X'
                    #     self.view.display_board(showboard)

                    #     player_choice = self.view.choose_tile_from_rack(curr_player)

                    #     if 


                    # self.model.score_turn()

                    # raise NotImplementedError

                case "exchange tiles":
                    tiles_to_exchange: list[Tile] = []
                    player_choice = self.view.choose_tile_from_rack(curr_player)
                    while isinstance(player_choice, int):
                        tiles_to_exchange.append(curr_player.rack.pop(player_choice))
                        self.view.display_tiles(tiles_to_exchange)

                    while self.model.tile_bag and len(curr_player.rack) < 7:
                        self.model.draw_tile(curr_player)

                    self.view.display_rack(curr_player.rack)

                case "pass":
                    pass

                case _:
                    raise Exception

            self.model.goto_next_player()

            if self.model.is_endgame:
                for player in self.model.players:
                    if not player.rack:
                        self.model.status = GameStatus.DONE
                        break

        self.view.player_win_msg(max(self.model.players, key= lambda x: x.score))
        self.view.display_scores(self.model.players)
        return












