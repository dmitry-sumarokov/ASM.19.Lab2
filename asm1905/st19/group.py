import pickle
from flask import render_template,request
import os
from Context import Context
from Chief import Chief
from Engeneer import Engeneer
from Specialist import Specialist
from ChiefSpecialist import ChiefSpecialist



class Group:
    def __init__(self):
        self._menu_list = [
                        Chief,
                        Engeneer,
                        Specialist,
                        ChiefSpecialist
                    ]
        try:
            self.load_from_file()
        except:
            self._workers = []
            
   
    def do_magic(self,id):
        ret = 'ID = '+str(id)+' This is Magic!<br>'
        ret += self._workers[int(id)].do_magic_logic()
        ret += self.print_group()
        return(ret)


    def get_worker(self, id):
        if id < 0:
            return Context(self._menu_list[-id-1]())
        else:
            return self._workers[id]

    def change_worker(self, id):
        return self.get_worker(id).do_print(id,"form.tpl")


    def add_worker(self):
        id = int(request.form.get('id', 0))
    
        item = self.get_worker(id)
        item.do_add_worker()

        if id <0:
            self._workers.append(item)
        return self.print_group()
   
    def print_group(self):
        ret = ''
        for i,item in enumerate(self._workers):
            ret += item.do_print(i, "item.tpl")
        ret += render_template("add.tpl")
        return ret

    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")


    def remove_worker(self,id):
        self._workers.pop(int(id))
        return self.print_group()

    def clear_worker(self):
        self._workers.clear()
        return self.print_group()


    def save_to_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.p'), 'wb') as f:
            pickle.dump(self._workers, f)
    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.p'), 'rb') as f:
            self._workers = pickle.load(f)
    


        


