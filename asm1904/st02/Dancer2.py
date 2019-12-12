from Tancor2 import Tancor2
class Dancer2(Tancor2):
    # def do_init(self,request=None):
        # if not request:
            # self._role = int(input('Введите количество дней до дедлайна: '))
        # else:
            # if ("role" not in request.form or not request.form['role']):
                 # return("""Введите роль в спектакле: <input type="text" name="role">""")
            # else:
                # self._role = str(request.form['role'])

    # def do_edit(self,request=None):
        # if not request:
            # new_role = input('Введите количество дней до дедлайна: ')
            # self._role = int(new_role) if new_role else self._role    
        # else:
            # if ("role" not in request.form or not request.form['role']):
               # return("""Введите роль в спектакле: <input type="text" name="role">""")
            # else:
                # self._role = str(request.form['role'])

    def do_magic(self):
       
        ret = 'Я танцор'
        return(ret)

    def do_print(self):
        return(' ')