from flask import Flask, render_template, request, redirect, url_for
from game import Game, Move
import pickle
MOVE_CMD = 'move'

app = Flask(__name__)
fileName = 'simple1.pkl';
# game = Game()
with open(fileName, mode='rb') as file:
    fileContent = file.read()
game = pickle.loads(fileContent)

@app.route('/')
def hello_world():
    # game.createInInitialState()
    # print(game.moves.moves)

    return render_template('index.html.j2', game=game)

@app.route("/ajax", methods = ['POST'])
def ajax():
    req = request.get_json()
    move = Move.fromRequest(req)
    if move:
        # createFixture(game)
        game.move(move)
    return game.toJSON()

    # if cmd == MOVE_CMD:
    #     move = Move.fromRequest(req)
    #     print(move)
	# 	if move == None:
	# 		return game.toJSON()
		# game.move(move)
		# if not game.violations.isEmpty() or game.winner != None:
		# 	return game.toJSON()
        #
		# if game.bootIsActive == True:
		# 	botMove = Bot(game).createMove()
		# 	game.move(botMove)
def createFixture(game):
    pickle.dump(game, open(fileName, 'wb'))
