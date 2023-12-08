from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from labirin import *
from char import *
from texture import *
from collision import *
from model import *
import os

menu = 0
pos_x = 0
pos_y = 0
start_time = 0
gameover = 0
win = 0
onbutton = False
cek_background = 0


pygame.init()
sounds = [pygame.mixer.Sound("assets/sound/ingame.wav"),
          pygame.mixer.Sound("assets/sound/mouse_point.wav")
          ]

charModel = char()
data = [maze1[i].get_vertices() for i in range(len(maze1))]
col = collision(charModel, data)

    
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, 1200, 0, 700, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    load_texture()

def display():
    global menu, gameover, win , onbutton
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if menu == 0:
        glClearColor(0.2, 0.2, 0.2, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1200, 0, 700, -1, 1)  # Adjusted for bottom-left origin
        glMatrixMode(GL_MODELVIEW)

        # CHANGE COLOR BACKGROUND WHEN MOUSE IN AREA BUTTON
        background(0, 0, 1200, 700, BG1 if cek_background == 0 else BGSUNSET if cek_background == 1 else BGUMI if cek_background == 2 else None)
        background(200, 500, 1000, 650, GAMENAME)
        background(480, 320, 720, 420, PLAYCLICK if pos_x >= 480 and pos_x <= 720 and pos_y >= 320 and pos_y <= 420 else PLAY)
        background(480, 200, 720, 300, OPTIONCLICK if pos_x >= 480 and pos_x <= 720 and pos_y >= 200 and pos_y <= 300 else OPTION)
        background(480, 80, 720, 180, QUITCLICK if pos_x >= 480 and pos_x <= 720 and pos_y >= 80 and pos_y <= 180 else QUIT)

        glFlush()
        glutSwapBuffers()
    elif menu == 1:
        glClearColor(0.2, 0.2, 0.2, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1200, 0, 700, 0, 1)  # Adjusted for bottom-left origin
        glMatrixMode(GL_MODELVIEW)

        # Rendering code with y-coordinates adjusted for the bottom-left origin
        background(0, 0, 1200, 700, BG1 if cek_background == 0 else BGSUNSET if cek_background == 1 else BGUMI if cek_background == 2 else None)
        background(50, -50 , 550 , 650 , INTROGIRL)
        background(800, 450, 1100, 550, EASYCLICK if pos_y >= 450 and pos_y <= 550 and pos_x >= 800 and pos_x <= 1100 else EASY)
        background(800, 300, 1100, 400, MEDIUMCLICK if pos_y >= 300 and pos_y <= 400 and pos_x >= 800 and pos_x <= 1100 else MEDIUM)
        background(800, 150, 1100, 250, HARDCLICK if pos_y >= 150 and pos_y <= 250 and pos_x >= 800 and pos_x <= 1100 else HARD)

        glFlush()
        glutSwapBuffers()

    elif menu == 2:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        cen = charModel.center()
            # projection is related to center of car , we need the center of the car to be the center of the screen
        glOrtho(cen[0] - 300, cen[0] + 300, cen[1] - 175, cen[1] + 175, -1, 1)
        # glOrtho(0, 1200, 0, 700, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.1, 0.1, 0.1, 0)
        # draw_grid()  # Jika Anda ingin menampilkan grid

        background(-1000,-675,2350,1375 , BGOUT)
        background(0,0,1200,700, BG2)
        draw_map()  # Gambar labirin
        draw_crustle()  # Gambar Pokeon crustle
        draw_pidgeot()  # Gambar Pokemon Pidgeot
        draw_pikachu()  # Gambar Pokemon Pikachu
        draw_finish()  # Gambar finish line
        background_kotak(cen[0]-290, cen[1] + 110, cen[0] - 85, cen[1] + 160, (0,0,0,0.5))
        charModel.draw()


        glPushMatrix()
        s = "Pokemon : " + str(charModel.pokemonCollect) + " / " + str((len(pikachu) + len(crustle) + len(pidgeot)))
        print_text(s,cen[0]-285,cen[1] + 140)
        glPopMatrix()

        glPushMatrix()
        second = start_time % 60
        minutes = start_time // 60 
        print_text("Minutes : " + str(minutes) + " Second : " + str(second),cen[0]-285,cen[1] + 120)
        if start_time < 0:
            menu = 3
            gameover = 1
            sounds[0].stop()
        
        if col.item_collisiom(finish) and charModel.pokemonCollect == (len(pikachu) + len(crustle) + len(pidgeot)) and gameover == 0:
            sounds[0].stop()
            menu = 3
            win = 1

        glPopMatrix()

        glPushMatrix()
        col.collosion_walls_horizontal()
        col.collosion_walls_vertical()
        col.item_collisiom(pikachu)
        col.item_collisiom(pidgeot)
        col.item_collisiom(crustle)
        glPopMatrix()

        glFlush()

    elif menu == 3:
        glClearColor(0.2, 0.2, 0.2, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1200, 0, 700, -1, 1)  # Adjusted for bottom-left origin
        glMatrixMode(GL_MODELVIEW)

        # Rendering code with y-coordinates adjusted for the bottom-left origin
        background(0, 0, 1200, 700, BG1 if cek_background == 0 else BGSUNSET if cek_background == 1 else BGUMI if cek_background == 2 else None)
        background(100, 350, 700, 550, FINISH if win == 1 else GAMEOVER)
        background(100, 200, 350, 300, PLAYCLICK if pos_y >= 200 and pos_y <= 300 and pos_x >= 100 and pos_x <= 350 else PLAY)
        background(450, 200, 700, 300, QUITCLICK if pos_y >= 200 and pos_y <= 300 and pos_x >= 450 and pos_x <= 700 else QUIT)
        background(800, -50 , 1200, 650, INTROBOY)

        print("Posisi X: ", pos_x)
        print("Posisi Y: ", pos_y)

        glFlush()
        glutSwapBuffers()
    
    elif menu == 4:
        glClearColor(0.2, 0.2, 0.2, 0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 1200, 0, 700, -1, 1)  # Adjusted for bottom-left origin
        glMatrixMode(GL_MODELVIEW)

        # Rendering code with y-coordinates adjusted for the bottom-left origin
        background(0, 0, 1200, 700, BG1 if cek_background == 0 else BGSUNSET if cek_background == 1 else BGUMI if cek_background == 2 else None)
        background(100, 50, 1100, 650, BOXBACKGROUND)
        background(150, 500, 650, 550, BACKGROUNDTITLE)
        background(150, 230, 430, 450, FARMERBUTTON)
        background(450, 230, 760, 450, SUNSETBUTTON)
        background(780, 230, 1050, 450, UMIBUTTON)
        background(780, 100, 1050, 200, BACKBUTTONCLICK if pos_y >= 100 and pos_y <= 200 and pos_x >= 700 and pos_x <= 1050 else BACKBUTTON)

        print("Posisi X: ", pos_x)
        print("Posisi Y: ", pos_y)

        glFlush()
        glutSwapBuffers()

