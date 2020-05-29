#!/usr/bin/python3
import spellChoice, cantripChoice
from flask import Flask, render_template, request, url_for, Markup
app = Flask(__name__)


def tables(data):
    headers = ['Casting Time','Range','Components','Duration','Description']
    htmlTable = '<table width="100">\n'
    for place in range(0,5):
        htmlTable += '\n<tr><th>{0}</th><td>{1}</td></tr>\n'.format(headers[place], data[place])
    htmlTable += '</table>'
    return Markup(htmlTable)


@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/casting/')
#def casting():
#    return render_template('casting.html')

#@app.route('/casting/v2/')
#def secondEdition():
#    return render_template('castingv2.html')

@app.route('/casting/v3')
def thirdEdition():
    return render_template('castingv3.html')

#@app.route('/casting/cantrip/')
#def cantrip():
#    return render_template('cantrip.html')

#@app.route('/casting/cantrip/cast', methods=['POST'])
#def cantripCast():
#    rolled = request.form['rolled']
#    if rolled.isdigit():
#        if int(rolled) <= 100:
#            cast, details = cantripChoice.main(int(rolled), None)
#            details = tables(details)
#            return render_template('CAST.html', cast=cast, details=details)
#        else:
#            return render_template('cantripTake2.html')
#    else:
#        return render_template('cantripTake2.html')


#@app.route('/casting/v2/cantripO/')
#def cantripO():
#    return render_template('cantripO.html')

#@app.route('/casting/v2/cantripO/cast',methods=['POST'])
#def cantripOCast():
#    rolled = request.form['rolled']
#    if rolled.isdigit():
#        if int(rolled) <= 100:
#            cast, details = cantripChoice.main(int(rolled), 'O')
#            details = tables(details)
#            return render_template('CASTv2.html', cast=cast, details=details)
#        else:
#            return render_template('cantripOTake2.html')
#    else:
#        return render_template('cantripOTake2.html')

#@app.route('/casting/v2/cantripD/')
#def cantripD():
#    return render_template('cantripD.html')

#@app.route('/casting/v2/cantripD/cast',methods=['POST'])
#def cantripDCast():
#    rolled = request.form['rolled']
#    if rolled.isdigit():
#        if int(rolled) <= 100:
#            cast, details = cantripChoice.main(int(rolled), 'D')
#            details = tables(details)
#            return render_template('CASTv2.html', cast=cast, details=details)
#        else:
#            return render_template('cantripDTake2.html')
#    else:
#        return render_template('cantripDTake2.html')

#@app.route('/casting/spell/')
#def spell():
#    return render_template('spell.html')

#@app.route('/casting/v2/spellO/')
#def spellO():
#    return render_template('spellO.html')

#@app.route('/casting/v2/spellO/cast',methods=['POST'])
#def spellOCast():
#    rolled = request.form['rolled']
#    if rolled.isdigit():
#        if int(rolled) <= 100:
#            cast, details = spellChoice.main(int(rolled), 'O')
#            details = tables(details)
#            return render_template('CASTv2.html', cast=cast, details=details)
#        else:
#            return render_template('spellOTake2.html')
#    else:
#        return render_template('spellOTake2.html')

@app.route('/casting/v3/spellO/')
def spellO():
    return render_template('spellO.html')

@app.route('/casting/v3/spellO/cast',methods=['POST'])
def spellOCast():
    rolled = request.form['rolled']
    if rolled.isdigit():
        if int(rolled) <= 100:
            cast, details = spellChoice.main(int(rolled), 'O')
            details = tables(details)
            return render_template('CASTv2.html', cast=cast, details=details)
        else:
            return render_template('spellOTake2.html')
    else:
        return render_template('spellOTake2.html')

@app.route('/casting/v3/spellD/')
def spellD():
    return render_template('spellD.html')

@app.route('/casting/v3/spellD/cast',methods=['POST'])
def spellDCast():
    rolled = request.form['rolled']
    if rolled.isdigit():
        if int(rolled) <= 100:
            cast, details = spellChoice.main(int(rolled), 'D')
            details = tables(details)
            return render_template('CASTv2.html', cast=cast, details=details)
        else:
            return render_template('spellDTake2.html')
    else:
        return render_template('spellDTake2.html')

#@app.route('/casting/spell/cast', methods=['POST'])
#def spellCast():
#    rolled = request.form['rolled']
#    if rolled.isdigit():
#        if int(rolled) <= 100:
#            cast, details = spellChoice.main(int(rolled), None)
#            details = tables(details)
#            return render_template('CAST.html', cast=cast, details=details)
#        else:
#            return render_template('spellTake2.html')
#    else:
#        return render_template('spellTake2.html')


if __name__ == '__main__':
    app.run(debug=True)
  #app.run(host='tatl.ddnsfree.com',debug=True)
