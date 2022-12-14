from flask import Flask, render_template, request
from game import Game

@app.route("/game")
def index():
    return render_template(index.html)

@app.route("/information", methods=['POST'])
def information():
    global game

    game = Game()
    game.play_game()

    return render_template(information.html, score=game.score)

@app.route("/leaderboard")
def leaderboard():
    global game

    leaderboard = {}
    player_name = request.form['name']

    leaderboard.setdefault("player" + len(leaderboard), [player_name, game.score])

    return render_template(leaderboard.html, leaderboard=leaderboard)
