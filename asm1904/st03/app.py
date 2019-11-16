from book import Library
from flask import Flask
from flask import g

app = Flask(__name__)

def GetBook():
        if 'book' not in g:
                g.book = Library()
        return g.book

@app.route("/")
def index():
	return GetBook().PrintHeader() + GetBook().ShowBook() + GetBook().PrintFooter()

@app.route("/Behaviour/<int:id>/<int:f>")
def Behaviour(id, f): 
    return GetBook().PrintHeader() + GetBook().Behaviour(id, f) + GetBook().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetBook().PrintHeader() + GetBook().ShowForm(id) + GetBook().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetBook().PrintHeader() + GetBook().DeleteItem(id) + GetBook().PrintFooter()

@app.route("/AddItem", methods=['POST'])
def AddItem():
	return GetBook().PrintHeader() + GetBook().AddItem() + GetBook().PrintFooter()

@app.route("/AddItemJournal", methods=['POST'])
def AddItemJournal():
	return GetBook().PrintHeader() + GetBook().AddItemJournal() + GetBook().PrintFooter()

@app.route("/AddItemNewspaper", methods=['POST'])
def AddItemNewspaper():
	return GetBook().PrintHeader() + GetBook().AddItemNewspaper() + GetBook().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        GetBook().store()

       
if __name__ == "__main__":
	app.run(debug=True)
