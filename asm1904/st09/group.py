from flask import render_template
from flask import request
import pickle

class Creative():
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

class IOFlaskArtist():
	def ShowForm(self, w):
		return render_template("Fartist.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Artist.tpl", **w.__dict__)

class IOFLaskWriter():
	def ShowForm(self, w):
		return render_template("Fwriter.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Writer.tpl", **w.__dict__)

class IOFlaskPoet():
	def ShowForm(self, w):
		return render_template("Fpoet.tpl", **w.__dict__)
	def Show(self, w):
		return render_template("Poet.tpl", **w.__dict__)

class Artist(Creative):
	IO_behaviour= IOFlaskArtist()

class Writer(Creative):
	IO_behaviour= IOFLaskWriter()

class Poet(Creative):
	IO_behaviour = IOFlaskPoet()

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
				return Artist()
			if f == 1:
				return Writer()
			if f == 2:
				return Poet()
		else:
			return self.items[id]

	def AddItemArtist(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,0)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()

	def AddItemWriter(self):
		id = int(request.form.get('id', 0))
		item = self.GetItem(id,1)
		item.SetData()
		if id <=0:
			self.maxid +=1
			item.id = self.maxid
			self.items[item.id] = item
		return self.ShowGroup()

	def AddItemPoet(self):
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

	def CreativeBehaviour(self, id, f):
		obj = self.GetItem(id, f)
		return obj.ShowForm()
