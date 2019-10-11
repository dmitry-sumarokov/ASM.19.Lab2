def is_float(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


def is_int(value):
	try:
		int(value)
		return True
	except ValueError:
		return False


def is_file(value):
	try:
		open(str(value) + '.dat', 'rb')
		return True
	except FileNotFoundError:
		return False


def show_menu(menu):

	print('Menu')
	for i in menu:
		print(i + ' - ' + menu[i][0])
	print('\n')