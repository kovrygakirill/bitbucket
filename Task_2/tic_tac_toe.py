class Board:
    def __init__(self):
        self.field = {1: "-", 2: "-", 3: "-",
                      4: "-", 5: "-", 6: "-",
                      7: "-", 8: "-", 9: "-"}
        self.win_positions = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                              {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                              {1, 5, 9}, {3, 5, 9})

    def print_board(self):
        for position, state in self.field.items():
            if position % 3 == 0:
                print(state)
            else:
                print(state, end=" ")


class StateStorage:
    def __init__(self, player_1, player_2):
        self.moves_players = {player_1.mark: set(), player_2.mark: set()}
        self.all_moves = set()


class LogicStateStorage:
    def __init__(self, board: Board, state_storage: StateStorage):
        self.board = board
        self.state_storage = state_storage

    def move(self, player, player_move):
        if player_move not in self.state_storage.all_moves:
            self.state_storage.moves_players[player.mark].add(player_move)
            self.state_storage.all_moves.add(player_move)
            self.board.field[player_move] = player.mark
        else:
            raise PositionAlreadyTaken("Это поле уже занято")

    def check_win(self, player):
        moves_player = self.state_storage.moves_players[player.mark]

        if len(moves_player) < len(min(self.board.win_positions)):
            return False

        for win_pos in self.board.win_positions:
            if not (win_pos - moves_player):
                return True

        return False
