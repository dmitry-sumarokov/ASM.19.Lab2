from .Employee import Employee
from random import randint

class DevOps(Employee):
	def enter_emp_params(self):
		print('Enter a salary for almighty one: ')
		while True:
			new_val = input()
			if new_val and new_val.isdigit():
				self.salary = int(new_val)
				break
			else:
				print('Enter a NUMBER!!!')
				# pass

	def print_emp_params(self):
		return('Position - DevOps. Salary - %s'%(self.salary))

	def print_emp_brief(self):
		pass

	def alter_emp_params(self):
		print('Enter a new salary: ')
		while True:
			new_val = input()
			if new_val and new_val.isdigit():
				self.salary = int(input())
			else:
				print('Enter a NUMBER or just press \'ENTER\'!!!')
				pass

	def emp_special_action(self):
		rd = randint(0, 10)

		try:
			if self.salary * rd > self.salary * 5:
				msg = 'God mode is on!!!'
			else:
				msg = 'You lost your privileges)'
		except Exception as e:
			msg = 'Something went wrong! f@!%'
			pass
		return msg