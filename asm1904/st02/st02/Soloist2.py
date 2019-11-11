from Tancor2 import Tancor2
class Soloist2(Tancor2):
    # def do_init(self,request=None):
        # if not request:
            # self._tryk = int(input('Введите название трюка: '))
        # else:
            # if ("tryk" not in request.form or not request.form['tryk']):
                  # return("""Введите название трюка: <input type="text" name="tryk">""")
            # else:
                # self._tryk = str(request.form['tryk'])
        

    # def do_edit(self,request=None):
        # if not request:
            # _tryk = input('Введите название трюка: ')
            # self._tryk = int(_tryk) if _tryk else self._tryk
        # else:
            # if ("tryk" not in request.form or not request.form['tryk']):
                 # return("""Введите название трюка: <input type="text" name="tryk">""")
            # else:
                # self._tryk = str(request.form['tryk'])

    def do_magic(self):
      
        ret = 'Я солист'
        return(ret)

    def do_print(self):
        return(' ')