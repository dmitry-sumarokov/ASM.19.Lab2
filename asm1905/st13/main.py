from ACS_SC_dep import ACS_SC_dep
from flask import Flask
from flask import g

app = Flask(__name__)


def GetDep():
    if 'dep' not in g:
        g.dep = ACS_SC_dep()
    return g.dep

# @app.route('/')
# def index():
#     return "Hello, World!"

@app.route("/")
def index():
    return GetDep().Head() + GetDep().Dep() + GetDep().Body()

@app.route("/EmpParamsForm/<id>")
def EmpParamsForm(id):
    return GetDep().Head() + GetDep().Alter_Employee(int(id)) + GetDep().Body()


# @app.route("/DeleteItem/<int:id>")
# def DeleteItem(id):
# 	return GetGroup().PrintHeader() + GetGroup().remove_worker(id) + GetGroup().PrintFooter()
#
# @app.route("/ShowMagicForm/<int:id>")
# def ShowMagicForm(id):
# 	return GetGroup().PrintHeader() + GetGroup().do_magic(id) + GetGroup().PrintFooter()
#
# @app.route("/DeleteGroup")
# def DeleteGroup():
# 	return GetGroup().PrintHeader() + GetGroup().clear_worker() + GetGroup().PrintFooter()
#
@app.route("/HireEmployee", methods=['POST'])
def HireEmployee():
    return GetDep().Head() + GetDep().Hire_Employee() + GetDep().Body()
#
#
# @app.teardown_appcontext
# def finish(ctx):
#         GetGroup().save_to_file()

if __name__ == "__main__":
    app.run(debug=True)
# def main():
#     dep = ACS_SC_dep()
#     print('Congratulations!!! You have just become the head of Automated Control Systems Security Center department')
#     print('What do you want to do?')
#     main_menu = (('Hire employee', dep.hire_employee),
#                  ('Alter employee params', dep.alter_employee),
#                  ('Print employees list', dep.print_emp_list),
#                  ('Show special employees abilities', dep.special_action),
#                  ('Fire employee', dep.fire_employee),
#                  ('Save employees list to file', dep.save_to_file),
#                  ('Load employees list from file', dep.load_from_file),
#                  ('Close department (delete all info about employees)', dep.close_dep))
#     # ('Exit department', exit))
#
#     while True:
#         try:
#             print("------------------------------")
#             for i, item in enumerate(main_menu):
#                 print("{0:2}. {1}".format(i, item[0]))
#             print("------------------------------")
#             choice = input()
#             if choice.isdigit():
#                 main_menu[int(choice)][1]()
#             else:
#                 print('Enter a number from main menu!')
#         except Exception as e:
#             print(e, "\n\nEnd of working day")
#             return
