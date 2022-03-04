# from email.policy import default
from distutils.log import Log
from app import app
from flask import render_template

from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login_form.html', form=form)



@app.route("/test", defaults={'name': None, 'id': 0})
@app.route("/test/<name>", defaults={'id': 0})
@app.route("/test_int/<int:id>", defaults={'name': None}, methods=['GET'])
def teste(name, id):
    if name:
        return "Olá %s" % name
    if id:
        return "Id = %d" % id
    return "Olá Usuário"