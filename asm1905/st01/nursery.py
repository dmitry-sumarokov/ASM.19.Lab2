import pickle
from cats import Cats, Siamese, British, Lop_eared, Sphinx
from flask import render_template
from flask import request, redirect

class Nursery():
	def __init__(self):
		self._menu_list = [
			["Siamese cat", Siamese],
			["British cat", British],
			["Lop-eared cat", Lop_eared],
			["Sphinx", Sphinx]
			]
		try:
		    self.load_from_file()
		except:
		    self.cats_list = []

	def GetItem(self, id):
		if id < 0:
		    return Behaviour(self._menu_list[-id-1][1]())
		else:
		    return self.cats_list[id]


	def do_special_meow(self,id):
		return self.GetItem(id).special_meow()

	def add_cat(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id)
		item.do_add_the_cat()

		if id <0:
			self.cats_list.append(item)
		return redirect("/")


	def change_cat(self, id):
		return self.GetItem(id).do_edit(id)
		

	def print_cats(self):
		return render_template("index.tpl", items=self.cats_list, numbers = range(len(self.cats_list)))

	def remove_the_cat(self,id):
		self.cats_list.pop(id)
		return redirect("/")

	def clear_cats_list(self):
		self.cats_list.clear()
		return redirect("/")
       
	def save_to_file(self):
		with open('cat_list.p', 'wb') as f:
			pickle.dump(self.cats_list, f)

	def load_from_file(self):
		with open('cat_list.p', 'rb') as f:
			self.cats_list = pickle.load(f)


class Behaviour():

	def __init__(self, cat: Cats):
		self._cat = cat
		self._name = ''
		self._gender = ''
		self._age = 0
		self._colour = ''

	def special_meow(self):
		return render_template("meow.tpl", o=self)



	def do_add_the_cat(self):
		self._name = request.form.get('name')
		self._gender = request.form.get('gender')
		self._age = int(request.form.get('age'))
		self._colour = request.form.get('colour')



	def do_edit(self,id):
		return render_template("form.tpl", o=self,id=id)

