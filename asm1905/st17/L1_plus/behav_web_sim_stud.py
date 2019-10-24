from flask import render_template

from .web_behavior import WebBehaviorStud


class BWebSimpStudent:
    def __init__(self):
        pass

    @staticmethod
    def do_input(simple_student, data):
        WebBehaviorStud.stand_do_input(simple_student, data)
        simple_student.performance = float(data['performance'])

    @staticmethod
    def do_print(simple_student, index):
        fields = {'Имя': simple_student.first_name, 'Фамилия': simple_student.second_name,
                  'Пол': simple_student.gender, 'Возраст': simple_student.age,
                  'Успеваемость': simple_student.performance}
        return render_template('print_student.html', index=index, fields=fields, type='Обычный студент')

    @staticmethod
    def do_edit(simple_student, data):
        if 'web' in data:
            return render_template('common_change.html', number=data['web'], name=simple_student.first_name,
                                   sec_name=simple_student.second_name, gender=simple_student.gender,
                                   age=simple_student.age) + render_template(f'change_student.html',
                                                                             perform=simple_student.performance)
        WebBehaviorStud.stand_do_edit(simple_student, data)
        simple_student.performance = float(data['performance']) if data['performance'] else simple_student.performance

    @staticmethod
    def do_magic(simple_student):
        simple_student.performance -= 0.1
        return render_template('magic_stud.html')
