class Obstacle():
    def __init__(self, sense, y_pos):
        self.sense = sense

        self.x_pos = 7
        self.y_pos = y_pos

    def movement(self):
        self.x_pos -= 1
        self.display()

    def display(self):
        for y in self.y_pos:
            if 0 < self.x_pos < 7:
                self.sense.set_pixel(self.x_pos+1, y, (100,150,150))
            self.sense.set_pixel(self.x_pos, y, (0,255,0))
