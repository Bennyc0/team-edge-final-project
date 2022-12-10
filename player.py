class Player():
    def __init__(self, sense):
        self.sense = sense

        self.x_pos = 2
        self.y_pos = 4
    
    def flap(self, direction):
        if direction == "up" and self.y_pos > 0:
            self.y_pos -= 1
            self.display(-1)

        elif direction == "down" and self.y_pos < 7 :
            self.y_pos += 1
            self.display(1)
    
    def display(self, change):
        self.sense.set_pixel(self.x_pos, self.y_pos-change, (100,155,155))
        self.sense.set_pixel(self.x_pos, self.y_pos, (255,0,0))
