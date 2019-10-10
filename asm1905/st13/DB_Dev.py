from .Employee import Employee

class DB_Dev(Employee):
    def enter_emp_params(self):
        print('Enter the number of coffee mugs per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                self.coffee = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                # pass

    def print_emp_params(self):
        return ('Position - DB Dev. Number of coffee mugs per day - %s' % (self.coffee))

    def print_emp_brief(self):
        pass

    def alter_emp_params(self):
        print('Enter a new number of coffee mugs: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                self.coffee = int(input())
            else:
                print('Enter a NUMBER or just press \'ENTER\'!!!')
                pass

    def emp_special_action(self):
        try:
            if self.coffee / 8 > 1:
                msg = 'You\'re next!!! Need moooooore coffee'
            else:
                msg = 'Get over here!!!'
        except Exception as e:
            msg = 'Something went wrong! f@!% CoffeeMan'
            pass
        return msg