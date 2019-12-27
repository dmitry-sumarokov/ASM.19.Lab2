import os, sys, threading, time


MENU = [
		["[1904-00] Образец 1904", "asm1904/st00/main.py"],
		["[1905-00] Образец 1905", "asm1905/st00/main.py"],
		["[1904-01] Абраменкова", "asm1904/st01/main.py"],
		["[1904-02] Бернштейн", "asm1904/st02/main2.py"],
        ["[1904-03] Быкова", "asm1904/st03/app.py"],
		["[1904-05] Дмитраков","asm1904/st05/main.py"],
		["[1904-07] Михайлова", "asm1904/st07/main.py"],
		["[1904-14] Новикова", "asm1904/st14/main.py"],
		["[1904-05] Орлов", "asm1904/st15/main.py"],
		["[1904-16] Садыкова", "asm1904/st16/main.py"],
		["[1904-17] Синицына", "asm1904/st17/main.py"],
		["[1904-19] Танин", "asm1904/st19/main.py"],
		["[1905-01] Абдуллина","asm1905/st01/main.py"],
		["[1904-06] Дремезов","asm1904/st06/main.py"],
		["[1904-08] Ильина","asm1904/st08/main.py"],
		["[1905-03] Кокухин","asm1905/st03/main.py"],
		["[1905-02] Вотинцев", "asm1905/st02/main.py"],
		["[1905-05] Коробка", "asm1905/st05/main.py"],
		["[1905-08] Никандров","asm1905/st08/main.py"],
		["[1905-10] Погонина", "asm1905/st10/main.py"],
		["[1905-11] Ремизова", "asm1905/st11/main.py"],
		["[1905-13] Рыжов", "asm1905/st13/main.py"],
		['[1905-17] Суфьянов', 'asm1905/st17/mainL2.py'],
		["[1905-13] Тарасов", "asm1905/st18/main.py"],
		["[1905-19] Шишкин", "asm1905/st19/main.py"],
       	["[1905-20] Шишкина", "asm1905/st20/main.py"],
		["[1905-21] Бегович", "asm1905/st21/main.py"],
        ["[1905-05] Коробка", "asm1905/st05/main.py"],
		["[1905-10] Погонина", "asm1905/st10/main.py"],
        ["[1905-01] Абдуллина","asm1905/st01/main.py"],
		["[1905-08] Никандров","asm1905/st08/main.py"],
		["[1904-05] Дмитраков","asm1904/st05/main.py"],
		["[1904-12] Кривов","asm1904/st12/main.py"],
		["[1905-04] Колодин","asm1905/st04/main.py"],
		["[1905-02] Вотинцев", "asm1905/st02/main.py"],
 		["[1905-12] Ручкина", "asm1905/st12/main.py"],
 		["[1905-15] Синявский", "asm1905/st15/main.py"],
		["[1904-04] Гасанов", "asm1904/st04/main.py"],
 		["[1904-09] Камшилов", "asm1904/st09/main.py"],

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
			if os.system("python3 "+app):
				os.system("python "+app)
		except KeyboardInterrupt:
			pass
except Exception as ex:
	print(ex, "\nbye")
