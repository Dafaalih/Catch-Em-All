class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_collision(self, x_k, y_k):
        return (
            x_k + 10 >= self.x and x_k - 10 <= self.x + self.width and
            y_k + 20 >= self.y and y_k - 15 <= self.y + self.height
        )

class Environment:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, x, y, width, height):
        obstacle = Obstacle(x, y, width, height)
        self.obstacles.append(obstacle)

    def handle_collision(self, x_k, y_k):
        for obstacle in self.obstacles:
            if obstacle.is_collision(x_k, y_k):
                # Implementasi aksi yang sesuai saat collision terjadi
                if x_k < obstacle.x:
                    x_k -= 15
                elif x_k > obstacle.x:
                    x_k += 15

                if y_k > obstacle.y:
                    y_k += 15
                elif y_k < obstacle.y:
                    y_k -= 15

# Inisialisasi lingkungan permainan
environment = Environment()

# Menambahkan rintangan-rintangan ke lingkungan permainan
environment.add_obstacle(0, 275, 70, 20)
environment.add_obstacle(70, 175, 10, 100)
environment.add_obstacle(70, 75, 10, 100)
environment.add_obstacle(170, 0, 10, 275)
environment.add_obstacle(170, 175, 100, 20)
environment.add_obstacle(270, 75, 400, 20)
environment.add_obstacle(370, 75, 10, 300)
environment.add_obstacle(270, 275, 300, 20)

# Contoh penggunaan:
x_k = 100  # Koordinat x karakter
y_k = 100  # Koordinat y karakter

# Memeriksa collision dan menangani aksi yang sesuai
environment.handle_collision(x_k, y_k)
