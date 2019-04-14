import numpy as np



class Board:

    def __init__(self, board_shape=(8, 8), initial_placement=True):
        # 0:None, 1:Black piece, 2:White piece.
        self.out_range = -1
        self.none  = 0
        self.black = 1
        self.white = 2

        # For out range.
        self.board_shape = (board_shape[0] + 2, board_shape[1] + 2)
        self.board_state = np.zeros(self.board_shape, dtype=int)

        # Set out range state.
        self.board_state[:,0] = self.board_state[:,-1] = self.out_range
        self.board_state[0,:] = self.board_state[-1,:] = self.out_range

        if initial_placement:
            self.board_state[4][5] = self.board_state[5][4] = self.black
            self.board_state[4][4] = self.board_state[5][5] = self.white

        self.player_count = 0
        print(self.board_state)


    def setup_player(self, player):
        self.player_count += 1
        player.set_piece_color(self.player_count)

    
    def get_board_state(self):
        return self.board_state.copy()


    def can_be_put(self, x, y):
        if 0 <= x < self.board_shape[1]: return False
        if 0 <= y < self.board_shape[0]: return False
        

        return self.board_state[y][x] == self.none


    def set_state(self, x, y, color):
        if not self.can_be_put(y, x):
            return False
        
        self.board_state[y][x] = color
        

    def explore_chains(self, x, y):
        return

    def turn_over_piece(self):
        return

    def render(self):
        return


if __name__ == '__main__':
    Board()
