# status = DONE

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

POINT_COUNT = 5000
HEIGHT = 500
WIDTH = 500


def draw_body(start_x, start_y, width, height):
    bottom_left = (start_x, start_y)
    bottom_right = (start_x + width, start_y)
    top_left = (start_x, start_y + height)
    top_right = (start_x + width, start_y + height)

    glBegin(GL_TRIANGLES)

    glColor3f(0, 0, 1)
    glVertex2f(*bottom_left)
    glVertex2f(*bottom_right)
    glVertex2f(*top_right)

    glVertex2f(*top_right)
    glVertex2f(*top_left)
    glVertex2f(*bottom_left)
    glEnd()

    return top_right, top_left


def top_cone(top_right, top_left, center):
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2f(*top_right)
    glVertex2f(*top_left)
    glVertex2f(*center)
    glEnd()


def draw_line(start, end):
    glBegin(GL_LINES)
    glColor3f(1, 0, 1)
    glVertex2f(*start)
    glVertex2f(*end)
    glEnd()


def draw_window(start_x, start_y, width, height):
    bottom_left = (start_x, start_y)
    bottom_right = (start_x + width, start_y)
    top_left = (start_x, start_y + height)
    top_right = (start_x + width, start_y + height)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(*bottom_left)
    glVertex2f(*bottom_right)
    glVertex2f(*top_right)

    glVertex2f(*top_right)
    glVertex2f(*top_left)
    glVertex2f(*bottom_left)
    glEnd()


def draw_door(start_x, start_y, width, height):
    bottom_left = (start_x, start_y)
    bottom_right = (start_x + width, start_y)
    top_left = (start_x, start_y + height)
    top_right = (start_x + width, start_y + height)

    glBegin(GL_TRIANGLES)
    glColor3f(1, 0.4, 0.4)
    glVertex2f(*bottom_left)
    glVertex2f(*bottom_right)
    glVertex2f(*top_right)

    glVertex2f(*top_right)
    glVertex2f(*top_left)
    glVertex2f(*bottom_left)
    glEnd()


def draw_door_nob(start_x, start_y, width, height):
    bottom_left = (start_x, start_y)
    bottom_right = (start_x + width, start_y)
    top_left = (start_x, start_y + height)
    top_right = (start_x + width, start_y + height)

    glBegin(GL_TRIANGLES)

    glColor3f(0, 0, 1)
    glVertex2f(*bottom_left)
    glColor3f(0, 0.4, 0)
    glVertex2f(*bottom_right)
    glColor3f(1, 0, 0)
    glVertex2f(*top_right)

    glColor3f(1, 0, 0)
    glVertex2f(*top_right)
    glColor3f(0, 0.4, 0)
    glVertex2f(*top_left)
    glColor3f(0, 0, 1)
    glVertex2f(*bottom_left)
    glEnd()


def task(point_size=3):
    glPointSize(point_size)

    width, height = 400, 300
    start_x, start_y = 50, 10

    top_right, top_left = draw_body(start_x, start_y, width, height)

    center = (WIDTH / 2, start_y + height + 180)
    top_cone(top_right, top_left, center)

    draw_line(top_right, top_left)

    # both window
    draw_window(start_x + 50, start_y + 170, 100, 100)
    draw_window(start_x + 250, start_y + 170, 100, 100)

    draw_door(start_x + 150, start_y, 100, 150)

    draw_door_nob(start_x + 150 + 80, start_y + 50, 10, 10)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    ## error due to type issue.
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # call the draw methods here
    task()
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
    main()
