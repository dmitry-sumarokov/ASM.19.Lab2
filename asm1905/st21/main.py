import os

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from strategy.menuItems import ADDITION_MENU, MENU
from strategy.scrumTeam import ScrumTeam
from wtforms import StringField

SECRET_KEY = os.urandom(32)
csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)
scrumTeam = ScrumTeam()


def render_header():
    return render_template('boilerplate.html')


class AdditionForm(FlaskForm):
    pass


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
        form = AdditionForm()
        if form.validate_on_submit():
            data = request.form
            scrumTeam.add_employee(data.to_dict())
            return redirect('/')
        return redirect('/add/')

    else:
        fields = scrumTeam.get_fields(number)
        for field in fields:
            setattr(AdditionForm, field, StringField())
        form = AdditionForm()
        for field in fields:
            delattr(AdditionForm, field)
        return render_header() + render_template('addition.html', form=form, number=number,
                                                 fields=fields)


@app.route('/edit/<int:number>', methods=['GET', 'POST'])
def change_student(number):
    if request.method == 'POST':
        form = AdditionForm()
        if form.validate_on_submit():
            scrumTeam.edit_employee(number)
            return redirect('/')
        return redirect('/add/')

    else:
        return scrumTeam.change_student(number, data={'web': number})


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


if __name__ == '__main__':
    app.run(debug=True)
