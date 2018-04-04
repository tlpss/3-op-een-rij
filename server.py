from game import Game
from flask import Flask, request, send_from_directory, jsonify,json
from time import sleep #delay before clearing board
app = Flask(__name__) 
app.config.from_object(__name__)

game=Game()

@app.route('/')
def index():
    return send_from_directory("templates", "index.html")

@app.route('/<string:name>')
def static_files(name):
    game.clear_board()
    return send_from_directory("templates", name) #sends CSS and JS files


@app.route('/next_move')
def next_move():
    args= request.args.items() #gets args form URL  
    game.put_x(args)
    ret=game.put_and_remove_o()
    ret= json.dumps(ret)
    return jsonify(ret=ret)


@app.route('/delete_x')
def delete_x():
    args=request.args.items()
    ret=game.remove_x(args)
    ret=json.dumps(ret)
    return jsonify(ret=ret)

@app.route('/clear_board')
def clear():
    #sleep(5)
    ret=game.clear_board()
    ret=json.dumps(ret)
    return jsonify(ret=ret)


if (__name__=='__main__'):
    app.run(debug=True) 
