from flask import Flask, render_template, request
from game import Game

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/information", methods=['POST'])
def information():
    global game

    game.play_game()

    return render_template('information.html', score=game.score)

@app.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    global game

    leaderboard = {}
    player_name = ""

    try:
        player_name = request.form['playername']
    except:
        return render_template('leaderboard.html', score_list=leaderboard)

    if player_name != "":
        leaderboard.setdefault("player" + str(len(leaderboard)+1), [player_name, game.score])

    return render_template('leaderboard.html', score_list=leaderboard)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="7000")