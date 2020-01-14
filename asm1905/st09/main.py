from flask import Flask, request, render_template, redirect, url_for

from group import Group

app = Flask(__name__)
app.config['SECRET_KEY'] = '42'

group = Group()


@app.route('/')
def index():
    content = [{'type':group.get_employee_type(x), 'name':x.name, 'sex':x.sex, 'age':x.age, 'special':x.get_magic()} for x in group.employee_list]
    return render_template('index.html', employee_list=content)

@app.route('/clear_group')
def clear_group():
    content = group.clear_group()
    return redirect(url_for('index'))

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee_post():
    if request.method == 'POST':
        print(request.form)
        group.add_employee(request.form['type'],
            name=request.form['name'],
            sex=request.form['sex'],
            age=request.form['age'],
            special=request.form['special'])
        return redirect(url_for('index'))
    else:
        return render_template('add_employee.html')

@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    if request.method == 'POST':
        group.edit_employee(id,
            name=request.form['name'],
            sex=request.form['sex'],
            age=request.form['age'],
            special=request.form['special'])
        return redirect(url_for('index'))
    else:
        emp = group.employee_list[id]
        content = {
            'name': emp.name,
            'sex': emp.sex,
            'age': emp.age,
            'special': emp.get_magic()
        }
        return render_template('edit_employee.html', employee=content)

@app.route('/remove_employee/<int:id>')
def remove_employee(id):
    group.remove_employee(id)
    return redirect(url_for('index'))

@app.route('/load_from_file')
def load_file():
    group.load_from_file()
    return redirect(url_for('index'))

@app.route('/save_to_file')
def save_file():
    group.save_to_file()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
