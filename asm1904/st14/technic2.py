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
    def print_technic2(self):
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

class Technic(ABC):
    ___dict__ = ('_name', '_color', '_year')
    @abstractmethod
    def do_magic(self):
        pass
    @abstractmethod
    def do_init(self):
        pass
    @abstractmethod
    def do_print(self):
        pass

class Auto(Technic):
    def do_init(self,request = None):
        if  not request:
            self._probeg = int(input('Введите пробег: '))
        else:
            if ("probeg" not in request.form or not request.form['probeg']):
                return("""Введите пробег: <input type="number" required  name="probeg">""")
            else:
                self._probeg = str(request.form['probeg'])

    def do_edit(self,request = None):
        if  not request:
            new_probeg = input('Введите пробег: ')
            self._probeg = int(new_probeg) if new_probeg else self._probeg
        else:
            if ("probeg" not in request.form or not request.form['probeg']):
                return("""Введите пробег: <input type="number" name="probeg">""")
            else:
                self._probeg = str(request.form['probeg'])



    def do_magic(self,per):
    
        ret = 'Эта машина! Пристегни ремень!'
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
            self._person._name = input('Введите марку: ')
            self._person._color = input('Введите цвет: ')
            self._person._year = int(input('Введите год выпуска: '))
            self._person.do_init()
        else:
            if ("name" not in request.form or not request.form['name']):
                ret = str(self._person.do_init(request))
                return("""
        <form action="/" method="POST">
            Введите марку:     <input type="tet" required name="name"><br />
            Введите цвет: <input type="tet" required name="color"><br />
            Введите год выпуска: <input type="number" required name="year"><br />
            """+ret+"""
            <input type="hidden" name="num_g" value="""+request.form['num_g']+""">
            <input type="hidden" name="num" value="""+request.form['num']+""">
            <input type="submit" value="Записать">
        </form>
    </body>
    </html>""")
            else:
                self._person._name = request.form['name']
                self._person._color = request.form['color']
                self._person._year = int(request.form['year'])
                self._person.do_init(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")

    def do_print(self,number, per):
        return('________________{0}_________________{1} Марка: {2}{3} Цвет: {4}{5} Год Выпуска: {6}{7} {8}'.format(
                                number,per, self._person._color,per, self._person._name,per, self._person._year,per, self._person.do_print(per)))


    def do_edit(self,request=None):
        if not request:
            print('Если не хотите вносить изменения, оставьте поля пустыми')
            new_name = input('Введите Марку: ')
            self._person._name = new_name if new_name else self._person._name
            new_color = input('Введите Цвет: ')
            self._person._color = new_color if new_color else self._person._color
            new_year = input('Введите Год выпуска: ')
            self._person._year = int(new_year) if new_year else self._person._year 
            self._person.do_edit()
        else:
            if ("name" not in request.form):
                ret = str(self._person.do_edit(request))
                return("""
        <form action="/" method="POST">
            Если не хотите вносить изменения, оставьте поля пустыми
            Введите Марку:     <input type="tet" name="name"><br />
            Введите Цвет: <input type="number" name="color"><br />
            Введите Год Выпуска: <input type="number" name="year"><br />
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
                self._person._color = request.form['color'] if request.form['color'] else self._person._color
                self._person._year = int(request.form['year']) if request.form['year'] else self._person._year 
                self._person.do_edit(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")


class Moto(Technic):
    def do_init(self,request=None):
        if not request:
            self._hours = int(input('Введите часы: '))
        else:
            if ("hours" not in request.form or not request.form['hours']):
                  return("""Введите часы: <input type="text" name="hours">""")
            else:
                self._hours = str(request.form['hours'])
        

    def do_edit(self,request=None):
        if not request:
            _hours = input('Введите часы: ')
            self._hours = int(_hours) if _hours else self._hours
        else:
            if ("hours" not in request.form or not request.form['hours']):
                 return("""Введите часы: <input type="text" name="hours">""")
            else:
                self._hours = str(request.form['hours'])

    def do_magic(self,per):
      
        ret = 'Это мотоцикл! Не забудь шлем!'
        return(ret)

    def do_print(self,per):
        return(' ')




class ATV(Technic):
    def do_init(self,request=None):
        if not request:
            self._iznos = int(input('Введите износ: '))
        else:
            if ("iznos" not in request.form or not request.form['iznos']):
                 return("""Введите износ: <input type="text" name="iznos">""")
            else:
                self._iznos = str(request.form['iznos'])

    def do_edit(self,request=None):
        if not request:
            new_iznos = input('Введите износ: ')
            self._iznos = int(new_iznos) if new_iznos else self._iznos    
        else:
            if ("iznos" not in request.form or not request.form['iznos']):
               return("""Введите износ: <input type="text" name="iznos">""")
            else:
                self._iznos = str(request.form['iznos'])

    def do_magic(self,per):
       
        ret = 'Это квадроцикл! Ездить только по боздорожью!'
        return(ret)

    def do_print(self,per):
        return(' ')


class Person_strategy:
    def __init__(self, technic2: Person):

        self._technic2 = technic2
        self._technic2._menu_list = [
                        ["Добавить автомобиль", Auto],
                        ["Добавить мотоцикл", Moto],
                        ["Добавить АТВ", ATV],		
                    ]
        self._technic2._ATVs = []




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
            return(self.print_technic2(request)+"""
    <form action="/" method="POST">
        Введите номер транспортного средства: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
       <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            ret = self._ATVs[int(request.form['num_w'])].do_magic_logic('<br />')
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
            self._ATVs.append(context)
            return(ret)
            
    def change_person(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_technic2(request)+"""
    <form action="/" method="POST">
        Введите номер транспортного средства: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            ret = self._ATVs[int(request.form['num_w'])].do_edit(request)
            return(ret)

            
    def print_technic2(self,reques):
            ret = []
            for i,w in enumerate(self._ATVs):
                ret.append(w.do_print(i,'<br />'))
            return('<br /> '.join(ret)+"""
    <form action="/" >
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
        
    def remove_person(self,request):
        if ("num_w" not in request.form or not request.form['num_w']):
            return(self.print_technic2(request)+"""
    <form action="/" method="POST">
        Введите транспортного средства: <input type="number" name="num_w">
        <input type="hidden" name="num" value="""+request.form['num']+""">
        <input type="submit" value="Записать">
    </form>
</body>
</html>""")
        else:
            self._ATVs.pop(int(request.form['num_w']))
            return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def clear_person(self,reques):
        self._ATVs.clear()
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def save_to_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('\\technic2', '\\'), 'technic2.p'), 'wb') as f:
            pickle.dump(self._ATVs, f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    def load_from_file(self,reques):
        with open(os.path.join(os.path.abspath(__name__).replace('\\technic2', '\\'), 'technic2.p'), 'rb') as f:
            self._ATVs = pickle.load(f)
        return("""
    <form action="/" >
        Успешно
        <input type="submit" value="На главную">
    </form>
</body>
</html>""")
    




        


