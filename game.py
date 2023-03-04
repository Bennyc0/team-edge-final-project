from sense_hat import SenseHat
from time import sleep
from obstacle import Obstacle
from player import Player
import random

class Game():
    def __init__(self):
        self.sense = SenseHat()
        
        self.score = 0
        self.player_alive = True

        self.tx_spd = 0.045
        self.tx_color = (255,150,100)

        self.bg_color = (100,150,150)

        self.player = Player(self.sense, self.bg_color)
        self.obstacles = []

        self.sense.low_light = True
    
    def play_game(self):
        turn = 0

        self.start_up()
        sleep(0.25)
        self.background()
        self.player.display(0)
        sleep(1.5)

        while self.player_alive:
            self.player.flap("down")
            self.delete_pipe()

            for event in self.sense.stick.get_events():
                if event.action == "pressed" and event.direction == "up":
                    self.player.flap(event.direction)

            for obstacle in self.obstacles:
                obstacle.movement()
                self.player.display(0)
          
            self.collision()
            
            if turn%4 == 0:
                self.generate()

            turn += 1
            sleep(0.5)

        self.sense.show_message("You Crashed!", scroll_speed=self.tx_spd, text_colour=self.tx_color)
        self.sense.show_message(f"Final Score: {self.score}", scroll_speed=self.tx_spd, text_colour=self.tx_color)

    def start_up(self):
        self.sense.show_message("Flappy Bird", scroll_speed=self.tx_spd, text_colour=self.tx_color)
        
        for x in range(5, 0, -1):
            self.sense.show_message(str(x), scroll_speed=self.tx_spd, text_colour=self.tx_color)
        self.sense.show_message("FLAP!", scroll_speed=self.tx_spd, text_colour=self.tx_color)
    
    def generate(self):
        conf = [
            [0,1,2,3,4],
            [0,1,2,3,7],
            [0,1,2,6,7],
            [0,1,5,6,7],
            [0,4,5,6,7],
            [3,4,5,6,7]]
        
        pipe = Obstacle(self.sense, random.choice(conf))
        self.obstacles.append(pipe)

    def delete_pipe(self):
        if len(self.obstacles) > 0 and self.obstacles[0].x_pos == 0:
            self.obstacles.remove(self.obstacles[0])
        for num in range(8):
            self.sense.set_pixel(0, num, self.bg_color)
            self.sense.set_pixel(1, num, self.bg_color)

    def collision(self):
        for pipe in self.obstacles:
            if self.player.x_pos == pipe.x_pos:
                if self.player.y_pos in pipe.y_pos:
                    self.player_alive = False
                else:
                    self.score += 1

        if self.player.y_pos == 7:
            self.player_alive = False
    
    def background(self):
        lb = self.bg_color
        background = [
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb,
            lb,lb,lb,lb,lb,lb,lb,lb]
        
        self.sense.set_pixels(background)