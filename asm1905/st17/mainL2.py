from flask import Flask, render_template, request

if __name__ == '__main__':
    from L1_plus.group import Group
else:
    from .L1_plus.group import Group

myG = Group()

app = Flask(__name__)


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/group/add', defaults={'number': None})
@app.route('/group/add/<int:number>', methods=['GET', 'POST'])
def add_student(number):
    if request.method == 'POST':
        data = request.form
        myG.add_student(number, data=data, type_context='web')
        return render_template("menu.html")
    if number is None:
        return render_template('add.html')
    else:
        templ_name = ['student', 'starosta', 'proforg']
        return render_template('common_add.html', number=number) + render_template(f'add_{templ_name[number]}.html')


@app.route('/group/edit', defaults={'number': None})
@app.route('/group/edit/<int:number>', methods=['GET', 'POST'])
def change_student(number):
    if request.method == 'POST':
        data = request.form
        myG.change_student(number, data=data)
        return render_template("menu.html")
    if number is None:
        return render_template('edit.html', length=myG.amount_students)
    else:
        return myG.change_student(number, data={'web': number})


@app.route('/group/show')
def print_group():
    page_group = render_template('show_top.html', length=myG.amount_students)
    body = myG.print_group()
    if body is not None:
        page_group += body
    page_group += render_template('show_f.html')
    return page_group


@app.route('/group/remove', methods=['GET', 'POST'])
def remove_student():
    if request.method == 'GET':
        return render_template('remove.html', length=myG.amount_students - 1)
    else:
        if request.form['number']:
            number = int(request.form['number'])
            myG.remove_student(number)
        return render_template('menu.html')


@app.route('/group/magic', defaults={'number': None})
@app.route('/group/magic/<int:number>')
def do_magic(number):
    return render_template('magic.html', length=myG.amount_students) if number is None else myG.do_magic(number)


@app.route('/group/save')
def save_to_file():
    myG.save_to_file()
    return render_template('menu.html')


@app.route('/group/load')
def load_from_file():
    myG.load_from_file()
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)
