from sense_hat import SenseHat
from time import sleep
from obstacle import Obstacle
from player import Player
import random

class Game():
    def __init__(self, sense):
        self.sense = sense
        
        self.score = 0
        self.player_alive = True

        self.player = Player(sense)
        self.obstacles = []
    
    def play_game(self):
        turn = 0

        self.start_up()
        self.player.display(0)

        while self.player_alive:
            self.player.flap("down")
            self.delete_pipe()

            # if len(self.obstacles) > 0:
            for obstacle in self.obstacles:
                #     # if obstacle.y_pos > 0:
                obstacle.movement()

            for event in self.sense.stick.get_events():
                if event.action == "pressed" and event.direction == "up":
                    self.player.flap(event.direction)
                # else:
                #     self.player.flap("")
            
            if turn%4 == 0:
                self.generate()

            self.collision()
            turn += 1
            sleep(1)

        self.sense.show_message("You Crashed! Game Over!", scroll_speed=0.05, text_colour=(255,0,0))
        self.sense.show_message(f"Final Score: {self.score}", scroll_speed=0.05, text_colour=(255,0,0))

    def start_up(self):
        self.sense.show_message("Flappy Bird", scroll_speed=0.05, text_colour=(255,0,0))
        self.background()

    def generate(self):
        conf = [
            [0,1,2,3,4],
            [0,1,2,3,7],
            [0,1,2,6,7],
            [0,1,5,6,7],
            [0,4,5,6,7],
            [3,4,5,6,7]]
        
        pipe = Obstacle(sense, random.choice(conf))
        self.obstacles.append(pipe)

    def delete_pipe(self):
        if len(self.obstacles) > 0 and self.obstacles[0].x_pos == 0:
            self.obstacles.remove(self.obstacles[0])
        for num in range(8):
            self.sense.set_pixel(0, num, (100,150,150))
            self.sense.set_pixel(1, num, (100,150,150))

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
        lb = (100,150,150)
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

# --------------- Game --------------- #
sense = SenseHat()
game = Game(sense)

game.play_game()