def input_keyboard(key,x,y):
    global pos_x, pos_y, menu

    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        charModel.move_to_top()
        charModel.position = "top"   
        if charModel.steptop >= 16:
            charModel.steptop = 12
        charModel.steptop += 1
    elif key == GLUT_KEY_DOWN:
        charModel.move_to_bottom()
        charModel.position = "bottom"
        if charModel.stepbottom >= 4:
            charModel.stepbottom = 0
        charModel.stepbottom += 1
    elif key == GLUT_KEY_RIGHT:
        charModel.move_to_right()
        charModel.position = "right"
        if charModel.stepright >= 12:
            charModel.stepright = 8
        charModel.stepright += 1
    elif key == GLUT_KEY_LEFT:
        charModel.move_to_left()
        charModel.position = "left"
        if charModel.stepleft >= 8:
            charModel.stepleft = 4
        charModel.stepleft += 1

def print_text(s, x, y):
    """
    this function draw text on the screen
    """
    glLineWidth(4)
    glTranslate(x, y, 0)
    glScale(0.08, 0.08, 1)
    s = s.encode()
    for char in s:
        glutStrokeCharacter(GLUT_STROKE_MONO_ROMAN, char)

def update():
    global start_time
    start_time -= 1
    for i in pikachu:
        i.switch_texture()
    for i in crustle:
        i.switch_texture()
    for i in pidgeot:
        i.switch_texture()
    glutPostRedisplay()

def set_timer(p):
    global start_time
    glutTimerFunc(1000, set_timer, 0)
    update()

