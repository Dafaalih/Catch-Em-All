from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

# Definisi garis batasan
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_vertices(self):
        return [[self.x1, self.y1], [self.x2, self.y2]]

# Definisi garis batasan
maze1 = [
    Line(0, 100, 300, 100),
    Line(150, 200, 150, 600),
    # Tambahkan garis lain di sini sesuai dengan kebutuhan
]

# Karakter yang bergerak dalam labirin
class Character:
    def __init__(self, x, y, width, height, maze):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.maze = maze
        self.collision = False

    def update(self):
        if not self.collision:
            self.move()

    def move(self):
        if keystates[GLUT_KEY_UP]:
            self.y += self.speed
        if keystates[GLUT_KEY_DOWN]:
            self.y -= self.speed
        if keystates[GLUT_KEY_LEFT]:
            self.x -= self.speed
        if keystates[GLUT_KEY_RIGHT]:
            self.x += self.speed

        for line in self.maze:
            if self.check_collision_with_line(line):
                self.collision = True
    

    def check_collision_with_line(self, line):
        character_vertices = self.get_vertices()
        line_vertices = line.get_vertices()

        for axis in self.get_axes(character_vertices):
            min1, max1 = self.project(character_vertices, axis)
            min2, max2 = self.project(line_vertices, axis)

            if not (max1 >= min2 and max2 >= min1):
                return True

        return False

    def get_axes(self, vertices):
        axes = []
        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]
            edge = (x2 - x1, y2 - y1)
            axes.append((edge[1], -edge[0]))
        return axes

    def project(self, vertices, axis):
        min_val = max_val = vertices[0][0] * axis[0] + vertices[0][1] * axis[1]

        for vertex in vertices[1:]:
            p = vertex[0] * axis[0] + vertex[1] * axis[1]
            if p < min_val:
                min_val = p
            elif p > max_val:
                max_val = p

        return min_val, max_val

    def get_vertices(self):
        vertices = [
            [self.x, self.y],
            [self.x + self.width, self.y],
            [self.x + self.width, self.y + self.height],
            [self.x, self.y + self.height]
        ]
        return vertices
    
character = Character(50, 50, 30, 30, maze1)

def input_keyboard(key,x,y):
        global pos_x, pos_y

        # Untuk mengubah posisi kotak
        if key == GLUT_KEY_UP:
            character.y += 5
        elif key == GLUT_KEY_DOWN:
            character.y -= 5
        elif key == GLUT_KEY_RIGHT:
            character.x += 5
        elif key == GLUT_KEY_LEFT:
            character.left -= 5

        for line in character.maze:
            if character.check_collision_with_line(line):
                character.collision = True

# Fungsi untuk menggambar karakter
def draw_character(character):
    glColor3f(0, 1, 0)
    glRectf(character.x, character.y, character.x + character.width, character.y + character.height)

# Fungsi untuk menggambar garis batasan
def draw_lines(lines):
    glColor3f(1, 0, 0)
    for line in lines:
        glBegin(GL_LINES)
        glVertex2f(line.x1, line.y1)
        glVertex2f(line.x2, line.y2)
        glEnd()

# Fungsi display
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_character(character)

    draw_lines(maze1)

    glutSwapBuffers()

    character.update()
    glutPostRedisplay()

# Fungsi keyboard input
keystates = {GLUT_KEY_UP: False, GLUT_KEY_DOWN: False, GLUT_KEY_LEFT: False, GLUT_KEY_RIGHT: False}

def special_keys(key, x, y):
    keystates[key] = True

def special_keys_up(key, x, y):
    keystates[key] = False

# Inisialisasi karakter


# Inisialisasi OpenGL
def init():
    glClearColor(0.2, 0.2, 0.2, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1200, 0, 700, -1, 1)
    glMatrixMode(GL_MODELVIEW)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(1200, 700)
    glutCreateWindow("Collision Example")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutSpecialFunc(input_keyboard)
    glutSpecialUpFunc(special_keys_up)
    glutMainLoop()
