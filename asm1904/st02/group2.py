from random import randint
from flask import request
import pickle
import os
from abc import ABC, abstractmethod




class Person(ABC):
    @abstractmethod   
    def menu(self):
        pass

    @abstractmethod
    def do_magic(self):
        pass

    @abstractmethod
    def add_person(self):
        pass
    

    @abstractmethod
    def change_person(self):
        pass

    @abstractmethod
    def print_group2(self):
        pass

    @abstractmethod
    def remove_person(self):
        pass

    @abstractmethod
    def clear_person(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

class Tancor(ABC):
    ___dict__ = ('_name', '_age', '_stazh')
    @abstractmethod
    def do_magic(self):
        pass
    @abstractmethod
    def do_init(self):
        pass
    @abstractmethod
    def do_print(self):
        pass

class Choreografer(Tancor):
    def do_init(self,request = None):
        if  not request:
            self._spektakl = int(input('Введите название спектакля: '))
        else:
            if ("spektakl" not in request.form or not request.form['spektakl']):
                return("""Введите название спектакля: <input type="text" required  name="spektakl">""")
            else:
                self._spektakl = str(request.form['spektakl'])

    def do_edit(self,request = None):
        if  not request:
            new_spektakl = input('Введите название спектакля: ')
            self._spektakl = int(new_spektakl) if new_spektakl else self._spektakl
        else:
            if ("spektakl" not in request.form or not request.form['spektakl']):
                return("""Введите название спектакля: <input type="text" name="spektakl">""")
            else:
                self._spektakl = str(request.form['spektakl'])



    def do_magic(self,per):
    
        ret = 'Особое действие с хореографом'
        return(ret)

    def do_print(self,per):
        return(' ')
		
class Context():

    def __init__(self, person: Person):

        self._person = person

    def do_magic_logic(self, per):
        return(self._person.do_magic(per))
    def do_add_person(self, request=None):
        if not request:  
            self._person._name = input('Введите имя: ')
            self._person._age = input('Введите Возраст: ')
            self._person._stazh = int(input('Введите Стаж: '))
            self._person.do_init()
        else:
            if ("name" not in request.form or not request.form['name']):
                ret = str(self._person.do_init(request))
                return("""
        <form action="/" method="POST">
            Введите имя:     <input type="tet" required name="name"><br />
            Введите Возраст: <input type="number" required name="age"><br />
            Введите Стаж: <input type="number" required name="stazh"><br />
            """+ret+"""
            <input type="hidden" name="num_g" value="""+request.form['num_g']+""">
            <input type="hidden" name="num" value="""+request.form['num']+""">
            <input type="submit" value="Записать">
        </form>
    </body>
    </html>""")
            else:
                self._person._name = request.form['name']
                self._person._age = request.form['age']
                self._person._stazh = int(request.form['stazh'])
                self._person.do_init(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")

    def do_print(self,number, per):
        return('________________{0}_________________{1} Фамилия: {2}{3} Имя: {4}{5} Стаж: {6}{7} {8}'.format(
                                number,per, self._person._age,per, self._person._name,per, self._person._stazh,per, self._person.do_print(per)))


    def do_edit(self,request=None):
        if not request:
            print('Если не хотите вносить изменения, оставьте поля пустыми')
            new_name = input('Введите имя: ')
            self._person._name = new_name if new_name else self._person._name
            new_age = input('Введите Возраст: ')
            self._person._age = new_age if new_age else self._person._age
            new_stazh = input('Введите Стаж: ')
            self._person._stazh = int(new_stazh) if new_stazh else self._person._stazh 
            self._person.do_edit()
        else:
            if ("name" not in request.form):
                ret = str(self._person.do_edit(request))
                return("""
        <form action="/" method="POST">
            Если не хотите вносить изменения, оставьте поля пустыми
            Введите имя:     <input type="tet" name="name"><br />
            Введите Возраст: <input type="number" name="age"><br />
            Введите Стаж: <input type="number" name="stazh"><br />
            """+ret+"""
            <input type="hidden" name="num_w" value="""+request.form['num_w']+""">
            <input type="hidden" name="num" value="""+request.form['num']+""">
            <input type="submit" value="Добавить">
        </form>
        <form action="/" >
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")
            else:
                self._person._name = request.form['name'] if request.form['name'] else self._person._name
                self._person._age = request.form['age'] if request.form['age'] else self._person._age
                self._person._stazh = int(request.form['stazh']) if request.form['stazh'] else self._person._stazh 
                self._person.do_edit(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")


class Soloist(Tancor):
    def do_init(self,request=None):
        if not request:
            self._tryk = int(input('Введите название трюка: '))
        else:
            if ("tryk" not in request.form or not request.form['tryk']):
                  return("""Введите название трюка: <input type="text" name="tryk">""")
            else:
                self._tryk = str(request.form['tryk'])
        

    def do_edit(self,request=None):
        if not request:
            _tryk = input('Введите название трюка: ')
            self._tryk = int(_tryk) if _tryk else self._tryk
        else:
            if ("tryk" not in request.form or not request.form['tryk']):
                 return("""Введите название трюка: <input type="text" name="tryk">""")
            else:
                self._tryk = str(request.form['tryk'])

    def do_magic(self,per):
      
        ret = 'Особое действие с солистом'
        return(ret)

    def do_print(self,per):
        return(' ')




class Dancer(Tancor):
    def do_init(self,request=None):
        if not request:
            self._role = int(input('Введите роль в спектакле: '))
        else:
            if ("role" not in request.form or not request.form['role']):
                 return("""Введите роль в спектакле: <input type="text" name="role">""")
            else:
                self._role = str(request.form['role'])

    def do_edit(self,request=None):
        if not request:
            new_role = input('Введите рольв спектакле: ')
            self._role = int(new_role) if new_role else self._role    
        else:
            if ("role" not in request.form or not request.form['role']):
               return("""Введите роль в спектакле: <input type="text" name="role">""")
            else:
                self._role = str(request.form['role'])

    def do_magic(self,per):
       
        ret = 'Особое действие с танцором'
        return(ret)

    def do_print(self,per):
        return(' ')


class Person_strategy:
    def __init__(self, group2: Person):

        self._group2 = group2
        self._group2._menu_list = [
                        ["Добавить хореографа", Choreografer],
                        ["Добавить солиста", Soloist],
                        ["Добавить танцора", Dancer],		
                    ]
        self._group2._dancers = []




class Person_flask(Person):

        
    def menu(self):
        ret = []
        ret.append("------------------------------")
        for i, item in enumerate(self._menu_list):
            ret.append("{0:2}. {1}".format(i, item[0]))
        ret.append("------------------------------")
        return('<br /> '.join(ret))
    def do_magic(self, request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group2(request)+"""
    <form action="/" method="POST">
        Введите номер участника труппы: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
       <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            ret = self._dancers[int(request.form['num_w'])].do_magic_logic('<br />')
            return(ret + """
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def add_person(self, request):
        if ("num_g" not in request.form or not request.form['num_g']):
            return(self.menu()+"""
    <form action="/" method="POST">
        Выберите номер меню: <input type="number" name="num_g">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Добавить">
    </form>
    <form action="/" >
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
        elif ("name" not in request.form or not request.form['name']):
            context = Context(self._menu_list[int(request.form['num_g'])][1]())
            return(context.do_add_person(request))
        else:
            context = Context(self._menu_list[int(request.form['num_g'])][1]())
            ret = context.do_add_person(request)
            self._dancers.append(context)
            return(ret)
            
    def change_person(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group2(request)+"""
    <form action="/" method="POST">
        Введите номер участника труппы: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            ret = self._dancers[int(request.form['num_w'])].do_edit(request)
            return(ret)

            
    def print_group2(self,reques):
            ret = []
            for i,w in enumerate(self._dancers):
                ret.append(w.do_print(i,'<br />'))
            return('<br /> '.join(ret)+"""
    <form action="/" >
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
        
    def remove_person(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group2(request)+"""
    <form action="/" method="POST">
        Введите номер участника труппы: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            self._dancers.pop(int(request.form['num_w']))
            return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def clear_person(self,reques):
        self._dancers.clear()
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def save_to_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('\\group2', '\\'), 'group2.p'), 'wb') as f:
            pickle.dump(self._dancers, f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def load_from_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('\\group2', '\\'), 'group2.p'), 'rb') as f:
            self._dancers = pickle.load(f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    




        


