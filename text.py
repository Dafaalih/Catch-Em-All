import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Inisialisasi Pygame
pygame.init()

# Inisialisasi PyOpenGL
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutCreateWindow("Text in PyOpenGL")

# Fungsi untuk menggambar teks
def draw_text(text, position):
    font = pygame.font.Font(None, 36)  # Ganti dengan path font yang Anda inginkan
    text_surface = font.render(text, True, (255, 255, 255, 255), (0, 0, 0, 0))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glRasterPos2f(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Gambar teks
    glColor3f(1.0, 1.0, 1.0)
    draw_text("Hello, PyOpenGL!", (100, 100))

    glutSwapBuffers()
