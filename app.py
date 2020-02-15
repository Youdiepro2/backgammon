from flask import Flask, render_template, request, redirect, url_for
from game import Game
MOVE_CMD = 'move'

app = Flask(__name__)
game = Game()

@app.route('/')
def hello_world():
    game.getMoves()
    # print(game.__dict__, game.pawns.__dict__)
    # print(game.__dict__)
    return render_template('index.html.j2', game=game)

@app.route("/ajax", methods = ['POST'])
def ajax():
	req = request.get_json()
	cmd = req.get('cmd')
	if cmd == MOVE_CMD:
		move = Move.fromRequest(req)
		if move == None:
			return game.toJSON()
        #
		# game.move(move)
		# if not game.violations.isEmpty() or game.winner != None:
		# 	return game.toJSON()
        #
		# if game.bootIsActive == True:
		# 	botMove = Bot(game).createMove()
		# 	game.move(botMove)

	return game.toJSON()
