from flask import Flask, jsonify

from popcopy import mano

app = Flask(__name__)

@app.route('/<search>/<kac>')
def hello_world(search, kac):

    return mano(search, kac)

if __name__ == '__main__':
    app.run(debug=True)