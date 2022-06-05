from Controller_2 import *
import copy
import math

p1_home, p2_home, p3_home, p4_home, p5_home, p6_home = build_home()
p1_goal, p2_goal, p3_goal, p4_goal, p5_goal, p6_goal = build_goal()


def alphabeta(board, depth, player, first_player, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home, alpha, beta):
    board_copy = board[:][:]

    if depth == 0:
        board_score = calculate_board_score(first_player, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home)
        return board_score, None

    set_pieces = set_homes(player, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home)

    obj_set = set_goal(player, p1_goal, p2_goal, p3_goal, p4_goal, p5_goal, p6_goal)

    valid_moves = find_Ai_legal_moves(board_copy, set_pieces, obj_set)

    scores = []
    moves = []

    if player == first_player:
        for move in valid_moves:
            board_copy_again = copy.copy(board_copy)
            new_board, new_set_pieces = do_move(board_copy_again, move, set_pieces)

            p1_home, p2_home, p3_home, p4_home, p5_home, p6_home = \
                update_playerHome(new_set_pieces, player, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home)

            next_player = player + 3
            if next_player == 7:
                next_player = 1

            score, something = alphabeta(new_board, depth - 1, next_player, first_player, p1_home, p2_home,
                                         p3_home, p4_home, p5_home, p6_home, alpha, beta)

            scores.append(score)
            moves.append(move)
            alpha = max(score, alpha)
            if beta <= alpha:
                break

        if len(scores) == 0:
            return
        max_score_index = scores.index(max(scores))
        best_move = moves[max_score_index]
        return scores[max_score_index], best_move

    else:

        for move in valid_moves:
            board_copy_again = copy.copy(board_copy)
            new_board, new_set_pieces = do_move(board_copy_again, move, set_pieces)
            p1_home, p2_home, p3_home, p4_home, p5_home, p6_home = \
                update_playerHome(new_set_pieces, player, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home)

            next_player = player + 3
            if next_player == 7:
                next_player = 1

            score, something = alphabeta(new_board, depth - 1, next_player, first_player, p1_home, p2_home,
                                         p3_home, p4_home, p5_home, p6_home, alpha, beta)

            scores.append(score)
            moves.append(move)
            beta = min(score, beta)
            if beta <= alpha:
                break

        if len(scores) == 0:
            return
        min_score_index = scores.index(min(scores))
        worst_opponent_move = moves[min_score_index]

        return scores[min_score_index], worst_opponent_move


def calculate_board_score(player_turn, p1_pieces, p2_pieces, p3_pieces, p4_pieces, p5_pieces, p6_pieces):
    p1_avg_distance = heuristic(p1_pieces, p1_goal, 16, 12)
    p2_avg_distance = heuristic(p2_pieces, p2_goal, 12, 0)
    p3_avg_distance = heuristic(p3_pieces, p3_goal, 4, 0)
    p4_avg_distance = heuristic(p4_pieces, p4_goal, 0, 12)
    p5_avg_distance = heuristic(p5_pieces, p5_goal, 4, 24)
    p6_avg_distance = heuristic(p6_pieces, p6_goal, 12, 24)
    score = calc_score(player_turn, p1_avg_distance, p2_avg_distance, p3_avg_distance, p4_avg_distance,
                       p5_avg_distance, p6_avg_distance)
    return score


def heuristic(p_pieces, p_obj, p_default_x, p_default_y):
    total_distance = 0
    obj_x = p_default_x
    obj_y = p_default_y
    for obj_piece in p_obj:
        if obj_piece not in p_pieces:
            [obj_x, obj_y] = obj_piece
            break

    for piece in p_pieces:
        [x, y] = piece

        square_y = (y * 14.43) / 25
        square_obj_y = (obj_y * 14.43) / 25

        distance_diag = math.sqrt(((obj_x - x) ** 2) + ((square_obj_y - square_y) ** 2))

        total_distance = total_distance + distance_diag

    avg_distance = total_distance / 10

    return avg_distance


def calc_score(player_turn, p1_avg_distance, p2_avg_distance, p3_avg_distance, p4_avg_distance, p5_avg_distance, p6_avg_distance):
    if player_turn == 1:
        p_turn_avg_distance = p1_avg_distance
        score = ((p2_avg_distance - p_turn_avg_distance) +
                 (p3_avg_distance - p_turn_avg_distance) +
                 (p4_avg_distance - p_turn_avg_distance) +
                 (p5_avg_distance - p_turn_avg_distance) +
                 (p6_avg_distance - p_turn_avg_distance)) / 5

    else:
        p_turn_avg_distance = p4_avg_distance
        score = ((p2_avg_distance - p_turn_avg_distance) +
                 (p3_avg_distance - p_turn_avg_distance) +
                 (p1_avg_distance - p_turn_avg_distance) +
                 (p5_avg_distance - p_turn_avg_distance) +
                 (p6_avg_distance - p_turn_avg_distance)) / 5
    return score
