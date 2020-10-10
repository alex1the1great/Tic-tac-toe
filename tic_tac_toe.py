from colored import fg, attr
from random import choice

board = {
    'top_L': ' ', 'top_M': ' ', 'top_R': ' ', 'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ', 'low_L': ' ', 'low_M': ' ', 'low_R': ' '
}


def print_board(tic_board):
    print(tic_board['top_L'] + '|' + tic_board['top_M'] + '|' + tic_board['top_R'])
    print('-+-+-')
    print(tic_board['mid_L'] + '|' + tic_board['mid_M'] + '|' + tic_board['mid_R'])
    print('-+-+-')
    print(tic_board['low_L'] + '|' + tic_board['low_M'] + '|' + tic_board['low_R'])


def check_available_option(tic_board):
    for key, value in tic_board.items():
        if not value or value == ' ':
            print(key, end=', ')


def all_space_occupied(tic_board):
    if ' ' not in tic_board.values():
        global game_loop
        game_loop = False


def check_winner(board, last_move_player):
    global match_draw
    match_draw = False
    if (board['top_L'] == last_move_player
            and board['top_M'] == last_move_player
            and board['top_R'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['mid_L'] == last_move_player
            and board['mid_M'] == last_move_player
            and board['mid_R'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['low_L'] == last_move_player
            and board['low_M'] == last_move_player
            and board['low_R'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['top_L'] == last_move_player
            and board['mid_L'] == last_move_player
            and board['low_L'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['top_M'] == last_move_player
            and board['mid_M'] == last_move_player
            and board['low_M'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['top_R'] == last_move_player
            and board['mid_R'] == last_move_player
            and board['low_R'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['top_L'] == last_move_player
            and board['mid_M'] == last_move_player
            and board['low_R'] == last_move_player):
        print(display_winner(last_move_player))
    elif (board['top_R'] == last_move_player
            and board['mid_M'] == last_move_player
            and board['low_L'] == last_move_player):
        print(display_winner(last_move_player))
    else:
        match_draw = True


def display_winner(winner):
    global game_loop
    game_loop = False
    return f'{fg(2)}Player {winner} won!!!{attr(0)}'


turn = choice(['X', 'O'])  # select random player turn.
game_loop = True
while game_loop:
    print_board(board)

    # print available space names.
    print('-' * 70)  # for UI
    print('Avialable option:')
    check_available_option(board)
    print()  # for UI
    print('-' * 70)  # for UI

    move = input(f'{fg(4)}Turn for {fg(5)}{turn}{attr(0)}{fg(4)}. Move on which space? {attr(0)}')

    try:
        # check space available.
        # add new value or print space not available.
        if board[move] == ' ':
            board[move] = turn
        else:
            print(f'{fg(1)}Space not available. Try new space.{attr(0)}')
            continue

        # check winner
        check_winner(board, turn)
    except KeyError:
        print(f'{fg(1)}Invalid space name.{attr(0)}')
        continue

    # for denoting whose turn is now.
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    # check all space occupied
    all_space_occupied(board)

print_board(board)

if match_draw:
    print(f'{fg(11)}Match Draw.{attr(0)}')
