from flask import render_template
from flask import request
from director import Director
from finansist import Finansist
from designer import Designer
from person import Person
import pickle

class Company:
    def __init__(self):
        try:
            self.load()
        except:
            self.staff = {}
            self.maxid = 0

    def PrintHeader(self):
        return render_template("header.tpl")

    def load(self):
        with open('staff.db', 'rb') as f:
            (self.maxid, self.staff) = pickle.load(f)

    def store(self):
        with open('staff.db', 'wb') as f:
            pickle.dump((self.maxid, self.staff), f)

    def ShowStaff(self):
        r = ""
        for (key, i) in self.staff.items():
            r += i.Show()
        r += render_template("menu.tpl")
        return r

    def AddStaff(self, type):
        if type==0:
            return render_template("director.tpl")
        elif type==1:
            return render_template("finansist.tpl")
        else: return render_template("designer.tpl")

    def Add(self, type):
        if type==0:
            i = Director()
        elif type==1:
            i = Finansist()
        else: i = Designer()

        i.SetData()
        self.maxid += 1
        print(self.maxid)
        i.id = self.maxid
        print(i.id)
        self.staff[i.id] = i
        return self.ShowStaff()

    def DeleteItem(self, id):
        del(self.staff[id])
        if id > 1:
            print(self.maxid)
            for i in range(id+1,self.maxid+1):
                self.staff[i].id -= 1
                self.staff[i-1] = self.staff[i]
                del(self.staff[i])
        self.maxid -= 1
        print(self.maxid)
        return self.ShowStaff()

    def DeleteStaff(self):
        self.staff.clear()
        self.maxid = 0
        return self.ShowStaff()
    
"""class Person:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.surname = ''
        self.age = ''
        self.wexp = ''
        
    def SetData(self):
        self.id = request.form.get('id')
        self.name = request.form.get('name')
        self.surname = request.form.get('surname')
        self.age = request.form.get('age')
        self.wexp = request.form.get('wexp')

    def Show(self, tpl):
        return render_template(tpl, **self.__dict__)
        
    def add_staff(self):
        print()
        for i, item in enumerate(self.menu):
            print(f'{i} - {item[0]}')
        print()
        num = int(input())
        self.staff.append(self.menu[num][1]())

    def edit_staff(self):
        self.staff[int(input('Введите номер сотрудника: '))].edit()
        print('--------------------')
        print('Изменения сохранены')

    def delete_staff(self):
        self.staff.pop(int(input('Введите номер сотрудника: ')))

    def delete_all(self):
        self.staff.clear()

    def show_staff(self):
        for i, staff in enumerate(self.staff):
            print(staff.__class__.__name__+' [id: '+str(i)+']')
            staff.print()

    def save_staff(self):
        f = open(r'data.txt', 'wb')
        pickle.dump(self.staff, f)
        f.close()
        print('Список сохранен')

    def load_staff(self):
        f = open(r'data.txt', 'rb')
        self.staff = pickle.load(f)
        print('Список загружен')"""
