from Animals import Animals, Behaviour_Mammals, Behaviour_Fish, Behaviour_Bird, Behaviour_Reptile, Disp, Mammals,Fish,Bird,Reptile
from flask import render_template
from flask import request
import pickle
import os

class Encyclo():
    def __init__(self):
        try:
            self.readEncyclo_File()
        except:
            self.Animals=[]
            
    def newAnimal(self, id):
        List=dict(Name = '', Klass = '', Age = '',  MaxAge = '', Detki = '')
        List['id']=id
        return render_template("form_New.tpl", **List)
    
    def Edit_newAnimal(self):
        Menu = [self.Edit_Mammals, self.Edit_Fish, self.Edit_Bird, self.Edit_Reptile]
        id = int(request.form.get('id', 0))
        Menu[id]()
        return self.Write_Encyclo()
        
    def Edit_Mammals(self):
        EditMammals = Mammals()
        EditMammals.Read()
        self.Animals.append(EditMammals)
        
    def Edit_Fish(self):
        EditFish = Fish()
        EditFish.Read()
        self.Animals.append(EditFish)
        
    def Edit_Bird(self):
        EditBird = Bird()
        EditBird.Read()
        self.Animals.append(EditBird)
        
    def Edit_Reptile(self):
        EditReptile = Reptile()
        EditReptile.Read()
        self.Animals.append(EditReptile)

    def Write_Encyclo(self):
        r = ""
        for (key, item) in enumerate(self.Animals):
            r += item.Write(key, "item.tpl")
        r += render_template("add.tpl")
        return r

    def delete_Animal(self, id):
        self.Animals.pop(int(id))
        return self.Write_Encyclo()
        
    def modify_form(self, id):
        return self.Animals[id].Write(id, "form_Modify.tpl")
    
    def modify_Animal(self):
        id = int(request.form.get('id', 0))
        self.Animals[id].Read()
        return self.Write_Encyclo()

    def Feature_animal(self, id):
        return (self.Animals[id].Feature() + self.Write_Encyclo())
    
    def delete_Encyclo(self):
        self.Animals.clear()
        return (self.Write_Encyclo())

    def writeEncyclo_File(self):
        with open('Encyclo.p', 'wb') as f:
            pickle.dump(self.Animals, f)
        
    def readEncyclo_File(self):
        with open('Encyclo.p', 'rb') as f:
            self.Animals= pickle.load(f)

    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")  

