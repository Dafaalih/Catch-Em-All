from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from labirin import *
from char import *

menu = 1
pos_x = 0
pos_y = 0

carModel = car()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, 1200, 0, 700, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():

    if menu == 1:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        cen = carModel.center()
            # projection is related to center of car , we need the center of the car to be the center of the screen
        glOrtho(cen[0] - 300, cen[0] + 300, cen[1] - 175, cen[1] + 175, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.2, 0.2, 0)
        # draw_grid()  # Jika Anda ingin menampilkan grid

        print("KIRII : ", carModel.left, " KANAN : " , carModel.right)
        print("ATAS : ", carModel.top, " BAWAH : " , carModel.bottom)
        draw_map()  # Gambar labirin
        draw_coins()  # Gambar koin
        draw_healthkit()  # Gambar kit kesehatan
        draw_bombs()  # Gambar bom
        draw_finish()  # Gambar finish line
        glutSwapBuffers()  # Tukar buffer untuk menampilkan gambar

        glPushMatrix()
        carModel.draw()
        glPopMatrix()

        glFlush()

def input_keyboard(key,x,y):
    global pos_x, pos_y

    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        carModel.top += 5
        carModel.bottom += 5   
    elif key == GLUT_KEY_DOWN:
        carModel.bottom -= 5
        carModel.top -= 5
    elif key == GLUT_KEY_RIGHT:
        carModel.right += 5
        carModel.left += 5
    elif key == GLUT_KEY_LEFT:
        carModel.left -= 5
        carModel.right -= 5

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def Timer(v):
    display()
    glutTimerFunc(10, Timer, 1)

def main():
    glutInit()
    glutInitWindowSize(1200, 700)
    glutCreateWindow(b"Maze Adventure")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    init()
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(10, Timer, 1)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
