from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from strategy.main import scrumTeam
from strategy.menuItems import ADDITION_MENU, MENU
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
myG = scrumTeam


def render_header():
    return render_template('boilerplate.html')


class AdditionForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@app.route('/')
def main():
    employees_num = enumerate(scrumTeam.employees)
    return render_header() + render_template('index.html', length=len(scrumTeam.employees), menu=MENU,
                                             employees=employees_num)


@app.route('/add/', defaults={'number': None})
@app.route('/add/<int:number>', methods=['GET', 'POST'])
def add_student(number):
    if number is None:
        return render_header() + render_template('addition.html', menu=ADDITION_MENU)
    if request.method == 'POST':
        data = request.form
        myG.add_student(number, data=data, type_context='web')
        return render_header() + render_template('/')
    else:
        form = AdditionForm()
        return render_header() + render_template('addition.html', form=form, number=number,
                                                 fields=scrumTeam.get_fields(number))


@app.route('/team/edit', defaults={'number': None})
@app.route('/team/edit/<int:number>', methods=['GET', 'POST'])
def change_student(number):
    if request.method == 'POST':
        data = request.form
        myG.change_student(number, data=data)
        return render_template('menu.html')
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


if __name__ == '__main__':
    app.run(debug=True)
