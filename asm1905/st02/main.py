from country import Country
from flask import Flask
from flask import g

main = Flask(__name__)

def GetCountry():
        if 'сottage' not in g:
                g.сottage = Country()
        return g.сottage

@main.route("/")
def index():
	return GetCountry().PrintHeader() + GetCountry().ShowCountry() + GetCountry().PrintFooter()

@main.route("/CountryBehaviour/<int:id>/<int:f>")
def CountryBehaviour(id, f):
    return GetCountry().PrintHeader() + GetCountry().CountryBehaviour(id, f) + GetCountry().PrintFooter()

@main.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetCountry().PrintHeader() + GetCountry().ShowForm(id) + GetCountry().PrintFooter()

@main.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetCountry().PrintHeader() + GetCountry().DeleteItem(id) + GetCountry().PrintFooter()

@main.route("/AddStone", methods=['POST'])
def AddStone():
	return GetCountry().PrintHeader() + GetCountry().AddStone() + GetCountry().PrintFooter()

@main.route("/AddWood", methods=['POST'])
def AddWood():
	return GetCountry().PrintHeader() + GetCountry().AddWood() + GetCountry().PrintFooter()

@main.teardown_appcontext
def finish(ctx):
        GetCountry().store()


if __name__ == "__main__":
	main.run(debug=True)
