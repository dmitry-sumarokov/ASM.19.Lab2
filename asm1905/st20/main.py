from Zoo import Zoo
from flask import Flask
from flask import g

app = Flask(__name__)

def GetZoo():
        if 'MyZoo' not in g:
                g.MyZoo=Zoo()
        return g.MyZoo

@app.route("/")
def index():
	return GetZoo().PrintHeader() + GetZoo().Write_ZooTeam() + GetZoo().PrintFooter()

@app.route("/update_form/<int:id>")
def update_form(id):
	return GetZoo().PrintHeader() + GetZoo().update_form(id) + GetZoo().PrintFooter()

@app.route("/Update", methods=['POST'])  
def update_Worker():
	return GetZoo().PrintHeader() + GetZoo().update_Worker() + GetZoo().PrintFooter()

@app.route("/new_form/<int:id>")
def newWorker(id):
	return GetZoo().PrintHeader() + GetZoo().newWorker(id) + GetZoo().PrintFooter()

@app.route("/New", methods=['POST'])  
def hire_newWorker():
	return GetZoo().PrintHeader() + GetZoo().hire_newWorker() + GetZoo().PrintFooter()

@app.route("/dismiss_Worker/<int:id>")
def dismiss_Worker(id):
	return GetZoo().PrintHeader() + GetZoo().dismiss_Worker(id) + GetZoo().PrintFooter()

@app.route("/Do_something/<int:id>")
def Do_something(id):
	return GetZoo().PrintHeader() + GetZoo().Do_something(id) + GetZoo().PrintFooter()

@app.route("/delete_Zoo")
def delete_Zoo():
	return GetZoo().PrintHeader() + GetZoo().delete_Zoo() + GetZoo().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        GetZoo().writeZoo_File()
        

if __name__ == "__main__":
	app.run(debug=True)
        










          
