from flask import Flask, render_template, request
from game import Game
import sqlite3
from db_functions import add_score, get_leaderboards

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/play", methods=['POST'])
def play():
    global game

    game.play_game()
    score = game.score

    return render_template('information.html', score=score)

@app.route("/", methods=['POST'])
def enter_name():
    global score

    player_name = request.form['name']

    add_score(player_name, score)

    return('index.html')

@app.route("/leaderboards")
def leaderboards():
    leaderboards = get_leaderboards()

    return render_template('leaderboards.html', leaderboards=leaderboards)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5000")

