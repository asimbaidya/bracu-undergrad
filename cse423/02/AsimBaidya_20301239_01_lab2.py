import sys
from random import random, seed

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WIDTH = 1920
HEIGHT = 1080

# for asthetic make sure width is > size
FONT_SIZE = 30
FONT_WIDTH = 30
DIGIT_TO_PRINT = 2


def findZone(x0: int, y0: int, x1: int, y1: int):
    d_y = y1 - y0
    d_x = x1 - x0

    if abs(d_x) > abs(d_y):
        if d_x > 0:
            return 0 if d_y > 0 else 7
        else:
            return 3 if d_y > 0 else 4
    else:
        if d_y > 0:
            return 1 if d_x > 0 else 2
        else:
            return 5 if d_x > 0 else 6


def c_to_zone_zero(zone: int, x: int, y: int):
    conversions = [
        (x, y),
        (y, x),
        (y, -x),
        (-x, y),
        (-x, -y),
        (-y, -x),
        (-y, x),
        (x, -y),
    ]

    if zone >= len(conversions):
        glutDestroyWindow(glutGetWindow())
        raise Exception("Zone is out of range")
    return conversions[zone]


def c_from_zone_zero(zone: int, x: int, y: int):
    conversions = [
        (x, y),
        (y, x),
        (-y, -x),
        (-x, y),
        (-x, -y),
        (-y, -x),
        (y, -x),
        (x, -y),
    ]

    if zone >= len(conversions):
        glutDestroyWindow(glutGetWindow())
        raise Exception("Zone is out of range")
    return conversions[zone]


def mid_point_points(zone, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    d = 2 * dy - dx
    x, y = x1, y1

    while x <= x2:
        a, b = c_from_zone_zero(zone, x, y)
        glBegin(GL_POINTS)
        glVertex2f(a, b)
        glEnd()

        x += 1
        d = d + dy if d < 0 else d + (dy - dx)
        y += 1 if d >= 0 else 0


def mid_point_line(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)

    z_x0, z_y0 = c_to_zone_zero(zone, x0, y0)
    z_x1, z_y1 = c_to_zone_zero(zone, x1, y1)

    mid_point_points(zone, z_x0, z_y0, z_x1, z_y1)


def draw_line(start, end):
    mid_point_line(*start, *end)


def generate_digits_coordinates(start_x, start_y, width, height):
    mid_y = height / 2

    a = (start_x, start_y)
    b = (start_x + width, start_y)
    c = (start_x, start_y + mid_y)
    d = (start_x + width, start_y + mid_y)
    e = (start_x, start_y + height)
    f = (start_x + width, start_y + height)
    pa = (start_x + int(width * 0.3), start_y)
    pc = (start_x + int(width * 0.2), start_y + mid_y + int(mid_y * 0.5))

    return [a, b, c, d, e, f, pa, pc]


def generate_digits_line(digits):
    a, b, c, d, e, f, pa, pc = digits
    digit_lines = {
        "0": [(e, a), (e, f), (f, b), (a, b)],
        "1": [(pc, f), (f, b)],
        "2": [(e, f), (f, d), (c, d), (c, a), (a, b)],
        "3": [(e, f), (f, d), (c, d), (d, b), (a, b)],
        "4": [(e, c), (c, d), (f, b)],
        "5": [(e, f), (e, c), (c, d), (d, b), (a, b)],
        "6": [(e, f), (e, a), (a, b), (d, b), (c, d)],
        "7": [(e, f), (f, pa)],
        "8": [(e, a), (e, f), (f, b), (a, b), (c, d)],
        "9": [(c, d), (e, c), (e, f), (f, b), (a, b)],
    }

    return digit_lines


def input_id() -> str:
    """
    >>> will work if input it 0, but if 01 is given as input, it will
    >>> show 1 in the output window, as 01 wil be converted as 1 in
    >>> input c if input takes as inter
    """

    n = int(input("Enter your ID: "))

    if n == 0:
        return "0"

    s = ""
    count = 0

    while n != 0 and count < DIGIT_TO_PRINT:
        s = str(n % 10) + s
        n //= 10
        count += 1

    return s


def lab_two(my_id=input_id()):
    global FONT_SIZE
    global FONT_WIDTH
    global WIDTH
    global HEIGHT
    glPointSize(FONT_WIDTH)

    width_i = 5
    height_i = 10

    width = width_i * FONT_SIZE
    height = height_i * FONT_SIZE

    gap = max(width * 0.4 + FONT_WIDTH * 0.1, 2)
    # gap = width * 0.8 + FONT_WIDTH * 0.1
    # print(width * 0.2 * FONT_WIDTH * 0.1)

    # lets print at center
    """
    >>> this will help to print the id at the center of the window
    """
    total_width = (width * DIGIT_TO_PRINT) + (gap * (DIGIT_TO_PRINT - 1))
    total_height = height
    start_x = (WIDTH - total_width) / 2
    start_y = (HEIGHT - total_height) / 2

    if total_width > WIDTH or total_height > HEIGHT:
        glutDestroyWindow(glutGetWindow())
        raise Exception("Content can not be shown in this window size")

    for d in my_id:
        r, g, b = random(), random(), random()
        glColor3f(r, g, b)  # konokichur color set (RGB)

        digits = generate_digits_coordinates(start_x, start_y, width, height)
        line_maps = generate_digits_line(digits)
        lines = line_maps[d]
        for line in lines:
            draw_line(*line)

        start_x += width + gap


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
    lab_two()

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
