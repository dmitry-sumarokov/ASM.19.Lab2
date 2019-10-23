# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:11:12 2019

@author: alena
"""




from man import Man
from flask import Flask
from flask import g

main = Flask(__name__)

def GetMan():
        if 'man' not in g:
                g.man = Man()
        return g.man

@main.route("/")
def index():
	return GetMan().PrintHeader() + GetMan().ShowMan() + GetMan().PrintFooter()

@main.route("/ManBehaviour/<int:id>/<int:f>")
def ManBehaviour(id, f): 
    return GetMan().PrintHeader() + GetMan().ManBehaviour(id, f) + GetMan().PrintFooter()

@main.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetMan().PrintHeader() + GetMan().ShowForm(id) + GetMan().PrintFooter()

@main.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetMan().PrintHeader() + GetMan().DeleteItem(id) + GetMan().PrintFooter()

@main.route("/AddItemAnalyst", methods=['POST'])
def AddItemAnalyst():
	return GetMan().PrintHeader() + GetMan().AddItemAnalyst() + GetMan().PrintFooter()

@main.route("/AddItemDeveloper", methods=['POST'])
def AddItemDeveloper():
	return GetMan().PrintHeader() + GetMan().AddItemDeveloper() + GetMan().PrintFooter()

@main.route("/AddItemTester", methods=['POST'])
def AddItemTester():
	return GetMan().PrintHeader() + GetMan().AddItemTester() + GetMan().PrintFooter()

@main.teardown_appcontext
def finish(ctx):
        GetMan().store()

       
if __name__ == "__main__":
	main.run(debug=True)
