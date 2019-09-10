import os, sys, threading, time

#	добавить импорт своего модуля по шаблону 
#	import asm<код группы>.st<номер по журналу>.main

MENU = [
		["[1904-00] Образец 1904", "asm1904/st00/main.py"],
		["[1905-00] Образец 1905", "asm1905/st00/main.py"],
		
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<код группы>-<номер по журналу>] <Фамилия>", "<путь до модуля>"],
	]

def launcher():
	time.sleep(3)
	os.system("start http://localhost:5000/")

def menu():
	print("------------------------------")
	for i, item in enumerate(MENU):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

try:
	while True:
		try:
			app = MENU[menu()][1]
			threading.Thread(target=launcher).start()
			os.system("python "+app)
		except KeyboardInterrupt:
			pass
except Exception as ex:
	print(ex, "\nbye")
