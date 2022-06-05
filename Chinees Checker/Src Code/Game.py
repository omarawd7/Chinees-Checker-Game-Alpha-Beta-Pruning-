import sys

import random


from Controller_1 import *
from Controller_2 import *
from GUI import *


def start_game(level, caption):
    human_turn = 4
    ai_turn = 1
    player_turn = human_turn
    win = ai_turn
    board = build_board()
    p1_home, p2_home, p3_home, p4_home, p5_home, p6_home = build_home()
    p1_goal, p2_goal, p3_goal, p4_goal, p5_goal, p6_goal = build_goal()
    screen = init_board(caption)

    game_over = False
    first_round = True

    moves = []
    current = []
    while not game_over:
        is_moved = False
        pg.display.update()
        draw_board(board, screen)
        if player_turn == ai_turn:
            all_legal_moves = find_Ai_legal_moves(board, p1_home, p1_goal)
            print("AI Thinking....")
            if first_round:
                best_move_index = random.randint(0, len(all_legal_moves) - 1)
                best_move = all_legal_moves[best_move_index]
                first_round = False
            else:
                best_move = find_best_move(board, all_legal_moves, p1_goal, player_turn, level, p1_home,
                                           p1_home, p2_home, p3_home, p4_home, p5_home,
                                           p6_home)
            if best_move is None:
                break

            highlight_best_move(best_move, screen)
            pg.display.update()

            board, p1_home = do_move(board, best_move, p1_home)
            pg.display.update()
            p1_home, p2_home, p3_home, p4_home, p5_home, p6_home = \
                update_playerHome(p1_home, player_turn, p1_home, p2_home, p3_home, p4_home, p5_home, p6_home)
            pg.display.update()
            game_over = check_win(p1_home, p1_goal)
            player_turn = human_turn
            print("AI move from (", best_move[0], ") to (", best_move[1], ")")
        else:
            for event in pg.event.get():
                if event.type == 256:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    circle_x, circle_y = find_circle_from2(pos[0], pos[1])
                    if [circle_x, circle_y] in p4_home:
                        moves = all_legalMoves1(board, [[circle_x, circle_y]])
                        if len(moves) == 0:
                            continue
                        print(moves)
                        highlight_legal_moves(moves, screen)
                        pg.display.update()
                        pg.time.wait(1500)
                        current = [circle_x, circle_y]
                    if [current, [circle_x, circle_y]] in moves:
                        board, p4_home = do_move(board, [current, [circle_x, circle_y]], p4_home)
                        pg.display.update()
                        print("you move from (",current," ) to (", [circle_x,circle_y]," )")
                        game_over = check_win(p4_home, p4_goal)
                        if game_over:
                            win = human_turn
                        game_over = check_win(p4_home, p4_goal)
                        is_moved = True
                        current = []
                        moves = []
                    pg.display.update()
            if is_moved:
                player_turn = ai_turn
                pg.display.update()
    return win
