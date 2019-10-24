from flask import render_template

from .web_behavior import WebBehaviorStud


class BWebStarosta:
    def __init__(self):
        pass

    @staticmethod
    def do_input(starosta_, data):
        WebBehaviorStud.stand_do_input(starosta_, data)
        starosta_.scholarship = float(data['scholarship'])

    @staticmethod
    def do_print(starosta_, index):
        fields = {'Имя': starosta_.first_name, 'Фамилия': starosta_.second_name,
                  'Пол': starosta_.gender, 'Возраст': starosta_.age,
                  'Надбавка к стипендии': starosta_.scholarship}
        return render_template('print_student.html', index=index, fields=fields, type='Староста')

    @staticmethod
    def do_edit(starosta_, data):
        if 'web' in data:
            return render_template('common_change.html', number=data['web'], name=starosta_.first_name,
                                   sec_name=starosta_.second_name, gender=starosta_.gender,
                                   age=starosta_.age) + render_template(f'change_starosta.html',
                                                                        scholarship=starosta_.scholarship)
        WebBehaviorStud.stand_do_edit(starosta_, data)
        starosta_.scholarship = float(data['scholarship']) if data['scholarship'] else starosta_.scholarship

    @staticmethod
    def do_magic(starosta_):
        starosta_.scholarship += 5
        return render_template('magic_starosta.html')
