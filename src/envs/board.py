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


    def setup_player(self, player):
        self.player_count += 1
        player.set_piece_color(self.player_count)

    
    def get_board_state(self):
        return self.board_state.copy()


    def render(self):
        print(self.board_state)


    # direction: 2 dim tuple (x, y). value is -1, 0, or 1.
    def count_turn_over(self, color, pos, direction):
        pos, direction = np.asarray(pos, dtype=int), np.asarray(direction, dtype=int)

        i = 0
        while True:
            i += 1
            state = self.board_state[tuple(pos + direction*i)]
            if state == self.out_range: return 0
            if state == self.none:      return 0
            if state == color:          return i-1
 

    def can_be_put(self, color, pos):
        if not self.board_state[pos] == self.none:
            return False

        # Examine clockwise from above.
        if self.count_turn_over(color, pos, direction=(-1, 0)): return True
        if self.count_turn_over(color, pos, direction=(-1, 1)): return True
        if self.count_turn_over(color, pos, direction=( 0, 1)): return True
        if self.count_turn_over(color, pos, direction=( 1, 1)): return True
        if self.count_turn_over(color, pos, direction=( 1, 0)): return True
        if self.count_turn_over(color, pos, direction=( 1,-1)): return True
        if self.count_turn_over(color, pos, direction=( 0,-1)): return True
        if self.count_turn_over(color, pos, direction=(-1,-1)): return True
        return False


    def exist_legal_move(self, color):
        for y in range(1, self.board_shape[0]-1):
            for x in range(1, self.board_shape[1]-1):
                if self.can_be_put(color, (x, y)):
                    return True
        return False


    def put_a_piece(self, color, pos):
        if not self.can_be_put(color, pos):
            return False
        
        self.board_state[pos] = color
        for v_y in range(-1, 2):
            for v_x in range(-1, 2):
                if v_x == v_y == 0:
                    continue
                n_turn_over_pieces = self.count_turn_over(color, pos, (v_x, v_y))
                self.turn_over_piece(pos, (v_x, v_y), n_turn_over_pieces)
        

    def turn_over_piece(self, pos, direction, n_pieces):
        pos, direction = np.asarray(pos, dtype=int), np.asarray(direction, dtype=int)
        for i in range(1, n_pieces+1):
            piece_pos = tuple(pos + direction*i)
            self.board_state[piece_pos] = 3 - self.board_state[piece_pos]


    def is_game_set(self):
        if self.exist_legal_move(self.black): return False
        if self.exist_legal_move(self.white): return False
        return True


    def get_game_result(self):
        n_black = len(self.board_state[self.board_state == self.black])
        n_white = len(self.board_state[self.board_state == self.white])

        if   n_black > n_white: winner = 'player1'
        elif n_white > n_black: winner = 'player2'
        else:                   winner = 'draw'

        board_state = self.get_board_state()

        return winner, n_black, n_white, board_state



if __name__ == '__main__':
    a = Board()

