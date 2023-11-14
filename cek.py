from OpenGL.GL import *
from OpenGL.GLUT import *

# Fungsi untuk menggambar polygon
def draw_polygon(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

# Fungsi untuk mendeteksi collision antara dua polygon
def is_collision(polygon1, polygon2):
    for point in polygon1:
        if point_in_polygon(point, polygon2):
            return True
    for point in polygon2:
        if point_in_polygon(point, polygon1):
            return True
    return False

# Fungsi untuk mendeteksi apakah suatu titik berada di dalam suatu polygon
def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

# Inisialisasi PyOpenGL
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutCreateWindow("Collision Detection")

# Polygon pertama
polygon1 = [(0, 0), (2, 0), (2, 2), (0, 2)]

# Polygon kedua
polygon2 = [(1, 1), (3, 1), (3, 3), (1, 3)]

while True:
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    draw_polygon(polygon1)

    glColor3f(0.0, 0.0, 1.0)
    draw_polygon(polygon2)

    if is_collision(polygon1, polygon2):
        print("Collision detected!")

    glutSwapBuffers()
