class Player():
    def __init__(self, sense, bg_color):
        self.sense = sense
        self.bg_color = bg_color

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
        self.sense.set_pixel(self.x_pos, self.y_pos-change, self.bg_color)
        self.sense.set_pixel(self.x_pos, self.y_pos, (255,0,0))
