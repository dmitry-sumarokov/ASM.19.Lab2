if __name__ == '__main__':
    from group import Group
else:
    from .group import Group

from flask import Flask
from flask import g
app = Flask(__name__)

def GetGroup():
        if 'cur_group' not in g:
                g.cur_group = Group()
        return g.cur_group

@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().print_group() + GetGroup().PrintFooter()

@app.route("/ShowForm/<id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().change_worker(int(id)) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().remove_worker(id) + GetGroup().PrintFooter()

@app.route("/ShowMagicForm/<int:id>")
def ShowMagicForm(id):
	return GetGroup().PrintHeader() + GetGroup().do_magic(id) + GetGroup().PrintFooter()

@app.route("/DeleteGroup")
def DeleteGroup():
	return GetGroup().PrintHeader() + GetGroup().clear_worker() + GetGroup().PrintFooter()

@app.route("/AddItem", methods=['POST'])
def AddItem():
	return GetGroup().PrintHeader() + GetGroup().add_worker() + GetGroup().PrintFooter()


@app.teardown_appcontext
def finish(ctx):
        GetGroup().save_to_file()

       
if __name__ == "__main__":
	app.run(debug=True)
