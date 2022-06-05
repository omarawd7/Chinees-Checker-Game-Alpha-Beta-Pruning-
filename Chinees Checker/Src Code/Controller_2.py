import math

import numpy as np

visit = 20
no_visit = 15


def build_home():
    p1_home = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
    p2_home = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
    p3_home = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
    p4_home = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]
    p5_home = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
    p6_home = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]

    return p1_home, p2_home, p3_home, p4_home, p5_home, p6_home


def build_goal():
    p1_goal = [[16, 12], [15, 11], [15, 13], [14, 10], [14, 14], [14, 12], [13, 9], [13, 15], [13, 13], [13, 11]]
    p2_goal = [[12, 0], [11, 1], [12, 2], [10, 2], [12, 4], [11, 3], [9, 3], [12, 6], [11, 5], [10, 4]]
    p3_goal = [[4, 0], [4, 2], [5, 1], [4, 4], [6, 2], [5, 3], [4, 6], [7, 3], [6, 4], [5, 5]]
    p4_goal = [[0, 12], [1, 13], [1, 11], [2, 14], [2, 10], [2, 12], [3, 15], [3, 9], [3, 11], [3, 13]]
    p5_goal = [[4, 24], [5, 23], [4, 22], [6, 22], [4, 20], [5, 21], [7, 21], [4, 18], [5, 19], [6, 20]]
    p6_goal = [[12, 24], [12, 22], [11, 23], [12, 20], [10, 22], [11, 21], [12, 18], [9, 21], [10, 20], [11, 19]]

    return p1_goal, p2_goal, p3_goal, p4_goal, p5_goal, p6_goal


def set_homes(player_turn, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home):
    assign_player = p1_home
    if player_turn == 1: assign_player = p1_home
    if player_turn == 2: assign_player = p2_home
    if player_turn == 3: assign_player = p3_home
    if player_turn == 4: assign_player = p4_home
    if player_turn == 5: assign_player = p5_home
    if player_turn == 6: assign_player = p6_home

    return assign_player


def set_goal(player_turn, p1_goal, p2_goal, p3_goal, p4_goal, p5_goal, p6_goal):
    assign_goal = p1_goal
    if player_turn == 1: assign_goal = p1_goal
    if player_turn == 2: assign_goal = p2_goal
    if player_turn == 3: assign_goal = p3_goal
    if player_turn == 4: assign_goal = p4_goal
    if player_turn == 5: assign_goal = p5_goal
    if player_turn == 6: assign_goal = p6_goal

    return assign_goal


def update_playerHome(player_set, player_turn, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home):
    if player_turn == 1: p1_home = player_set
    if player_turn == 2: p2_home = player_set
    if player_turn == 3: p3_home = player_set
    if player_turn == 4: p4_home = player_set
    if player_turn == 5: p5_home = player_set
    if player_turn == 6: p6_home = player_set

    return p1_home, p2_home, p3_home, p4_home, p5_home, p6_home


def all_legalMoves1(board, p_home):
    valid = []
    for home in p_home:
        color_board = np.full(board.shape, no_visit)
        valid = isMove(board, color_board, home, 0, home, valid)
    return valid

def valid_move_in_house(valid_moves, obj_set):
    moves_to_remove = []

    for valid_move in valid_moves:

        start_move = valid_move[0]
        end_move = valid_move[1]

        if start_move in obj_set:

            square_start_y = (start_move[1] * 14.43) / 25
            square_end_y = (end_move[1] * 14.43) / 25
            central_pos = (12 * 14.43) / 25

            start_diag = math.sqrt(((8 - start_move[0]) ** 2) + ((central_pos - square_start_y) ** 2))
            end_diag = math.sqrt(((8 - end_move[0]) ** 2) + ((central_pos - square_end_y) ** 2))

            if start_diag > end_diag:
                moves_to_remove.append(valid_move)

    new_valid_moves = [i for i in valid_moves + moves_to_remove if i not in valid_moves or i not in moves_to_remove]

    return new_valid_moves
