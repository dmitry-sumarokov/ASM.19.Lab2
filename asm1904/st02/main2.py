if __name__ == '__main__':
    from group2 import Group
else:
    from .group2 import Group

from flask import Flask
from flask import g
app = Flask(__name__)
ctx=app.app_context()
ctx.g.cur_group = Group()
ctx.push()

def GetGroup():
        # if 'cur_group' not in g:
                # g.cur_group = Group()
        # return g.cur_group
    return ctx.g.cur_group
@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().print_group() + GetGroup().PrintFooter()

@app.route("/ShowForm/<id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().change_Tancor2(int(id)) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().remove_Tancor2(id) + GetGroup().PrintFooter()

@app.route("/ShowMagicForm/<int:id>")
def ShowMagicForm(id):
	return GetGroup().PrintHeader() + GetGroup().do_magic(id) + GetGroup().PrintFooter()

@app.route("/DeleteGroup")
def DeleteGroup():
	return GetGroup().PrintHeader() + GetGroup().clear_Tancor2() + GetGroup().PrintFooter()

@app.route("/AddItem", methods=['POST'])
def AddItem():
	return GetGroup().PrintHeader() + GetGroup().add_Tancor2() + GetGroup().PrintFooter()

	
@app.route("/load")
def load():
    return GetGroup().PrintHeader() +GetGroup().load_from_file()+ GetGroup().PrintFooter()
	
@app.route("/save")
def save():
    return GetGroup().PrintHeader() +GetGroup().save_to_file()+ GetGroup().PrintFooter()


# @app.teardown_appcontext
# def finish(ctx):
        # # GetGroup().save_to_file()
		# with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'temp.p'), 'wb') as f:
            # pickle.dump(self._Tancors2, f)
        # return self.print_group()

       
if __name__ == "__main__":
	app.run(debug=True)
