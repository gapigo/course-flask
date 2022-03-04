# from email.policy import default
from distutils.log import Log
from app import app
from flask import render_template

from app import db
from app.models.tables import User
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



@app.route('/teste/<info>')
@app.route('/teste', defaults={"info": None})
def testing_crud(info):
    
    # CRUD CREATE READ UPDATE DELETE
    
    # CREATE
    # i = User("gapigo2", "newgen123", "Gabriel Pinheiro", "gabriel2@example.com")
    # db.session.add(i)
    # db.session.commit()
    
    # READ
    # r = User.query.filter_by(username="gapigo").all()
    # r2 = User.query.filter(User.email.endswith("@example.com")).all()
    # r3 = User.query.filter_by(username="gapigo").first()
    # print(r, r2, r3)
    
    # UPDATE
    # r = User.query.filter_by(username="gapigo").first()
    # r.name = "Gabriel P."
    # db.session.add(r)
    # db.session.commit()
    
    # DELETE
    # r = User.query.filter_by(username="gapigo").first()
    # db.session.delete(r)
    # db.session.commit()
    
    return "OK"




@app.route("/test", defaults={'name': None, 'id': 0})
@app.route("/test/<name>", defaults={'id': 0})
@app.route("/test_int/<int:id>", defaults={'name': None}, methods=['GET'])
def teste(name, id):
    if name:
        return "Olá %s" % name
    if id:
        return "Id = %d" % id
    return "Olá Usuário"