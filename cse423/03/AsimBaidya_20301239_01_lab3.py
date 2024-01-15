import sys
from math import sqrt
from random import random, seed

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WIDTH = 1920 // 1
HEIGHT = 1080 // 1
MARGIN = 10


def mid_point_circle(i_x: int, i_y: int, radius: int, point_size=3):
    """
    initiliztion of basic variables
    """
    x = 0
    y = radius
    d = 1 - radius

    # the mid_point_circle algorithm from slides :)
    while x < y:
        x += 1

        if d < 0:
            # right only
            d += 2 * x + 1
        else:
            # down and right
            y -= 1
            d += 2 * (x - y) + 1

        # finding all the zones
        zones = [
            (x + i_x, y + i_y),
            (x + i_x, -y + i_y),
            (-x + i_x, y + i_y),
            (-x + i_x, -y + i_y),
            (y + i_x, x + i_y),
            (y + i_x, -x + i_y),
            (-y + i_x, x + i_y),
            (-y + i_x, -x + i_y),
        ]

        # printing points on screen on each iteration

        glPointSize(point_size)
        glBegin(GL_POINTS)
        for z in zones:
            glVertex2f(z[0], z[1])
        glEnd()


def lab_task_3():
    #
    global WIDTH, HEIGHT, MARGIN

    # center point & appropriate radius calculation
    x_cnt = WIDTH // 2
    y_cnt = HEIGHT // 2
    r_l = (min(WIDTH, HEIGHT) // 2) - MARGIN
    r_s = r_l // 2

    x_dig = 0
    y_dig = 0

    # finding intermediate point in diagonal direction
    # !!probably better solution exis
    while sqrt(x_dig**2 + y_dig**2) < r_s:
        x_dig += 1
        y_dig += 1

    circles = [
        (x_cnt + r_l // 2, y_cnt, r_s),
        (x_cnt - r_l // 2, y_cnt, r_s),
        (x_cnt, y_cnt + r_l // 2, r_s),
        (x_cnt, y_cnt - r_l // 2, r_s),
        (x_cnt + x_dig, y_cnt + y_dig, r_s),
        (x_cnt - x_dig, y_cnt + y_dig, r_s),
        (x_cnt + x_dig, y_cnt - y_dig, r_s),
        (x_cnt - x_dig, y_cnt - y_dig, r_s),
        (x_cnt, y_cnt, r_l),
    ]

    # printing all required circles
    for x, y, r in circles:
        RED, GREEN, BLUE = random(), random(), random()
        glColor3f(RED, GREEN, BLUE)  # konokichur color set (RGB)
        mid_point_circle(x, y, r)

    # center location as red
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x_cnt, y_cnt)
    glEnd()


def lab_three():
    # mid_point_circle(300, 300, 100)
    lab_task_3()


def iterate():
    global WIDTH, HEIGHT
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WIDTH, 0.0, HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # calling lab_two
    lab_three()

    glutSwapBuffers()


def main():
    global HEIGHT, WIDTH
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WIDTH, HEIGHT)  # window size
    glutInitWindowPosition(0, 0)

    # (important for xmonad to ingnore tiling)
    wind = glutCreateWindow(b"opengl")

    glutDisplayFunc(showScreen)

    glutMainLoop()


if __name__ == "__main__":
    # seed(42)
    main()
