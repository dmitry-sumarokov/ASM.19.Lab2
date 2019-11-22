from group import Students
from student import Student
from flask import Flask
from flask import g

app = Flask(__name__)

def GetStudents():
        if 'Students' not in g:
                g.Students = Students()              
        return g.Students

def GetStudent():
        if 'student' not in g:
                g.Student = Student()
        return g.Student
    
@app.route("/")
def index():
	return GetStudents().PrintHeader() + GetStudents().ShowStudents() + GetStudents().PrintFooter()

@app.route("/StudentBehaviour/<int:id>/<int:f>")
def StudentBehaviour(id, f): 
    return GetStudents().PrintHeader() + GetStudents().StudentBehaviour(id, f) + GetStudents().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetStudents().PrintHeader() + GetStudents().ShowForm(id) + GetStudents().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetStudents().PrintHeader() + GetStudents().DeleteItem(id) + GetStudents().PrintFooter()

@app.route("/AddItemBachelor", methods=['POST'])
def AddItemStudent():
	return GetStudents().PrintHeader() + GetStudents().AddItemBachelor() + GetStudents().PrintFooter()

@app.route("/AddItemMaster", methods=['POST'])
def AddItemMaster():
	return GetStudents().PrintHeader() + GetStudents().AddItemMaster() + GetStudents().PrintFooter()

@app.route("/AddItemGraduate_student", methods=['POST'])
def AddItemGraduate_student():
	return GetStudents().PrintHeader() + GetStudents().AddItemGraduate_student() + GetStudents().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        GetStudents().store()

       
if __name__ == "__main__":
	app.run(debug=True)
