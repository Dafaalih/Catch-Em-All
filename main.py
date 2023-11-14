from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from labirin import *
from char import *
from texture import *
from collision import *

menu = 1
pos_x = 0
pos_y = 0

carModel = car()
data = [maze1[i].get_vertices() for i in range(len(maze1))]
col = collision(carModel, data)

    
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, 1200, 0, 700, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    load_texture()


def display():

    if menu == 1:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        cen = carModel.center()
            # projection is related to center of car , we need the center of the car to be the center of the screen
        # glOrtho(cen[0] - 300, cen[0] + 300, cen[1] - 175, cen[1] + 175, -1, 1)
        glOrtho(0, 1200, 0, 700, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.2, 0.2, 0)
        # draw_grid()  # Jika Anda ingin menampilkan grid

        draw_map()  # Gambar labirin
        draw_coins()  # Gambar koin
        draw_healthkit()  # Gambar kit kesehatan
        draw_bombs()  # Gambar bom
        draw_finish()  # Gambar finish line
        carModel.draw()
        glutSwapBuffers()  # Tukar buffer untuk menampilkan gambar

        glPushMatrix()
        col.collosion_walls_horizontal()
        col.collosion_walls_vertical()
        col.item_collisiom(coins1)
        col.item_collisiom(bombs1)
        col.item_collisiom(health1)
        glPopMatrix()

        glFlush()

def input_keyboard(key,x,y):
    global pos_x, pos_y

    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        carModel.move_to_top()   
    elif key == GLUT_KEY_DOWN:
        carModel.move_to_bottom()
    elif key == GLUT_KEY_RIGHT:
        carModel.move_to_right()
    elif key == GLUT_KEY_LEFT:
        carModel.move_to_left()

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
