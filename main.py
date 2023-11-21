from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from labirin import *
from char import *
from texture import *
from collision import *

menu = 0
pos_x = 0
pos_y = 0

carModel = car()
data = [maze1[i].get_vertices() for i in range(len(maze1))]
col = collision(carModel, data)

    
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    # glOrtho(0, 1200, 0, 700, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    load_texture()

def background(x1, y1, x2, y2, image):
        glBindTexture(GL_TEXTURE_2D, image)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2f(x1, y1)
        glTexCoord2f(1, 0)
        glVertex2f(x2, y1)
        glTexCoord2f(1, 1)
        glVertex2f(x2, y2)
        glTexCoord2f(0, 1)
        glVertex2f(x1, y2)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, -1)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if menu == 0:
        glClearColor(0.2, 0.2, 0.2, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1200, 0, 700, -1, 1)  # Adjusted for bottom-left origin
        glMatrixMode(GL_MODELVIEW)

        # Rendering code with y-coordinates adjusted for the bottom-left origin
        background(0, 0, 1200, 700, BG1)
        background(200, 500, 1000, 650, GAMENAME)
        if pos_y >= 288 and pos_y <= 370 and pos_x >= 480 and pos_x <= 720: 
            background(480, 320, 720, 420, PLAYCLICK)
        else:
            background(480, 320, 720, 420, PLAY)
            
        if pos_y >= 405 and pos_y <= 485 and pos_x >= 480 and pos_x <= 720:
            background(480, 200, 720, 300, OPTIONCLICK)
        else:
            background(480, 200, 720, 300, OPTION)

        if pos_y >= 528 and pos_y <= 610 and pos_x >= 480 and pos_x <= 720:
            background(480, 80, 720, 180, QUITCLICK)
        else:
            background(480, 80, 720, 180, QUIT)

        print("Posisi X: ", pos_x)
        print("Posisi Y: ", pos_y)


        glFlush()
        glutSwapBuffers()
    elif menu == 1:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        cen = carModel.center()
            # projection is related to center of car , we need the center of the car to be the center of the screen
        glOrtho(cen[0] - 300, cen[0] + 300, cen[1] - 175, cen[1] + 175, -1, 1)
        # glOrtho(0, 1200, 0, 700, -1, 1)
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
        # glutSwapBuffers()  # Tukar buffer untuk menampilkan gambar

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

def trackingMouse(x, y):
    global pos_x , pos_y
    pos_x = x
    pos_y = y

def mouse(state,key, x , y):
    global menu

    if y >= 288 and y <= 370 and x >= 480 and x <= 720 and key == GLUT_LEFT_BUTTON and menu == 0:
        menu = 1


def main():
    glutInit()
    glutInitWindowSize(1200, 700)
    glutCreateWindow(b"Maze Adventure")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA|GLUT_DEPTH)
    init()
    glutSpecialFunc(input_keyboard)
    glutPassiveMotionFunc(trackingMouse)
    glutTimerFunc(10, Timer, 1)
    glutMouseFunc(mouse)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
