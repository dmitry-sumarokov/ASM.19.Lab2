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
    def print_group2Sin(self):
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

class Animal(ABC):
    ___dict__ = ('_name', '_year', '_gender')
    @abstractmethod
    def do_magic(self):
        pass
    @abstractmethod
    def do_init(self):
        pass
    @abstractmethod
    def do_print(self):
        pass

class Cat(Animal):
    def do_init(self,request = None):
        if  not request:
            self._poroda = int(input('Введите породу: '))
        else:
            if ("poroda" not in request.form or not request.form['poroda']):
                return("""Введите породу: <input type="tet" required  name="poroda">""")
            else:
                self._poroda = str(request.form['poroda'])

    def do_edit(self,request = None):
        if  not request:
            new_poroda = input('Введите породу: ')
            self._poroda = int(new_poroda) if new_poroda else self._poroda
        else:
            if ("poroda" not in request.form or not request.form['poroda']):
                return("""Введите породу: <input type="tet" name="poroda">""")
            else:
                self._poroda = str(request.form['poroda'])



    def do_magic(self,per):
    
        ret = 'Эта котик! Он может оцарапать!'
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
            self._person._name = input('Введите Имя: ')
            self._person._year = input('Введите Возраст: ')
            self._person._gender = str(input('Введите Пол: '))
            self._person.do_init()
        else:
            if ("name" not in request.form or not request.form['name']):
                ret = str(self._person.do_init(request))
                return("""
        <form action="/" method="POST">
            Введите Имя:     <input type="tet" required name="name"><br />
            Введите Возраст: <input type="num" required name="year"><br />
            Введите Пол: <input type="tet" required name="gender"><br />
            """+ret+"""
            <input type="hidden" name="num_g" value="""+request.form['num_g']+""">
            <input type="hidden" name="num" value="""+request.form['num']+""">
            <input type="submit" value="Записать">
        </form>
    </body>
    </html>""")
            else:
                self._person._name = request.form['name']
                self._person._year = request.form['year']
                self._person._gender = str(request.form['gender'])
                self._person.do_init(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")

    def do_print(self,number, per):
        return('________________{0}_________________{1} Имя: {2}{3} Возраст: {4}{5} Пол: {6}{7} {8}'.format(
                                number,per, self._person._year,per, self._person._name,per, self._person._gender,per, self._person.do_print(per)))


    def do_edit(self,request=None):
        if not request:
            print('Если не хотите вносить изменения, оставьте поля пустыми')
            new_name = input('Введите Имя: ')
            self._person._name = new_name if new_name else self._person._name
            new_year = input('Введите Возраст: ')
            self._person._year = new_year if new_year else self._person._year
            new_gender = input('Введите Пол: ')
            self._person._gender = str(new_gender) if new_gender else self._person._gender 
            self._person.do_edit()
        else:
            if ("name" not in request.form):
                ret = str(self._person.do_edit(request))
                return("""
        <form action="/" method="POST">
            Если не хотите вносить изменения, оставьте поля пустыми
            Введите Имя:     <input type="tet" name="name"><br />
            Введите Возраст: <input type="number" name="year"><br />
            Введите Пол: <input type="tet" name="gender"><br />
            """+ret+"""
            <input type="hidden" name="num_w" value="""+request.form['num_w']+""">
            <input type="hidden" name="tet" value="""+request.form['num']+""">
            <input type="submit" value="Добавить">
        </form>
        <form action="/" >
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")
            else:
                self._person._name = request.form['name'] if request.form['name'] else self._person._name
                self._person._year = request.form['year'] if request.form['year'] else self._person._year
                self._person._gender = str(request.form['gender']) if request.form['gender'] else self._person._gender 
                self._person.do_edit(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")


class Dog(Animal):
    def do_init(self,request=None):
        if not request:
            self._okras = str(input('Введите окрас: '))
        else:
            if ("okras" not in request.form or not request.form['okras']):
                  return("""Введите окрас: <input type="text" name="okras">""")
            else:
                self._okras = str(request.form['okras'])
        

    def do_edit(self,request=None):
        if not request:
            _okras = input('Введите окрас: ')
            self._okras = str(_okras) if _okras else self._okras
        else:
            if ("okras" not in request.form or not request.form['okras']):
                 return("""Введите окрас: <input type="text" name="okras">""")
            else:
                self._okras = str(request.form['okras'])

    def do_magic(self,per):
      
        ret = 'Это Собака! Она может укусить!'
        return(ret)

    def do_print(self,per):
        return(' ')




class Rabbit(Animal):
    def do_init(self,request=None):
        if not request:
            self._food = int(input('Введите любимую еду: '))
        else:
            if ("food" not in request.form or not request.form['food']):
                 return("""Введите любимую еду: <input type="text" name="food">""")
            else:
                self._food = str(request.form['food'])

    def do_edit(self,request=None):
        if not request:
            new_food = input('Введите любимую еду: ')
            self._food = str(new_food) if new_food else self._food    
        else:
            if ("food" not in request.form or not request.form['food']):
               return("""Введите любимую еду: <input type="text" name="food">""")
            else:
                self._food = str(request.form['food'])

    def do_magic(self,per):
       
        ret = 'Это кролиу! Он может убежать!'
        return(ret)

    def do_print(self,per):
        return(' ')


class Person_strategy:
    def __init__(self, group2Sin: Person):

        self._group2Sin = group2Sin
        self._group2Sin._menu_list = [
                        ["Добавить котика", Cat],
                        ["Добавить собаку", Dog],
                        ["Добавить кролика", Rabbit],		
                    ]
        self._group2Sin._Rabbits = []




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
            return(self.print_group2Sin(request)+"""
    <form action="/" method="POST">
        Введите номер Питомца: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
       <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            ret = self._Rabbits[int(request.form['num_w'])].do_magic_logic('<br />')
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
            self._Rabbits.append(context)
            return(ret)
            
    def change_person(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group2Sin(request)+"""
    <form action="/" method="POST">
        Введите номер Питомца: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            ret = self._Rabbits[int(request.form['num_w'])].do_edit(request)
            return(ret)

            
    def print_group2Sin(self,reques):
            ret = []
            for i,w in enumerate(self._Rabbits):
                ret.append(w.do_print(i,'<br />'))
            return('<br /> '.join(ret)+"""
    <form action="/" >
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
        
    def remove_person(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_group2Sin(request)+"""
    <form action="/" method="POST">
        Введите номер Питомца: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            self._Rabbits.pop(int(request.form['num_w']))
            return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def clear_person(self,reques):
        self._Rabbits.clear()
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def save_to_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('\\group2Sin', '\\'), 'group2Sin.p'), 'wb') as f:
            pickle.dump(self._Rabbits, f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def load_from_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('\\group2Sin', '\\'), 'group2Sin.p'), 'rb') as f:
            self._Rabbits = pickle.load(f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    




        


