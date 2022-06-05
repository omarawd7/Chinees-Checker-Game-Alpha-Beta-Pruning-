import numpy as np
from AlphaBeta_Algorithm import alphabeta


def build_board():
    board = np.zeros((17, 25))

    board[:][:] = -1

    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9] = 1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

    board[4][18] = 0
    board[4][20] = 0
    board[4][22] = 0
    board[4][24] = 0
    board[5][19] = 0
    board[5][21] = 0
    board[5][23] = 0
    board[6][20] = 0
    board[6][22] = 0
    board[7][21] = 0

    board[9][21] = 0
    board[10][20] = 0
    board[10][22] = 0
    board[11][19] = 0
    board[11][21] = 0
    board[11][23] = 0
    board[12][18] = 0
    board[12][20] = 0
    board[12][22] = 0
    board[12][24] = 0

    board[13][9] = 4
    board[13][11] = 4
    board[13][13] = 4
    board[13][15] = 4
    board[14][10] = 4
    board[14][12] = 4
    board[14][14] = 4
    board[15][11] = 4
    board[15][13] = 4
    board[16][12] = 4

    board[9][21 - 18] = 0
    board[10][20 - 18] = 0
    board[10][22 - 18] = 0
    board[11][19 - 18] = 0
    board[11][21 - 18] = 0
    board[11][23 - 18] = 0
    board[12][18 - 18] = 0
    board[12][20 - 18] = 0
    board[12][22 - 18] = 0
    board[12][24 - 18] = 0

    board[4][18 - 18] = 0
    board[4][20 - 18] = 0
    board[4][22 - 18] = 0
    board[4][24 - 18] = 0
    board[5][19 - 18] = 0
    board[5][21 - 18] = 0
    board[5][23 - 18] = 0
    board[6][20 - 18] = 0
    board[6][22 - 18] = 0
    board[7][21 - 18] = 0

    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0

    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0

    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0

    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0

    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0

    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

    board[12][8] = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


def find_best_move(board, all_legal_moves, goal, player_turn, level, home_pieces, p1_home, p2_home, p3_home,
                   p4_home, p5_home, p6_home):
    goal_left = [i for i in goal + home_pieces if i not in goal or i not in home_pieces]
    if len(goal_left) == 2:
        for move in all_legal_moves:
            start_move = move[0]
            end_move = move[1]
            if start_move == goal_left[1] and end_move == goal_left[0]:
                return move
    try:
        score, best_move = alphabeta(board, level, player_turn, player_turn, p1_home, p2_home,
                                     p3_home, p4_home, p5_home, p6_home, -1000, 1000)
    except Exception:
        return

    return best_move


def check_win(player_set, goal):
    game_end = True
    for piece in player_set:
        if piece not in goal:
            game_end = False

    return game_end
