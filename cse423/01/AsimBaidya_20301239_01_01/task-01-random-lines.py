# status = DONE

from random import randint, random, seed

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

POINT_COUNT = 50
HEIGHT = 500
WIDTH = 500


def random_point():
    global POINT_COUNT
    x, y = randint(0, WIDTH), randint(0, HEIGHT)
    r, g, b = random(), random(), random()
    glBegin(GL_POINTS)
    glColor3f(r, g, b)  # konokichur color set (RGB)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def task(point_size=40):
    glPointSize(point_size)

    for _ in range(POINT_COUNT):
        random_point()


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
    seed(42)
    main()
