#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, Markup
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/backstory/')
def back():
    return render_template('backstory.html')


@app.route('/setting/')
def back():
    return render_template('setting.html')


@app.route('/character/')
def back():
    return render_template('character.html')


@app.route('/zero/')
def back():
    return render_template('zero.html')


if __name__ == '__main__':
    app.run(debug=True)
  #app.run(host='tatl.ddnsfree.com',debug=True)
