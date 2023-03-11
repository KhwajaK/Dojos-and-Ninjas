from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojos 

@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def home():
    dojos=Dojos.get_all_dojos()
    return render_template("dojos.html", dojos=dojos)

@app.route('/add/dojo', methods=["POST"])
def add_dojo():
    Dojos.save_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def view_dojo(id):
    dojo_dict={
    "id":id
    }
    logged_dojo = Dojos.dojo_with_ninjas(dojo_dict)
    return render_template("show_dojo.html", one_dojo = logged_dojo)