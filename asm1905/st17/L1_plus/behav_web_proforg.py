from random import randint

from flask import render_template

from .web_behavior import WebBehaviorStud


class BWebProforg:
    def __init__(self):
        pass

    @staticmethod
    def do_input(proforg_, data):
        WebBehaviorStud.stand_do_input(proforg_, data)
        proforg_.amount_contribution = float(data['amount_contribution'])

    @staticmethod
    def do_print(proforg_, index):
        fields = {'Имя': proforg_.first_name, 'Фамилия': proforg_.second_name,
                  'Пол': proforg_.gender, 'Возраст': proforg_.age,
                  'Величина взноса': proforg_.amount_contribution}
        return render_template('print_student.html', index=index, fields=fields, type='Профорг')

    @staticmethod
    def do_edit(proforg_, data):
        if 'web' in data:
            return render_template('common_change.html', number=data['web'], name=proforg_.first_name,
                                   sec_name=proforg_.second_name, gender=proforg_.gender,
                                   age=proforg_.age) + render_template(f'change_proforg.html',
                                                                       am_contr=proforg_.amount_contribution)
        WebBehaviorStud.stand_do_edit(proforg_, data)
        proforg_.amount_contribution = float(data['amount_contribution']) if data['amount_contribution'] \
                                                                          else proforg_.amount_contribution

    @staticmethod
    def do_magic(proforg_):
        c_sum = proforg_.amount_contribution * randint(0, 10)
        return render_template('magic_proforg.html', sum=c_sum)
