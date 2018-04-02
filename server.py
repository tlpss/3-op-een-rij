
import game
from flask import Flask, request, send_from_directory, jsonify,json

app = Flask(__name__) 
app.config.from_object(__name__)

@app.route('/')
def index():
    return send_from_directory("templates", "index.html")

@app.route('/<string:name>')
def static_files(name):
    return send_from_directory("templates", name) #sends CSS and JS files


@app.route('/next_move')
def next_move():
    args= request.args.items() #gets args form URL  
    print(str(args))
    ret={"board":[1,0,2,0,2,1,0,2,0]}
    ret=json.dumps(ret)
    return jsonify(ret=ret)


@app.route('/delete_x')
def delete_x():
    args=request.args.items()
    print(str(args))
    ret=1
    ret={"board":[1,0,2,0,2,1,0,0,0],"valid":ret}
    ret=json.dumps(ret)
    return jsonify(ret=ret)


if (__name__=='__main__'):
    app.run(debug=True) 
