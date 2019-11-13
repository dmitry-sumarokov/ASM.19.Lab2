from flask import render_template
from flask import request
import pickle

class Worker():
	IO_behaviour = None

	def __init__(self):
		self.id = 0
		self.Fname = ''
		self.Sname = ''
		self.Position = ''

	def SetData(self):
		self.id = request.form.get('id')
		self.Fname = request.form.get('Fname')
		self.Sname = request.form.get('Sname')
		self.Position = request.form.get('Position')

	def ShowForm(self):
		return self.IO_behaviour.ShowForm(self)
		
	def Show(self):
		return self.IO_behaviour.Show(self)

class IOFlaskSeller():
	def ShowForm(self, w):
		return render_template("Fseller.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Seller.tpl", **w.__dict__)

class IOFLaskManager():
	def ShowForm(self, w):
		return render_template("Fmanager.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Manager.tpl", **w.__dict__)
		
class IOFlaskCleaner():
	def ShowForm(self, w):
		return render_template("Fcleaner.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Cleaner.tpl", **w.__dict__)

class Seller(Worker):
	IO_behaviour= IOFlaskSeller()

class Manager(Worker):
	IO_behaviour= IOFLaskManager()

class Cleaner(Worker): 
	IO_behaviour = IOFlaskCleaner() 

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
				return Seller()
			if f == 1:
				return Manager()
			if f == 2:
				return Cleaner()
		else:
			return self.items[id]

	def AddItemSeller(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,0)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()
	
	def AddItemManager(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,1)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()
	
	def AddItemCleaner(self):
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
	
	def WorkerBehaviour(self, id, f):
		obj = self.GetItem(id, f)
		return obj.ShowForm()		 