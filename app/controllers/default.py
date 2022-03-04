from email.policy import default
from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Hello World!"

@app.route("/test", defaults={'name': None, 'id': 0})
@app.route("/test/<name>", defaults={'id': 0})
@app.route("/test_int/<int:id>", defaults={'name': None}, methods=['GET'])
def teste(name, id):
    if name:
        return "Olá %s" % name
    if id:
        return "Id = %d" % id
    return "Olá Usuário"