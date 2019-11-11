from Encyclo import Encyclo
from flask import Flask
from flask import g

app = Flask(__name__)

def GetEncyclo():
        if 'NewEncyclo' not in g:
                g.NewEncyclo=Encyclo()
        return g.NewEncyclo

@app.route("/")
def index():
	return GetEncyclo().PrintHeader() + GetEncyclo().Write_Encyclo() + GetEncyclo().PrintFooter()

@app.route("/modify_form/<int:id>")
def modify_form(id):
	return GetEncyclo().PrintHeader() + GetEncyclo().modify_form(id) + GetEncyclo().PrintFooter()

@app.route("/modify", methods=['POST'])  
def modify_Animal():
	return GetEncyclo().PrintHeader() + GetEncyclo().modify_Animal() + GetEncyclo().PrintFooter()

@app.route("/new_form/<int:id>")
def newAnimal(id):
	return GetEncyclo().PrintHeader() + GetEncyclo().newAnimal(id) + GetEncyclo().PrintFooter()

@app.route("/New", methods=['POST'])  
def Edit_newAnimal():
	return GetEncyclo().PrintHeader() + GetEncyclo().Edit_newAnimal() + GetEncyclo().PrintFooter()

@app.route("/delete_Animal/<int:id>")
def delete_Animal(id):
	return GetEncyclo().PrintHeader() + GetEncyclo().delete_Animal(id) + GetEncyclo().PrintFooter()

@app.route("/Feature_animal/<int:id>")
def Feature_animal(id):
	return GetEncyclo().PrintHeader() + GetEncyclo().Feature_animal(id) + GetEncyclo().PrintFooter()

@app.route("/delete_Encyclo")
def delete_Encyclo():
	return GetEncyclo().PrintHeader() + GetEncyclo().delete_Encyclo() + GetEncyclo().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        GetEncyclo().writeEncyclo_File()
        

if __name__ == "__main__":
	app.run(debug=True)
        

