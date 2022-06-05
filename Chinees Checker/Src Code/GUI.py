import pygame as pg

# BACKGROUND
back = pg.image.load('background.jpg')
EMPTY_CELL = (213, 192, 155)
# Green
HUMAN_COLOR = (0, 250, 0)
# Red
AI_COLOR = (250, 0, 37)
# HIGHLIGHT
HUMAN_HIGHLIGHT = (0, 255, 255)
AI_HIGHLIGHT = (5, 5, 5)

# Constants of board
H_MARGIN_DISTANCE = 20
V_MARGIN_DISTANCE = 20
CIRCLE_RADIUS = 20
CIRCLE_DIAMETER = 2 * CIRCLE_RADIUS
H_SPACING = 8
V_SPACING = 1
WINDOW_WIDTH = (H_MARGIN_DISTANCE * 2) + (CIRCLE_DIAMETER * 13) + (H_SPACING * 12)
WINDOW_HEIGHT = (V_MARGIN_DISTANCE * 2) + (CIRCLE_DIAMETER * 17) + (V_SPACING * 16)


def init_board(caption):
    pg.init()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption(caption)
    return screen


def draw_board(board, screen):
    screen.blit(back, (0, 0))

    y_coord = V_MARGIN_DISTANCE + CIRCLE_RADIUS

    for row in range(0, 17):

        x_coord_long = H_MARGIN_DISTANCE + CIRCLE_RADIUS
        x_coord_short = int(H_MARGIN_DISTANCE + CIRCLE_DIAMETER + (H_SPACING / 2))

        for circle_in_a_row in range(0, 13):
            if row % 2 == 0:

                board_value = board[row][circle_in_a_row * 2]

                color_circle(board_value, screen, x_coord_long, y_coord)

                x_coord_long = x_coord_long + CIRCLE_DIAMETER + H_SPACING

            elif row % 2 != 0 and circle_in_a_row != 12:

                board_value = board[row][circle_in_a_row * 2 + 1]
                color_circle(board_value, screen, x_coord_short, y_coord)

                x_coord_short = x_coord_short + CIRCLE_DIAMETER + H_SPACING

        y_coord = y_coord + CIRCLE_DIAMETER + V_SPACING


def color_circle(board_value, display_surface, x_coord, y_coord):
    if board_value == 0:
        pg.draw.circle(display_surface, EMPTY_CELL, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 1:
        pg.draw.circle(display_surface, AI_COLOR, (x_coord, y_coord), CIRCLE_RADIUS, 0)
    if board_value == 4:
        pg.draw.circle(display_surface, HUMAN_COLOR, (x_coord, y_coord), CIRCLE_RADIUS, 0)


def highlight_best_move(best_move, display_surface):
    [start_x, start_y] = best_move[0]
    [end_x, end_y] = best_move[1]

    circle_start_x, circle_start_y = find_circle_from(start_x, start_y)
    pg.draw.ellipse(display_surface, AI_HIGHLIGHT, (circle_start_x - CIRCLE_RADIUS, circle_start_y - CIRCLE_RADIUS,
                                                    CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)

    circle_end_x, circle_end_y = find_circle_from(end_x, end_y)
    pg.draw.ellipse(display_surface, AI_HIGHLIGHT, (circle_end_x - CIRCLE_RADIUS, circle_end_y - CIRCLE_RADIUS,
                                                    CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)


def highlight_legal_moves(moves, display_surface):
    for move in moves:
        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]
        circle_end_x, circle_end_y = find_circle_from(start_x, start_y)
        pg.draw.ellipse(display_surface, AI_COLOR, (circle_end_x - CIRCLE_RADIUS, circle_end_y - CIRCLE_RADIUS,
                                                    CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)
        circle_end_x, circle_end_y = find_circle_from(end_x, end_y)
        pg.draw.ellipse(display_surface, HUMAN_HIGHLIGHT, (circle_end_x - CIRCLE_RADIUS, circle_end_y - CIRCLE_RADIUS,
                                                           CIRCLE_DIAMETER, CIRCLE_DIAMETER), 5)


def find_circle_from(x, y):
    if x % 2 == 0:
        circle_x = int(H_MARGIN_DISTANCE + CIRCLE_RADIUS + (CIRCLE_DIAMETER + H_SPACING) * (y / 2))
    else:
        circle_x = int(H_MARGIN_DISTANCE + CIRCLE_DIAMETER + (H_SPACING / 2) + (CIRCLE_DIAMETER + H_SPACING) * ((y - 1)
                                                                                                                / 2))
    circle_y = V_MARGIN_DISTANCE + CIRCLE_RADIUS + (CIRCLE_DIAMETER + V_SPACING) * x

    return circle_x, circle_y


def find_circle_from2(x, y):
    circle_x = int((y - H_MARGIN_DISTANCE) / (CIRCLE_DIAMETER + V_SPACING))
    circle_y = int(2 * (x - V_MARGIN_DISTANCE) / (CIRCLE_DIAMETER + H_SPACING))
    return circle_x, circle_y
