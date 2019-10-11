from ZooWorker import ZooWorker, Behaviour_DirectorZoo, Behaviour_SecurityZoo, Behaviour_KeeperZoo, Behaviour_IceCreamSellerZoo, A_Display, DirectorZoo,SecurityZoo,KeeperZoo,IceCreamSellerZoo
from flask import render_template
from flask import request
import pickle
import os

class Zoo():
    def __init__(self):
        try:
            self.reedZoo_File()
        except:
            self.ZooWorkers =[]           

    def newWorker(self, id):
        List=dict(Name = '', Surname = '', Age = '',  Gender = '', Position = '')
        List['id']=id
        return render_template("form_New.tpl", **List)

    def hire_newWorker(self):
        Menu = [self.hire_DirectorZoo, self.hire_SecurityZoo, self.hire_KeeperZoo, self.hire_IceCreamSellerZoo]
        id = int(request.form.get('id', 0))
        Menu[id]()
        return self.Write_ZooTeam()
        
    def hire_DirectorZoo(self):
        hireDirector = DirectorZoo()
        hireDirector.Read()
        self.ZooWorkers.append(hireDirector)
        
    def hire_SecurityZoo(self):
        hireSecurity = SecurityZoo()
        hireSecurity.Read()
        self.ZooWorkers.append(hireSecurity)
        
    def hire_KeeperZoo(self):
        hireKeeper = KeeperZoo()
        hireKeeper.Read()
        self.ZooWorkers.append(hireKeeper)
        
    def hire_IceCreamSellerZoo(self):
        hireIceCreamSeller = IceCreamSellerZoo()
        hireIceCreamSeller.Read()
        self.ZooWorkers.append(hireIceCreamSeller)
    
    def Write_ZooTeam(self):
        r = ""
        for (key, item) in enumerate(self.ZooWorkers):
            r += item.Write(key, "item.tpl")
        r += render_template("add.tpl")
        return r

    def dismiss_Worker(self,id):
        self.ZooWorkers.pop(int(id))
        return self.Write_ZooTeam()

    def update_form(self, id):
        return self.ZooWorkers[id].Write(id, "form_Update.tpl")
        
    def update_Worker(self):
        id = int(request.form.get('id', 0))
        self.ZooWorkers[id].Read()
        return self.Write_ZooTeam()

    def Do_something(self, id):
        return(self.ZooWorkers[id].Do() + self.Write_ZooTeam())
    
    def delete_Zoo(self):
        self.ZooWorkers.clear()
        return(self.Write_ZooTeam())

    def writeZoo_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\Zoo', '\\'), 'Zoo.p'), 'wb') as f:
            pickle.dump(self.ZooWorkers, f)
        
    def reedZoo_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\Zoo', '\\'), 'Zoo.p'), 'rb') as f:
            self.ZooWorkers = pickle.load(f)
            
    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")


