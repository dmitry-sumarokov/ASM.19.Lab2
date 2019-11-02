# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template

from shop import Shop

app = Flask(__name__)
s = Shop()


@app.route("/delete", methods=['GET'])
def delete():
    s.remove_from_list(int(request.args.get('id', '')))
    return redirect('/')


@app.route("/clear", methods=['GET'])
def clear_list():
    s.clear_current_list()
    return redirect("/")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "GET":
        id = int(request.args.get('id', ''))
        t = request.args.get('type', '')
        return render_template(
            'form.html', type=t,
            data=s.mobile_list[id], id=id)

    elif request.method == "POST":
        s.edit_list_entry(request.form)
        return redirect('/')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        t = request.args.get('type', '')
        return render_template('form.html', type=t)

    elif request.method == 'POST':
        s.add_list_entry(request.form)
        return redirect('/')


@app.route("/")
def show_list():
    return render_template("list.html", mobile_list=s.mobile_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