def find_Ai_legal_moves(board,player_set, goal):
    valid_move = all_legalMoves1(board, player_set)
    valid_move = valid_move_in_house(valid_move,goal)
    p2_goal = [[12, 0], [11, 1], [12, 2], [10, 2], [12, 4], [11, 3], [9, 3], [12, 6], [11, 5], [10, 4]]
    p2_home = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
    p6_home = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]
    p6_goal = [[12, 24], [12, 22], [11, 23], [12, 20], [10, 22], [11, 21], [12, 18], [9, 21], [10, 20], [11, 19]]
    invalid_home = p2_home + p2_goal + p6_home + p6_goal
    valid_move = dont_stop_in_home(valid_move, invalid_home)
    return valid_move


def isMove(board, color_board, start, depth, origin, v_moves):
    [x_0, y_0] = start
    color_board[x_0][y_0] = visit

    neighbors = find_neighbors_from(start)

    for x_1, y_1 in neighbors:

        if depth == 0 and board[x_1][y_1] == 0:
            v_moves.append([start, [x_1, y_1]])

        if depth == 0 and board[x_1][y_1] > 0:
            x_2, y_2 = find_jump_between(start, x_1, y_1)
            if board[x_2][y_2] == 0:
                v_moves.append([start, [x_2, y_2]])
                v_moves = isMove(board, color_board, [x_2, y_2], depth + 1, origin, v_moves)

        if depth > 0 and board[x_1][y_1] > 0:
            x_2, y_2 = find_jump_between(start, x_1, y_1)
            if board[x_2][y_2] == 0 and color_board[x_2][y_2] == no_visit:
                v_moves.append([origin, [x_2, y_2]])
                v_moves = isMove(board, color_board, [x_2, y_2], depth + 1, origin, v_moves)

    return v_moves


def find_neighbors_from(point):
    [x, y] = point
    neighbors = []
    node = [x, y + 2]
    if 0 <= node[1] <= 24:
        neighbors.append([x, y + 2])
    node = [x, y - 2]
    if 0 <= node[1] <= 24:
        neighbors.append([x, y - 2])
    node = [x + 1, y + 1]
    if 0 <= node[0] <= 16 and 0 <= node[1] <= 24:
        neighbors.append([x + 1, y + 1])

    node = [x + 1, y - 1]
    if 0 <= node[0] <= 16 and 0 <= node[1] <= 24:
        neighbors.append([x + 1, y - 1])

    node = [x - 1, y + 1]
    if 0 <= node[0] <= 16 and 0 <= node[1] <= 24:
        neighbors.append([x - 1, y + 1])

    node = [x - 1, y - 1]
    if 0 <= node[0] <= 16 and 0 <= node[1] <= 24:
        neighbors.append([x - 1, y - 1])

    return neighbors


def find_jump_between(start, x_1, y_1):
    [start_x, start_y] = start

    x_2 = x_1 + (x_1 - start_x)
    y_2 = y_1 + (y_1 - start_y)

    if 0 <= x_2 <= 16 and 0 <= y_2 <= 24:
        return x_2, y_2
    else:
        return 0, 0


def dont_stop_in_home(valid_moves, invalid_homes_set):
    moves_to_remove = []

    for valid_move in valid_moves:
        end_move = valid_move[1]
        if end_move in invalid_homes_set:
            moves_to_remove.append(valid_move)

    new_valid_moves = [i for i in valid_moves + moves_to_remove if i not in valid_moves or i not in moves_to_remove]

    return new_valid_moves


def do_move(board, best_move, home_pieces):
    [begin_x, begin_y] = best_move[0]
    [finish_x, finish_y] = best_move[1]

    piece = board[begin_x][begin_y]
    board[begin_x][begin_y] = 0
    board[finish_x][finish_y] = piece

    piece_to_remove = [[begin_x, begin_y]]
    new_home_pieces = [i for i in home_pieces + piece_to_remove if i not in home_pieces or i not in piece_to_remove]
    new_home_pieces.append([finish_x, finish_y])

    return board, new_home_pieces
