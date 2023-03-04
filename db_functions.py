import sqlite3

def add_score(name, score):
    connect = sqlite3.connect('./static/data/leaderboards.db')
    cursor = connect.cursor()

    cursor.execute("INSERT INTO leaderboards('name', 'score) VALUES (?, ?)", (name, score))
    connect.commit()
    connect.close()

def get_leaderboards():
    leaderboards = []

    connect = sqlite3.connect('./static/data/leaderboards.db')
    cursor = connect.cursor()
    result = cursor.execute("SELECT rowid, * FROM leaderboards")

    for row in result: 
        player_score = {
            'player': row[0],
            'score': row[1],
        }

        leaderboards.append(player_score)

    connect.close()
    return leaderboards