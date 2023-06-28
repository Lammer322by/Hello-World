import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )

@app.route('/home/cirno')
def show_cirno():
    return flask.render_template(
        'cirno.html'
    )

@app.route('/home/cirno/cheese_crepes')
def show_crepes():
    return flask.render_template(
        'cheese_crepes.html'
    )

@app.route('/home/cirno_game', methods = ['GET', 'POST'])
def hello_name():
    if request.method == 'GET':
        word_in=request.args.get("word")
    elif request.method == 'POST':
        word_in=request.form.get("word")

    if word_in is None:
        word_in="Соус"
    
    if word_in[-1] == 'с':
        reaction = " - Сырно!!"
    else:
        reaction = "Неет! Это слово не подходит!! Скажи что-нибудь заканчивающееся на букву 'с' >_<"

    return flask.render_template(
        'cirno_game.html',
        word=word_in,
        reaction=reaction
    )


if __name__ == '__main__':
   app.run(debug = True)
