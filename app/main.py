#!/usr/bin/python3
from flask import Flask, render_template, request, url_for, Markup
app = Flask(__name__, template_folder='/var/www/ericdiemerjones/templates/')
import sys, os
#sys.path.insert(0, '/var/www/ericdiemerjones/')

#template_dir = 

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')


@app.route('/about/')
def about():
    return render_template('about.html')


#@app.route('/sounds/')
#def test():
#    print(os.getcwd())
#    os.chdir('/var/www/soundBoard/app/')
#    print(os.getcwd())
#    return board.soundBoard()

if __name__ == '__main__':
    app.run(debug=True)
