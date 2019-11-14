import pickle
from flask import render_template,request
import os
from Context2 import Context2
from Choreografer2 import Choreografer2
from Dancer2 import Dancer2
from Soloist2 import Soloist2



class Group:
    def __init__(self):
        self._menu_list = [
                        Dancer2,
						Soloist2,
						Choreografer2
                    ]
        try:
            self.load_from_file()
        except:
            self._Tancors2 = []
            
   
    def do_magic(self,id):
        ret = 'ID = '+str(id)+' This is Magic!<br>'
        ret += self._Tancors2[int(id)].do_magic_logic()
        ret += self.print_group()
        return(ret)


    def get_Tancor2(self, id):
        if id < 0:
            return Context2(self._menu_list[-id-1]())
        else:
            return self._Tancors2[id]

    def change_Tancor2(self, id):
        return self.get_Tancor2(id).do_print(id,"form2.tpl")


    def add_Tancor2(self):
        id = int(request.form.get('id', 0))
    
        item = self.get_Tancor2(id)
        item.do_add_Tancor2()

        if id <0:
            self._Tancors2.append(item)
        return self.print_group()
   
    def print_group(self):
        ret = ''
        for i,item in enumerate(self._Tancors2):
            ret += item.do_print(i, "item2.tpl")
        ret += render_template("add2.tpl")
        return ret

    def PrintHeader(self):
        return render_template("header2.tpl")

    def PrintFooter(self):
        return render_template("footer2.tpl")


    def remove_Tancor2(self,id):
        self._Tancors2.pop(int(id))
        return self.print_group()

    def clear_Tancor2(self):
        self._Tancors2.clear()
        return self.print_group()


    def save_to_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group2', '\\'), 'group.p'), 'wb') as f:
            pickle.dump(self._Tancors2, f)
        return self.print_group()

    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group2', '\\'), 'group.p'), 'rb') as f:
            self._Tancors2 = pickle.load(f)
        return self.print_group()


        


