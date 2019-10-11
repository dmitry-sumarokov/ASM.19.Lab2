﻿import os, sys, threading, time


MENU = [
		["[1904-00] Образец 1904", "asm1904/st00/main.py"],
		["[1905-00] Образец 1905", "asm1905/st00/main.py"],
		["[1904-01] Абраменкова", "asm1904/st01/main.py"],
		["[1904-19] Танин", "asm1904/st19/main.py"],
		["[1904-05] Орлов", "asm1904/st15/main.py"],
		["[1904-07] Михайлова", "asm1904/st07/main.py"],
		["[1905-11] Ремизова", "asm1905/st11/main.py"],
		["[1905-13] Рыжов", "asm1905/st13/main.py"],
		["[1905-19] Шишкин", "asm1905/st19/main.py"],
                ["[1905-20] Шишкина", "asm1905/st20/main.py"],
		["[1905-21] Бегович", "asm1905/st21/main.py"],

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