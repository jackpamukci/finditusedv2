from flask import Flask, jsonify
from grabba import search_me


app = Flask(__name__)


@app.route('/<name>/<num>')
def get_data(name, num):

    data = search_me(name, num)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)