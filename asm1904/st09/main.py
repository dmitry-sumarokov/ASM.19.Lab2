from group import group
from group import Creative
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
		if 'group' not in g:
				g.group = group()
		return g.group

def GetCreative():
		if 'Creative' not in g:
				g.Creative = Creative()
		return g.Creative

@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().ShowGroup() + GetGroup().PrintFooter()

@app.route("/CreativeBehaviour/<int:id>/<int:f>")
def CreativeBehaviour(id, f):
	return GetGroup().PrintHeader() + GetGroup().CreativeBehaviour(id, f) + GetGroup().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().ShowForm(id) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().DeleteItem(id) + GetGroup().PrintFooter()

@app.route("/AddItemArtist", methods=['POST'])
def AddItemArtist():
	return GetGroup().PrintHeader() + GetGroup().AddItemArtist() + GetGroup().PrintFooter()

@app.route("/AddItemWriter", methods=['POST'])
def AddItemWriter():
	return GetGroup().PrintHeader() + GetGroup().AddItemWriter() + GetGroup().PrintFooter()

@app.route("/AddItemPoet", methods=['POST'])
def AddItemPoet():
	return GetGroup().PrintHeader() + GetGroup().AddItemPoet() + GetGroup().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
		GetGroup().store()


if __name__ == "__main__":
	app.run(debug=True)
