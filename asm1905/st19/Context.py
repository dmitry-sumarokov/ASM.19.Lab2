from Worker import Worker
from flask import request





class Context():

    def __init__(self, worker: Worker):

        self._worker = worker

    def do_magic_logic(self, per):
        return(self._worker.do_magic(per))
    def do_add_worker(self, request=None):
        if not request:  
            self._worker._first_name = input('Введите имя: ')
            self._worker._second_name = input('Введите фамилию: ')
            self._worker._gender = input('Введите пол: ')
            self._worker._age = int(input('Введите возраст: '))
            self._worker.do_init()
        else:
            if ("first_name" not in request.form or not request.form['first_name']):
                ret = str(self._worker.do_init(request))
                return("""
        <form action="/" method="POST">
            Введите имя:     <input type="tet" required name="first_name"><br />
            Введите фамилию: <input type="tet" required name="second_name"><br />
            Введите пол:     <input type="tet" required name="gender"><br />
            Введите возраст: <input type="number" required name="age"><br />
            """+ret+"""
            <input type="hidden" name="num_g" value="""+request.form['num_g']+""">
            <input type="hidden" name="num" value="""+request.form['num']+""">
            <input type="submit">
        </form>
    </body>
    </html>""")
            else:
                self._worker._first_name = request.form['first_name']
                self._worker._second_name = request.form['second_name']
                self._worker._gender = request.form['gender']
                self._worker._age = int(request.form['age'])
                self._worker.do_init(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")

    def do_print(self,number, per):
        return('________________{0}_________________{1} Фамилия: {2}{3} Имя: {4}{5} Пол: {6}{7} Возраст: {8}{9} {10}'.format(
                                number,per, self._worker._second_name,per, self._worker._first_name,per, self._worker._gender,per, self._worker._age,per, self._worker.do_print(per)))


    def do_edit(self,request=None):
        if not request:
            print('Если не хотите вносить изменения, оставьте поля пустыми')
            new_first_name = input('Введите имя: ')
            self._worker._first_name = new_first_name if new_first_name else self._worker._first_name
            new_second_name = input('Введите фамилию: ')
            self._worker._second_name = new_second_name if new_second_name else self._worker._second_name
            new_gender = input('Введите пол: ')
            self._worker._gender = new_gender if new_gender else self._worker._gender
            new_age = input('Введите возраст: ')
            self._worker._age = int(new_age) if new_age else self._worker._age 
            self._worker.do_edit()
        else:
            if ("first_name" not in request.form):
                ret = str(self._worker.do_edit(request))
                return("""
        <form action="/" method="POST">
            Если не хотите вносить изменения, оставьте поля пустыми
            Введите имя:     <input type="tet" name="first_name"><br />
            Введите фамилию: <input type="tet" name="second_name"><br />
            Введите пол:     <input type="tet" name="gender"><br />
            Введите возраст: <input type="number" name="age"><br />
            """+ret+"""
            <input type="hidden" name="num_w" value="""+request.form['num_w']+""">
            <input type="hidden" name="num" value="""+request.form['num']+""">
            <input type="submit">
        </form>
        <form action="/" >
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")
            else:
                self._worker._first_name = request.form['first_name'] if request.form['first_name'] else self._worker._first_name
                self._worker._second_name = request.form['second_name'] if request.form['second_name'] else self._worker._second_name
                self._worker._gender = request.form['gender'] if request.form['gender'] else self._worker._gender
                self._worker._age = int(request.form['age']) if request.form['age'] else self._worker._age 
                self._worker.do_edit(request)
                return("""
        <form action="/" >
            Успешно
            <input type="submit" value="На главную">
        </form>
    </body>
    </html>""")



        
      
      
