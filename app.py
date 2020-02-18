from flask import Flask, render_template, request, redirect, url_for
from game import Game, Move
import pickle
MOVE_CMD = 'move'

app = Flask(__name__)
fileName = 'simple1.pkl';

game = Game()

@app.route('/')
def hello_world():
    # if not fileName:
    game.createInInitialState()

    return render_template('index.html.j2', game=game)

@app.route("/reset", methods = ['GET'])
def reset():
    game.createInInitialState()
    return render_template('index.html.j2', game=game)


@app.route("/ajax", methods = ['POST'])
def ajax():
    req = request.get_json()
    move = Move.fromRequest(req)
    if move:
        game.move(move)
    return game.toJSON()

if __name__ == "__main__":
	app.run( port=5008, debug=True)
