from flask import Flask, render_template, url_for
from game import Game
app = Flask(__name__)

@app.route('/')
def hello_world():
    game = Game()
    game.getMoves()
    # print(game.__dict__, game.pawns.__dict__)
    # print(game.__dict__)
    return render_template('index.html.j2', game=game)
