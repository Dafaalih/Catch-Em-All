class collision:
    def __init__(self, char, object_maze):
        self.char = char
        self.object = object_maze
    
    def collosion_walls_horizontal(self):
        for i in self.object:
            if self.char.top == i[0][1] and ((self.char.left >= i[0][0] and self.char.left <= i[1][0]) or (self.char.right >= i[0][0] and self.char.right <= i[1][0])) :
                self.char.move_to_bottom()
            elif self.char.bottom == i[0][1] and ((self.char.left >= i[0][0] and self.char.left <= i[1][0]) or (self.char.right >= i[0][0] and self.char.right <= i[1][0])) :
                self.char.move_to_top()
            elif self.char.top >= 700:
                self.char.move_to_bottom()
            elif self.char.left == i[1][0] and (self.char.bottom <= i[1][1] and self.char.top >=  i[1][1]):
                self.char.move_to_right()
            elif self.char.right == i[0][0] and (self.char.bottom <= i[1][1] and self.char.top >=  i[1][1]):
                self.char.move_to_left()

    
    def collosion_walls_vertical(self):
        for i in self.object:
            if self.char.right == i[0][0] and ((self.char.bottom <= i[1][1] and self.char.bottom >= i[0][1]) or (self.char.top >= i[0][1] and self.char.top <= i[1][1])):
                self.char.move_to_left()
            elif self.char.left == i[0][0] and ((self.char.bottom <= i[1][1] and self.char.bottom >= i[0][1]) or (self.char.top >= i[0][1] and self.char.top <= i[1][1])) :
                self.char.move_to_right()
            elif self.char.left <= 0:
                self.char.move_to_right()
            elif self.char.top == i[0][1] and (self.char.left <= i[0][0] and self.char.right >=  i[0][0]):
                self.char.move_to_bottom()
            elif self.char.bottom == i[1][1] and (self.char.left <= i[1][0] and self.char.right >=  i[1][0]):
                self.char.move_to_top()
            # elif self.char.bottom == i[1][1]:
            #     self.char.move_to_top()

    def item_collisiom(self, box):
        for i in box:
            data = i.get_vertices()
            if ((self.char.right >= data[0][0] and self.char.right <= data[2][0]) or (self.char.left >= data[0][0] and self.char.left <= data[2][0])) and ((self.char.bottom <= data[0][1] and self.char.bottom >=  data[2][1]) or (self.char.top <= data[0][1] and self.char.top >=  data[2][1])):
                if i.type == 3:
                    return True
                else:
                    if i.collected == False:
                        self.char.pokemonCollect += 1
                    i.collected = True
            elif ((self.char.top <= data[0][1] and self.char.top >= data[1][1]) or (self.char.bottom <= data[0][1] and self.char.bottom >= data[1][1])) and (data[0][0] >= self.char.left and data[2][0] <= self.char.right):
                if i.type == 3:
                    return True
                else:
                    if i.collected == False:
                        self.char.pokemonCollect += 1
                    i.collected = True