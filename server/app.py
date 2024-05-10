#!/usr/bin/env python3

from flask import Flask, make_response, jsonify

app = Flask(__name__)
app.json.compact = False

@app.get('/')
def index():
    return make_response( jsonify("Hello world") )

@app.get('/blog/<string:name>')
def show_blog(name:str):
    return make_response(jsonify(f"{name} has an amazing blog check it out"))


# write your routes here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)
