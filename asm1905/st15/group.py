from flask import render_template
from flask import request
import pickle

class Workman():
	IO_behaviour = None

	def __init__(self):
		self.id = 0
		self.Name = ''
		self.Surname = ''
		self.Function = ''

	def SetData(self):
		self.id = request.form.get('id')
		self.Name = request.form.get('Name')
		self.Surname = request.form.get('Surname')
		self.Function = request.form.get('Function')

	def ShowForm(self):
		return self.IO_behaviour.ShowForm(self)
		
	def Show(self):
		return self.IO_behaviour.Show(self)

class IOFlaskMechanic():
	def ShowForm(self, w):
		return render_template("Fmechanic.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Mechanic.tpl", **w.__dict__)

class IOFLaskMainEngineer():
	def ShowForm(self, w):
		return render_template("Fmainengineer.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("MainEngineer.tpl", **w.__dict__)
		
class IOFlaskSecurity():
	def ShowForm(self, w):
		return render_template("Fsecurity.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Security.tpl", **w.__dict__)

class Mechanic(Workman):
	IO_behaviour= IOFlaskMechanic()

class MainEngineer(Workman):
	IO_behaviour= IOFLaskMainEngineer()

class Security(Workman): 
	IO_behaviour = IOFlaskSecurity() 

class group:
		
	IO_behaviour = None
	
	def __init__(self):
		try:
			self.load()
		except:
			self.items = {}
			self.maxid = 0
		
	def GetItem(self, id, f):
		if id <= 0:
			if f == 0:
				return Mechanic()
			if f == 1:
				return MainEngineer()
			if f == 2:
				return Security()
		else:
			return self.items[id]

	def AddItemMechanic(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,0)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()
	
	def AddItemMainEngineer(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,1)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()
	
	def AddItemSecurity(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,2)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()
	
	def PrintHeader(self):
		return render_template("header.tpl")

	def PrintFooter(self):
		return render_template("footer.tpl")

	def DeleteItem(self, id):
		del(self.items[id])
		return self.ShowGroup()	 

	def load(self):
		with open('group.db', 'rb') as f:
			(self.maxid, self.items) = pickle.load(f)

	def store(self):
		with open('group.db', 'wb') as f:
			pickle.dump((self.maxid, self.items), f)
	
	def ShowGroup(self):
		r = ""
		for (key, item) in self.items.items():
			r += item.Show()
		r += render_template("add.tpl")
		return r
	
	def WorkmanBehaviour(self, id, f):
		obj = self.GetItem(id, f)
		return obj.ShowForm()		 