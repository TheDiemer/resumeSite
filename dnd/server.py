#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, Markup
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/backstory')
def back():
    return render_template('backstory.html')


@app.route('/setting')
def setting():
    return render_template('setting.html')


@app.route('/character')
def character():
    return render_template('character.html')


@app.route('/sessions')
def sessions():
    return render_template('sessions.html')


@app.route('/story')
def story():
    return render_template('story.html')


@app.route('/noodles')
def noodles():
    return render_template('noodles.html')


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/hidden')
def hidden():
    return render_template('hidden.html')


@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/party')
def party():
    return render_template('party.html')

@app.route('/prizes')
def rings():
    return render_template('prizes.html')


if __name__ == '__main__':
    app.run(debug=True)
