from flask import Flask, url_for, render_template
import cgi
import cgitb
from strategy.menuItems import ADDITION_MENU

cgitb.enable()
app = Flask(__name__)

if __name__ == '__main__':
    from strategy.main import scrumTeam
else:
    from .strategy.main import scrumTeam


@app.route("/")
def main():
    scrumTeam.load_from_file()
    employees_num = enumerate(scrumTeam.employees)
    return render_template('index.html', menu=ADDITION_MENU, employees=employees_num)


@app.route('/team/add', defaults={'number': None})
@app.route('/team/add/<int:number>', methods=['GET', 'POST'])
def add_student(number):
    form = cgi.FieldStorage()
    text1 = form.getfirst("TEXT_1", "не задано")
    text2 = form.getfirst("TEXT_2", "не задано")

    if number is None:
        return render_template('add.html')
    else:
        templ_name = ['student', 'starosta', 'proforg']
        return render_template('addition.html', number=number)

    # if request.method == 'POST':
    #     data = request.form
    #     myG.add_student(number, data=data, type_context='web')
    #     return render_template("menu.html")


@app.route('/team/edit', defaults={'number': None})
@app.route('/team/edit/<int:number>', methods=['GET', 'POST'])
def change_student(number):
    if request.method == 'POST':
        data = request.form
        myG.change_student(number, data=data)
        return render_template("menu.html")
    if number is None:
        return render_template('edit.html', length=myG.amount_students)
    else:
        return myG.change_student(number, data={'web': number})


@app.route('/team/show')
def print_group():
    page_group = render_template('show_top.html', length=myG.amount_students)
    body = myG.print_group()
    if body is not None:
        page_group += body
    page_group += render_template('show_f.html')
    return page_group


@app.route('/team/remove/<int:number>', methods=['GET', 'POST'])
def remove_student():
    if request.method == 'GET':
        return render_template('remove.html', length=myG.amount_students - 1)
    else:
        if request.form['number']:
            number = int(request.form['number'])
            myG.remove_student(number)
        return render_template('menu.html')


@app.route('/team/magic', defaults={'number': None})
@app.route('/team/magic/<int:number>')
def do_magic(number):
    return render_template('magic.html', length=myG.amount_students) if number is None else myG.do_magic(number)


@app.route('/team/save')
def save_to_file():
    myG.save_to_file()
    return render_template('menu.html')


@app.route('/team/load')
def load_from_file():
    myG.load_from_file()
    return render_template('menu.html')


if __name__ == "__main__":
    app.run(debug=True)
