from CommonActions import CommonActions
from random import randint


class AnalystAction:
    def __init__(self):
        pass

    def hire_alter_employee(analyst, hire_alter):
        CommonActions.hire_alter_employee(analyst, hire_alter)

        if hire_alter == 0:
            print('Enter an average number of calls per day: ')
        elif hire_alter == 1:
            print('Enter a new average number of calls per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                analyst.avg_calls_per_day = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                pass

    def print_employees(analyst, number):
        CommonActions.print_employees(analyst, number)
        print('    Position - 			 Analyst\n	Average number of calls per day - %s' % (
            analyst.avg_calls_per_day))

    def print_special_action(analyst):
        rd = randint(0, 5)
        try:
            if (analyst.avg_calls_per_day / rd) % 2 == 0:
                msg = 'What are you doing???'
            else:
                msg = 'Are you kidding me??? What does it mean?'
        except Exception as e:
            msg = 'Something went wrong! f@!%'
            pass
        print(msg)

    def print_brief(analyst, number):
        CommonActions.print_brief(analyst, number)
        pass
