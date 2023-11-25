import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import time

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width, height = 800, 600

# Set display mode
# pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Inisialisasi OpenGL
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(b"Waktu Hitung Mundur")

# Fungsi untuk menggambar teks pada layar
def draw_text(text, x, y):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))

# Fungsi untuk menggambar waktu hitung mundur
def draw_countdown(time_left):
    glColor3f(1, 1, 1)
    draw_text("Waktu Hitung Mundur", 250, 500)
    draw_text(str(time_left), 400, 400)

# Fungsi utama untuk merender layar
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_countdown(time_left)
    glutSwapBuffers()

# Fungsi yang dipanggil setiap frame
def update():
    global time_left
    time_left -= 1
    glutPostRedisplay()
    if time_left <= 0:
        print('WAKTU HABIS')

# Set waktu awal dan interval waktu hitung mundur
start_time = 5
time_interval = 1000  # dalam milidetik

# Inisialisasi waktu hitung mundur
time_left = start_time

# Fungsi untuk mengatur waktu
def set_timer(p):
    global time_left
    glutTimerFunc(time_interval, set_timer, 0)
    update()

# Inisialisasi timer
set_timer(0)

# Set properti layar
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, width, 0, height, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Set warna background
glClearColor(0, 0, 0, 1)

# Set fungsi untuk merender layar
glutDisplayFunc(draw)

# Mulai loop Pygame
glutMainLoop()
