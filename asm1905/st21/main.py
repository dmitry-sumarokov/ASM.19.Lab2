import os

from flask import Flask, render_template, request, redirect
from strategy.employee import Employee
from strategy.menuItems import ADDITION_MENU, MENU
from strategy.scrumTeam import ScrumTeam

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
scrumTeam = ScrumTeam()


def render_header():
    return render_template('boilerplate.html')


def get_form_data(number):
    data = request.form
    data = data.to_dict()
    e = ADDITION_MENU[number]
    employee = Employee(e[1], e[2])
    data['Type'] = employee.get_type()
    return data


@app.route('/')
def main():
    employees_num = enumerate(scrumTeam.employees)
    return _add_boilerplate(
        render_template('index.html', length=len(scrumTeam.employees), menu=MENU, employees=employees_num))


@app.route('/add/', defaults={'number': None})
@app.route('/add/<int:number>', methods=['GET', 'POST'])
def add_student(number):
    if number is None:
        return _add_boilerplate(render_template('addition.html', menu=ADDITION_MENU))

    if request.method == 'POST':
        if not _get_form_fields():
            form = _create_form(number)
            return _add_boilerplate(render_template('addition.html', form=form, number=number, endpoint='add',
                                                    msg='All fields are required!'))
        else:
            data = get_form_data(number)
            scrumTeam.add_employee(data)
            return redirect('/')

    else:
        form = _create_form(number)
        return _add_boilerplate(render_template('addition.html', form=form, number=number, endpoint='add'))


@app.route('/edit/<int:number>', methods=['GET', 'POST'])
def change_student(number):
    employee_data = scrumTeam.employees[number]
    form = _create_form(number, employee_data)

    if request.method == 'POST':
        if not _get_form_fields():
            return _add_boilerplate(
                render_template('addition.html', form=form, number=number, endpoint='edit',
                                msg='All fields are required!'))
        else:
            data = get_form_data(number)
            scrumTeam.edit_employee(data, number)
            return redirect('/')

    elif number is not None:
        return _add_boilerplate(
            render_template('addition.html', form=form, number=number, endpoint='edit'))


@app.route('/remove/<int:number>', methods=['GET', 'POST'])
def remove_student(number):
    if number is not None:
        scrumTeam.remove_employee(number)
        return redirect('/')


@app.route('/export/')
def save_to_file():
    scrumTeam.save_to_file()
    return redirect('/')


@app.route('/load/')
def load_from_file():
    scrumTeam.load_from_file()
    return redirect('/')


def _create_form(number, values=None) -> str:
    form = ''
    fields = scrumTeam.get_fields(number)
    for field in fields:
        if values:
            form += _make_field(field, values.get(field.lower()))
        else:
            form += _make_field(field)
    return form


def _make_field(name, value=None) -> str:
    dt = "<dt>" + name.title() + ":"
    dt_end = "</dt>"
    input_start = '<input name='
    input_end = '> </input>'
    if value:
        temp = ' value=' + str(value) + input_end
    else:
        temp = input_end
    return dt + input_start + name.lower() + temp + dt_end


def _add_boilerplate(template) -> str:
    return render_header() + template


def _get_form_fields() -> list or bool:
    answers = []
    form = request.form
    for i in form.keys():
        if form.get(i) == '':
            return False
        else:
            answers.append(form.get(i))
    return answers


if __name__ == '__main__':
    app.run(debug=True)
