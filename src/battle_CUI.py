from envs.board import Board
from agents.human import Human
from agents.randomer import Randomer



def main():
    field = Board()
    field.render()

    player1 = Randomer()
    player2 = Randomer()
    players = (player1, player2)

    field.setup_player(player1)
    field.setup_player(player2)
    
    turn = 0
    while not field.is_game_set():
        player = players[turn%2]
        color = player.get_piece_color()
        turn += 1
        
        if not field.exist_legal_move(color):
            continue

        player.update(field.get_board_state())

        put_pos = (0, 0)
        while not field.can_be_put(color, put_pos):
            put_pos = player.move()

        field.put_a_piece(color, put_pos)
        
        field.render()
    
    winner, n_black, n_white, last_field = field.get_game_result()
    print(winner + ' is winner.')
    print('black:' + str(n_black))
    print('white:' + str(n_white))
    print(last_field)


        
if __name__ == '__main__':
    main()
