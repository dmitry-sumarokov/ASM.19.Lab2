from group import group
from human import Human
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
    if 'group' not in g:
        g.group = group()
    return g.group


def GetHuman():
    if 'Human' not in g:
        g.Human = Human()
    return g.Human


@app.route("/")
def index():
    return GetGroup().PrintHeader() + GetGroup().ShowGroup() + GetGroup().PrintFooter()


@app.route("/HumanBehaviour/<int:id>/<int:f>")
def HumanBehaviour(id, f):
    return GetGroup().PrintHeader() + GetGroup().HumanBehaviour(id, f) + GetGroup().PrintFooter()


@app.route("/ShowForm/<int:id>")
def ShowForm(id):
    return GetGroup().PrintHeader() + GetGroup().ShowForm(id) + GetGroup().PrintFooter()


@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
    return GetGroup().PrintHeader() + GetGroup().DeleteItem(id) + GetGroup().PrintFooter()


@app.route("/AddItemEngineer", methods=['POST'])
def AddItemEngineer():
    return GetGroup().PrintHeader() + GetGroup().AddItemEngineer() + GetGroup().PrintFooter()


@app.route("/AddItemSpecialist", methods=['POST'])
def AddItemSpecialist():
    return GetGroup().PrintHeader() + GetGroup().AddItemSpecialist() + GetGroup().PrintFooter()


@app.route("/AddItemDepartment", methods=['POST'])
def AddItemDepartment():
    return GetGroup().PrintHeader() + GetGroup().AddItemDepartment() + GetGroup().PrintFooter()


@app.teardown_appcontext
def finish(ctx):
    GetGroup().store()


if __name__ == "__main__":
    app.run(debug=True)