from company import Company
from flask import Flask
from flask import render_template
from flask import g

app = Flask(__name__)

"""def GetStaff():
        if 'staff' not in g:
                g.staff = Company()
        return g.staff"""

GetStaff = Company()

@app.route("/")
def index():
	return GetStaff.PrintHeader() + GetStaff.ShowStaff()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetStaff.PrintHeader() + GetStaff.DeleteItem(id)

@app.route("/DeleteStaff")
def DeleteStaff():
	return GetStaff.PrintHeader() + GetStaff.DeleteStaff()

@app.route("/Submenu/")
def Submenu():
	return render_template("submenu.tpl")

@app.route("/AddStaff/<int:type>")
def AddStaff(type):
        return GetStaff.AddStaff(type)

@app.route("/Add/<int:type>", methods=['POST'])
def Add(type):
        return GetStaff.PrintHeader() + GetStaff.Add(type)

@app.teardown_appcontext
def finish(ctx):
        GetStaff.store()
       
if __name__ == "__main__":
	app.run(debug=True)
