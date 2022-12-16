from flask import Flask, render_template, request
from game import Game

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/play", methods=['POST'])
def play():
    global game

    game.play_game()
    return render_template('score.html', score=game.score)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="7000")