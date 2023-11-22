from flask import Flask, render_template, request
from flask_pymongo import PyMongo


app = Flask(__name__, static_folder='assets')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/audio1')
def audio1():
    return render_template("audio1.html")

@app.route('/audio2')
def audio2():
    return render_template("audio2.html")

@app.route('/audio3')
def audio3():
    return render_template("audio3.html")

@app.route('/podcast1')
def podcast1():
    return render_template("podcast1.html")

@app.route('/podcast2')
def podcast2():
    return render_template("podcast2.html")

@app.route('/podcast3')
def podcast3():
    return render_template("podcast3.html")

@app.route('/music1')
def music1():
    return render_template("music1.html")

@app.route('/music2')
def music2():
    return render_template("music2.html")

@app.route('/music3')
def music3():
    return render_template("music3.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)