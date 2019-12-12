from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from container import Container

app = Flask(__name__)
c = Container()


@app.route("/", methods=["GET"])
def index():
    c.laod_list()
    return render_template("index.html", tea_list=c._list)


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("form.html", var=request.args["var"])
    elif request.method == "POST":
        c.add_new(request.form)
        return redirect("/")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        id = int(request.args["id"])
        return render_template(
            "form.html", data=c._list[id - 1], id=id)
    elif request.method == "POST":
        c.edit(request.form)
        return redirect("/")


@app.route("/delete", methods=["GET"])
def delete():
    c.delete(request.args["id"])
    return redirect("/")


@app.route("/clear", methods=["GET"])
def clear():
    c.clear()
    return redirect("/")


@app.route("/behaviour", methods=["GET"])
def behaviour():
    beh = c.behaviour(request.args["id"])
    return render_template("behaviour.html", beh=beh)


if __name__ == "__main__":
    app.run()
