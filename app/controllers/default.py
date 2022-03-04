# from email.policy import default
from app import app
from flask import render_template

@app.route("/index/<user>")
@app.route("/", defaults={'user': None})
def index(user):
    return render_template('index.html', user=user)

@app.route("/test", defaults={'name': None, 'id': 0})
@app.route("/test/<name>", defaults={'id': 0})
@app.route("/test_int/<int:id>", defaults={'name': None}, methods=['GET'])
def teste(name, id):
    if name:
        return "Olá %s" % name
    if id:
        return "Id = %d" % id
    return "Olá Usuário"