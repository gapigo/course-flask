# from email.policy import default
from distutils.log import Log

from flask_login import login_user, logout_user
from app import app, login_manager, db
from flask import flash, redirect, render_template, url_for

from app.models.tables import User
from app.models.forms import LoginForm

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            if user:
                flash("Password and username don't match")
            else:
                flash("User doesn't exist")
    else:
        flash("Invalid login.")
    return render_template('login_form.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


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