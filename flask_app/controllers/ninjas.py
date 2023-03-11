from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

#ninja routes-- create new ninja, edit ninja, view ninjas in a specific dojo, delete ninja and reset back to ninjas in specific dojo
@app.route("/ninja/create/form")
def ninja_form():
    new_ninja = ninja.Ninjas.save_ninja(request.form)
    return render_template("ninjas.html", dojos=dojo.Dojos.get_all_dojos())

@app.route('/create_ninja', methods=['POST'])
def new_ninja():
    ninja.Ninjas.save_ninja(request.form)
    return redirect('/')


@app.route('/ninja/<int:id>')
def show_ninja(id):
    data={
    'id':id
    }
    logged_ninja = ninja.Ninjas.get_one_ninja(data)
    return render_template('show_ninja.html', one_ninja= logged_ninja)

@app.route('/update_ninja', methods=['POST'])
def edit_ninja(): 
    data={
    'id':id
    }
    ninja.Ninjas.update_ninja(request.form)
    print(request.form)
    return redirect(f'/dojo/{request.form["dojo_id"]}')

@app.route('/update_ninja/<int:id>')
def update_ninja(id):
    data={
    'id':id
    }
    return render_template('edit_ninja.html', one_ninja= ninja.Ninjas.get_one_ninja(data))

@app.route("/ninja/delete/<int:id>/<int:dojo_id>")
def delete_ninja(id, dojo_id):
    data={
    'id':id
    }
    ninja.Ninjas.delete_ninja(data)
    return redirect(f'/dojo/{dojo_id}')
