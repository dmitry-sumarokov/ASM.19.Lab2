from abc import ABC, abstractmethod
import pickle
from enum import Enum

from Basic import Basic
from Student import Student
from Headman import Headman
from Container import Container

from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class ChooseTypeForm(FlaskForm):
    type = SelectField('type', choices=[('Студент', 'Студент'), ('Староста', 'Староста')])
    submit = SubmitField('Ok')

class ChooseIdForm(FlaskForm):
    ids = SelectField('ids')
    submit = SubmitField('Ok')

class ElementForm(FlaskForm):
    fio = StringField('fio', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    connect = StringField('connect')
    submit = SubmitField('Ok')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

type = "None"
idx = 0
const_url = "http://127.0.0.1:5000/"
container = Container()

def add_in_container(type_el, fio, age, connect):
    if type_el == "Студент":
        el = Student(fio, age, connect)
    elif type_el == "Староста":
        el = Headman(fio, age, connect)
    container.add_element(el)

@app.route('/load_from_file')
def load_from_file():
    global container
    global const_url
    container.read_data("data.pickle")
    return redirect(const_url + "info")

@app.route('/save_in_file')
def save_in_file():
    global container
    global const_url
    container.write_data("data.pickle")
    return redirect(const_url + "info")

@app.route('/clear_container')
def clear_container():
    global container
    container.clear()
    return redirect(const_url + "info")

@app.route('/')
@app.route('/index')
@app.route('/info')
def info():
    global container
    elements = container.my_list
    return render_template('print_info.html', elements = elements)

@app.route('/add', methods=['GET', 'POST'])
def add():
    global type
    form_add = ElementForm()
    form_choose = ChooseTypeForm()
    if form_add.validate_on_submit():
        add_in_container(type, form_add.fio.data, form_add.age.data, form_add.connect.data)
        return redirect(const_url + "info")
    if form_choose.validate_on_submit():
        if form_choose.type.data == "Студент":
            type = "Студент"
            return render_template('add_element_student.html', form=form_add)
        elif form_choose.type.data == "Староста":
            type = "Староста"
            return render_template('add_element_headman.html', form=form_add)
    return render_template('choose_type.html', form=form_choose)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    global container
    global idx
    global const_url
    form_edit = ElementForm()
    if form_edit.validate_on_submit():
        container.my_list[idx].fio = form_edit.fio.data
        container.my_list[idx].age = form_edit.age.data
        if container.my_list[idx].type == "Студент":
            container.my_list[idx].email = form_edit.connect.data
        elif container.my_list[idx].type == "Староста":
            container.my_list[idx].tel_number = form_edit.connect.data
        return redirect(const_url + "info")
    ids = request.args.get("id")
    idx = container.find_index(ids)
    el = container.my_list[idx]
    if el.type == "Студент":
        return render_template('edit_element_student.html', form=form_edit, el=el)
    elif el.type == "Староста":
        return render_template('edit_element_headman.html', form=form_edit, el=el)

if __name__ == "__main__":
	app.run(debug=True)
