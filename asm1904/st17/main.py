if __name__ == '__main__':
    from conteiner import Container
else:
    from .conteiner import Container


from conteiner import Container
from flask import Flask
from flask import g

app = Flask(__name__)

def GetAnimal():
        if 'MyAnimal' not in g:
            	g.MyAnimal=Container()
        return g.MyAnimal

@app.route("/")
def index():
	return GetAnimal().PrintHeader() + GetAnimal().printlist() + GetAnimal().PrintFooter()

@app.route("/update_form/<int:id>")
def update_form(id):
	return GetAnimal().PrintHeader() + GetAnimal().update_form(id) + GetAnimal().PrintFooter()

@app.route("/Update", methods=['POST']) 
def edit_elem():
	return GetAnimal().PrintHeader() + GetAnimal().edit_elem() + GetAnimal().PrintFooter()

@app.route("/new_form/<int:id>")
def newAnimal(id):
	return GetAnimal().PrintHeader() + GetAnimal().newAnimal(id) + GetAnimal().PrintFooter()

@app.route("/New", methods=['POST'])  
def add_newAnimal():
	return GetAnimal().PrintHeader() + GetAnimal().add_newAnimal() + GetAnimal().PrintFooter()

@app.route("/remove_elem/<int:id>")
def remove_elem(id):
	return GetAnimal().PrintHeader() + GetAnimal().remove_elem(id) + GetAnimal().PrintFooter()

@app.route("/different/<int:id>")
def different(id):
	return GetAnimal().PrintHeader() + GetAnimal().different(id) + GetAnimal().PrintFooter()

@app.route("/clearlist")
def clearlist():
	return GetAnimal().PrintHeader() + GetAnimal().clearlist() + GetAnimal().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
    GetAnimal().recording()
        

if __name__ == "__main__":
	app.run(debug=True)
        


        







          
