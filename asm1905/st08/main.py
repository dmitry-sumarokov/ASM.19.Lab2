from company import Company
from flask import Flask
from flask import g

main = Flask(__name__)

def GetCompany():
        if 'company' not in g:
                g.company = Company()
        return g.company

@main.route("/")
def index():
	return GetCompany().PrintHeader() + GetCompany().ShowCompany() + GetCompany().PrintFooter()

@main.route("/CompanyBehaviour/<int:id>/<int:f>")
def CompanyBehaviour(id, f):
    return GetCompany().PrintHeader() + GetCompany().CompanyBehaviour(id, f) + GetCompany().PrintFooter()

@main.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetCompany().PrintHeader() + GetCompany().ShowForm(id) + GetCompany().PrintFooter()

@main.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetCompany().PrintHeader() + GetCompany().DeleteItem(id) + GetCompany().PrintFooter()

@main.route("/AddEmployer", methods=['POST'])
def AddEmployer():
	return GetCompany().PrintHeader() + GetCompany().AddEmployer() + GetCompany().PrintFooter()

@main.route("/AddManager", methods=['POST'])
def AddManager():
	return GetCompany().PrintHeader() + GetCompany().AddManager() + GetCompany().PrintFooter()

@main.teardown_appcontext
def finish(ctx):
        GetCompany().store()


if __name__ == "__main__":
	main.run(debug=True)
