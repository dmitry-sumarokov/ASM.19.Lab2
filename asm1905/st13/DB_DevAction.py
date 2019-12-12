from CommonActions import CommonActions
from random import randint
from flask import render_template, request

class DB_DevAction:
    def __init__(self):
        pass

    def hire_alter_employee(db_dev, hire_alter):
        # CommonActions.hire_alter_employee(db_dev, hire_alter)

        if hire_alter == 0:
            db_dev.coffee = 0
        elif hire_alter == 1:
            db_dev.coffee = int(request.form.get('unique'))
        return db_dev.coffee

    # def alter_emp_params(db_dev):
    #     CommonActions.hire_alter_employee(db_dev, 1)
    #
    #     print('Enter a new number of coffee mugs: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             db_dev.coffee = int(input())
    #         else:
    #             print('Enter a NUMBER or just press \'ENTER\'!!!')
    #             pass

    def print_employees(db_dev,  act):
        if act == 0:
            return "db_hire.tpl"
        elif act == 1:
            return "db_show.tpl"
        # CommonActions.print_employees(db_dev, number)
        # print('Position - DB Dev. Number of coffee mugs per day - %s' % (db_dev.coffee))

    def print_special_action(db_dev, unique = None):
        db_dev.call_per_day = unique
        msg = ''
        try:
            if db_dev.coffee / 8 > 1:
                msg += 'You\'re next!!! Need moooooore coffee'
            else:
                msg += 'Get over here!!!'
        except Exception as e:
            msg += 'Something went wrong! f@!% CoffeeMan'
            pass
        return (msg)

    def print_brief(db_dev, number):
        CommonActions.print_brief(db_dev, number)
        pass