def Timer(v):
    display()
    glutTimerFunc(10, Timer, 1)

def trackingMouse(x, y):
    global pos_x , pos_y, menu, onbutton
    pos_x = x
    pos_y = 700 - y

    if pos_x >= 480 and pos_x <= 720 and pos_y >= 320 and pos_y <= 420 and menu == 0: # Button Home Play
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_x >= 480 and pos_x <= 720 and pos_y >= 200 and pos_y <= 300 and menu == 0: # Button Home Option
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_x >= 480 and pos_x <= 720 and pos_y >= 80 and pos_y <= 180 and menu == 0: # Button Home Quit
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_y >= 450 and pos_y <= 550 and pos_x >= 800 and pos_x <= 1100 and menu == 1:  # Button Select Level Easy
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_y >= 300 and pos_y <= 400 and pos_x >= 800 and pos_x <= 1100 and menu == 1: # Button Select Level Medium
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_y >= 150 and pos_y <= 250 and pos_x >= 800 and pos_x <= 1100 and menu == 1: # Button Select Level Hard
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_y >= 200 and pos_y <= 300 and pos_x >= 100 and pos_x <= 350 and menu == 3: # Button Game Over Play Again
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_y >= 200 and pos_y <= 300 and pos_x >= 450 and pos_x <= 700 and menu == 3: # Button Game Over Quit
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    elif pos_y >= 100 and pos_y <= 200 and pos_x >= 700 and pos_x <= 1050 and menu == 4:
        if onbutton == False:
            sounds[1].play(0)
            onbutton = True
    else :
        onbutton = False
           

def mouse(state,key, x , y):
    global menu, gameover, win, start_time, cek_background

    if y >= 320 and y <= 420 and x >= 480 and x <= 720 and key == GLUT_LEFT_BUTTON and menu == 0:
        menu = 1
    elif pos_y >= 200 and pos_y <= 300 and pos_x >= 480 and pos_x <= 720 and key == GLUT_LEFT_BUTTON and menu == 0:
        menu = 4
    elif pos_y >= 80 and pos_y <= 180 and pos_x >= 480 and pos_x <= 720 and key == GLUT_LEFT_BUTTON and menu == 0:
        os._exit(0)
    elif pos_y >= 450 and pos_y <= 550 and pos_x >= 800 and pos_x <= 1100 and key == GLUT_LEFT_BUTTON and menu == 1:
        start_time = 300
        sounds[0].play(-1)
        menu = 2
    elif pos_y >= 300 and pos_y <= 400 and pos_x >= 800 and pos_x <= 1100 and key == GLUT_LEFT_BUTTON and menu == 1:
        start_time = 180
        sounds[0].play(-1)
        menu = 2
    elif pos_y >= 150 and pos_y <= 250 and pos_x >= 800 and pos_x <= 1100 and menu == 1 and key == GLUT_LEFT_BUTTON and menu == 1:
        start_time = 120
        sounds[0].play(-1)
        menu = 2
    elif pos_y >= 200 and pos_y <= 300 and pos_x >= 100 and pos_x <= 350 and key == GLUT_LEFT_BUTTON and menu == 3:
        reset_maze()
        charModel.reset_position()
        menu = 1
    elif pos_y >= 200 and pos_y <= 300 and pos_x >= 450 and pos_x <= 700 and key == GLUT_LEFT_BUTTON and menu == 3:
        os._exit(0)
    elif pos_x >= 150 and pos_x <= 430 and pos_y >= 230 and pos_y <= 450 and key == GLUT_LEFT_BUTTON and menu == 4:
        cek_background = 0
    elif pos_x >= 450 and pos_x <= 760 and pos_y >= 230 and pos_y <= 450 and key == GLUT_LEFT_BUTTON and menu == 4:
        cek_background = 1
    elif pos_x >= 780 and pos_x <= 1050 and pos_y >= 230 and pos_y <= 450 and key == GLUT_LEFT_BUTTON and menu == 4:
        cek_background = 2
    elif pos_y >= 100 and pos_y <= 200 and pos_x >= 700 and pos_x <= 1050 and key == GLUT_LEFT_BUTTON and menu == 4:
        menu = 0



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
    set_timer(0)
    glutMainLoop()

if __name__ == "__main__":
    main()
