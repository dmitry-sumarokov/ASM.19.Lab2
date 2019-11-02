# from .Employee import Employee


class CommonActions:
    def __init__(self):
        pass

    def hire_alter_employee(employee, hire_alter):
        if hire_alter == 0:
            print('Enter employee\'s nickname: ')
        elif hire_alter == 1:
            print('Enter some changes or press \'ENTER\' to skip filling in the field')
            print('Enter employee\'s nickname: ')

        while True:
            nickname = input()
            if nickname:
                employee.nickname = nickname
                break
            else:
                print('Enter something!')
                pass

        print('Enter employee\'s working experience: ')

        while True:
            exp = input()
            if exp.isdigit():
                employee.exp = int(exp)
                break
            else:
                print('Enter a NUMBER!')
                pass

        print('Enter employee\'s sex (M - man or F - female): ')
        while True:
            sex = input().upper()
            if sex in ('M', 'F'):
                employee.sex = sex
                break
            else:
                print('Enter M or F!')
                pass

        print('Enter employee\'s age: ')
        while True:
            age = input()
            if age.isdigit():
                employee.age = int(age)
                break
            else:
                print('Enter a NUMBER!')
                pass

    def print_employees(employee, number):
        print('%s.  Nickname - 			 %s\n    Working experience - %s\n    Sex - 				 %s\n    Age - 	'
              '			 %s' % (number, employee.nickname, employee.exp, employee.sex, employee.age))

    def print_brief(employee, number):
        print('%s.  Nickname - %s\n'
            % (number, employee.nickname))


    # def alter_emp_params(employee):
    #
    #
    #     print('Enter employee\'s nickname: ')
    #     new_nickname = input()
    #     if new_nickname:
    #         employee.employee.nickname = new_nickname
    #
    #     print('Enter employee\'s working experience: ')
    #     while True:
    #         new_exp = input()
    #         if new_exp.isdigit():
    #             employee.employee.exp = int(new_exp)
    #             break
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass
    #
    #     print('Enter employee\'s sex (M - man or F - female): ')
    #     while True:
    #         new_sex = input().upper()
    #         if new_sex in ('M', 'F'):
    #             employee.employee.sex = new_sex
    #             break
    #         else:
    #             print('You should enter M or F or just press \'ENTER\'')
    #             pass
    #
    #     print('Enter employee\'s age: ')
    #     while True:
    #         new_age = input()
    #         if new_age.isdigit():
    #             employee.employee.age = int(new_age)
    #             break
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass

    # def print_emp_params(self, number):
    #     self.employee.print_employees(number)
    #
    # def print_emp_brief(self, number):
    #     print('%s.  Nickname - %s\n'
    #           % (number, self.employee.nickname))
    #
    #
    #
    # def emp_special_action(self):
    #     print(self.employee.emp_special_action())
