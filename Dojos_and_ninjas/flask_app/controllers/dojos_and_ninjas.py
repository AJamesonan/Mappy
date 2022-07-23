from flask import render_template,redirect,request,session,flash
from flask_app import app

from flask_app.models.dojo_and_ninja import Dojo
from flask_app.models.dojo_and_ninja import Ninja

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos = dojos)

@app.route('/add_dojo', methods = ['POST'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/dojo/<int:dojo_id>')
def ninjas_in_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.get_dojo_by_id(data)
    return render_template('ninjas.html', dojo = dojo)

@app.route('/new_ninja')
def create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos = dojos)


@app.route('/add_ninja', methods = ['POST'])
def add_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/dojos')