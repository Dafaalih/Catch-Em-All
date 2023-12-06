from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def background(left, bottom, right, top, image):
        glBindTexture(GL_TEXTURE_2D, image)
        glBegin(GL_POLYGON)
        glTexCoord2f(0, 0)
        glVertex2f(left, bottom)
        glTexCoord2f(1, 0)
        glVertex2f(right, bottom)
        glTexCoord2f(1, 1)
        glVertex2f(right, top)
        glTexCoord2f(0, 1)
        glVertex2f(left, top)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, -1)

def background_kotak(left, bottom, right, top, color):
    glBegin(GL_POLYGON)
    glColor4f(*color)
    glTexCoord(0, 0)
    glVertex(left, bottom, 0)
    glTexCoord(1, 0)
    glVertex(right, bottom, 0)
    glTexCoord(1, 1)
    glVertex(right, top, 0)
    glTexCoord(0, 1)
    glVertex(left, top, 0)
    glEnd()
