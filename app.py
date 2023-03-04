from flask import Flask, render_template, request
from game import Game
import sqlite3
from db_functions import add_score, get_leaderboards

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route("/information", methods=['GET','POST'])
def information():
    global score
=======
@app.route("/play", methods=['POST'])
def play():
    global game
>>>>>>> refs/remotes/origin/main

    game.play_game()
<<<<<<< HEAD
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
=======
    return render_template('score.html', score=game.score)

@app.route("/about")
def about():
    return render_template('about.html')
>>>>>>> refs/remotes/origin/main

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="7000")

