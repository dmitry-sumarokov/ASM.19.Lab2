import pickle
from flask import render_template,request
import os
from Context import Context
from AM import AM
from ATV import ATV
from MOTO import MOTO



class Group:
    def __init__(self):
        self._menu_list = [
                        AM,
						ATV,
						MOTO
                    ]
        try:
            self.load_from_file()
        except:
            self._Technic = []
            
   
    def do_it(self,id):
        ret = 'ID = '+str(id)+' Невероятно!!!<br>'
        ret += self._Technic[int(id)].do_it_logic()
        ret += self.print_group()
        return(ret)


    def get_Technic(self, id):
        if id < 0:
            return Context(self._menu_list[-id-1]())
        else:
            return self._Technic[id]

    def change_Technic(self, id):
        return self.get_Technic(id).do_print(id,"form2.tpl")


    def add_Technic(self):
        id = int(request.form.get('id', 0))
    
        item = self.get_Technic(id)
        item.do_add_Technic()

        if id <0:
            self._Technic.append(item)
        return self.print_group()
   
    def print_group(self):
        ret = ''
        for i,item in enumerate(self._Technic):
            ret += item.do_print(i, "item2.tpl")
        ret += render_template("add2.tpl")
        return ret

    def PrintHeader(self):
        return render_template("header2.tpl")

    def PrintFooter(self):
        return render_template("footer2.tpl")


    def remove_Technic(self,id):
        self._Technic.pop(int(id))
        return self.print_group()

    def clear_Technic(self):
        self._Technic.clear()
        return self.print_group()


    def save_to_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.p'), 'wb') as f:
            pickle.dump(self._Technic, f)
        return self.print_group()

    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.p'), 'rb') as f:
            self._Technic = pickle.load(f)
        return self.print_group()


        


