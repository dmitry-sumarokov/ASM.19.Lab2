from .Employee import Employee


class Common_Params:
    def __init__(self):
        self.employee = Employee
        # self.employee.type =

    def hire_employee(self):
        print('Enter employee\'s nickname: ')
        self.employee.nickname = input()

        print('Enter employee\'s working experience: ')
        while True:
            exp = input()
            if exp.isdigit():
                self.employee.exp = int(exp)
                break
            else:
                print('Enter a NUMBER!')
                pass

        print('Enter employee\'s sex (M - man or F - female): ')
        while True:
            sex = input().upper()
            if sex in ('M', 'F'):
                self.employee.sex = sex
                break
            else:
                print('Enter M or F!')
                pass

        print('Enter employee\'s age: ')
        while True:
            age = input()
            if age.isdigit():
                self.employee.age = int(age)
                break
            else:
                print('Enter a NUMBER!')
                pass

        # self.employee.enter_emp_params()

    def print_emps(self, number):
        print('%s.  Nickname - 			 %s\n    Working experience - %s\n    Sex - 				 %s\n    Age - 	'
              '			 %s'
              % (number, self.employee.nickname, self.employee.exp, self.employee.sex, self.employee.age))

    def print_emps_brief(self, number):
        print('%s.  Nickname - %s\n'
              % (number, self.employee.nickname))

    def alter_emp(self):
        print('Enter some changes or press \'ENTER\' to skip filling in the field')

        print('Enter employee\'s nickname: ')
        new_nickname = input()
        if new_nickname:
            self.employee.nickname = new_nickname

        print('Enter employee\'s working experience: ')
        while True:
            new_exp = input()
            if new_exp.isdigit():
                self.employee.exp = int(new_exp)
                break
            else:
                print('You should enter a NUMBER or just press \'ENTER\'')
                pass

        print('Enter employee\'s sex (M - man or F - female): ')
        while True:
            new_sex = input().upper()
            if new_sex in ('M', 'F'):
                self.employee.sex = new_sex
                break
            else:
                print('You should enter M or F or just press \'ENTER\'')
                pass

        print('Enter employee\'s age: ')
        while True:
            new_age = input()
            if new_age.isdigit():
                self.employee.age = int(new_age)
                break
            else:
                print('You should enter a NUMBER or just press \'ENTER\'')
                pass

        # self.employee.enter_emp_params()

    def emp_sp_action(self):
        print(self.employee.emp_special_action())
