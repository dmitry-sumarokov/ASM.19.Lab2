from flask import request
import pickle
import os
from Context import Context
from Chief import Chief
from Engeneer import Engeneer
from Specialist import Specialist
from ChiefSpecialist import ChiefSpecialist
from abc import ABC, abstractmethod




class Group(ABC):
    @abstractmethod   
    def menu(self):
        pass

    @abstractmethod
    def do_magic(self):
        pass

    @abstractmethod
    def add_worker(self):
        pass
    

    @abstractmethod
    def change_worker(self):
        pass

    @abstractmethod
    def print_group(self):
        pass

    @abstractmethod
    def remove_worker(self):
        pass

    @abstractmethod
    def clear_worker(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

class Group_behav:
    def __init__(self, group: Group):

        self._group = group
        self._group._menu_list = [
                        ["Добавить начальника", Chief],
                        ["Добавить инженера", Engeneer],
                        ["Добавить специалиста", Specialist],
                        ["Добавить главного специалиста", ChiefSpecialist]
                    ]
        self._group._workers = []




class Group_web(Group):

        
    def menu(self):
        ret = []
        ret.append("------------------------------")
        for i, item in enumerate(self._menu_list):
            ret.append("{0:2}. {1}".format(i, item[0]))
        ret.append("------------------------------")
        return('<br /> '.join(ret))
    def do_magic(self, request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group(request)+"""
    <form action="/" method="POST">
        Введите номер сотрудника: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit">
    </form>
</body>
</html>""")
        else:
            ret = self._workers[int(request.form['num_w'])].do_magic_logic('<br />')
            return(ret + """
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def add_worker(self, request):
        if ("num_g" not in request.form or not request.form['num_g']):
            return(self.menu()+"""
    <form action="/" method="POST">
        Выберите номер меню: <input type="number" name="num_g">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit">
    </form>
    <form action="/" >
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
        elif ("first_name" not in request.form or not request.form['first_name']):
            context = Context(self._menu_list[int(request.form['num_g'])][1]())
            return(context.do_add_worker(request))
        else:
            context = Context(self._menu_list[int(request.form['num_g'])][1]())
            ret = context.do_add_worker(request)
            self._workers.append(context)
            return(ret)
            
    def change_worker(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group(request)+"""
    <form action="/" method="POST">
        Введите номер сотрудника: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit">
    </form>
</body>
</html>""")
        else:
            ret = self._workers[int(request.form['num_w'])].do_edit(request)
            return(ret)

            
    def print_group(self,reques):
            ret = []
            for i,w in enumerate(self._workers):
                ret.append(w.do_print(i,'<br />'))
            return('<br /> '.join(ret)+"""
    <form action="/" >
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
        
    def remove_worker(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group(request)+"""
    <form action="/" method="POST">
        Введите номер сотрудника: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit">
    </form>
</body>
</html>""")
        else:
            self._workers.pop(int(request.form['num_w']))
            return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def clear_worker(self,reques):
        self._workers.clear()
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def save_to_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('/group', '/asm1905/st19/'), 'group.p'), 'wb') as f:
            pickle.dump(self._workers, f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def load_from_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('/group', '/asm1905/st19/'), 'group.p'), 'rb') as f:
            self._workers = pickle.load(f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    


class Group_console(Group):

        
    def menu(self):
        print("------------------------------")
        for i, item in enumerate(self._menu_list):
            print("{0:2}. {1}".format(i, item[0]))
        print("------------------------------")
        return int(input())
    def do_magic(self):
        self._workers[int(input('Введите номер сотрудника: '))].do_magic_logic('\n')

    def add_worker(self):
            context = Context(self._menu_list[self.menu()][1]())
            context.do_add_worker()
            self._workers.append(context)
    def change_worker(self):
            self._workers[int(input('Введите номер сотрудника: '))].do_edit()
    def print_group(self):
            for i,w in enumerate(self._workers):
                print(w.do_print(i,'\n'))
    def remove_worker(self):
        self._workers.pop(int(input('Введите номер сотрудника: ')))
        print('Успешно')
    def clear_worker(self):
        self._workers.clear()
        print('Успешно')
    def save_to_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('/group', '/asm1905/st19/'), 'group.p'), 'wb') as f:
            pickle.dump(self._workers, f)
        print('Успешно')
    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('/group', '/asm1905/st19/'), 'group.p'), 'rb') as f:
            self._workers = pickle.load(f)
        print('Успешно')




        


