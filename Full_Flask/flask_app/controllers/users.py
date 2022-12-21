from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask import jsonify

@app.route('/get_data')
def get_data():
    # jsonify will serialize data into JSON format.
    return jsonify(message="Hello World")

from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/create')
def new_form():
    return render_template('new_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = {
        'first_name':request.form['first_name'],
        'last_name' :request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/')

@app.route('/<int:user_id>/delete')
def delete_user(user_id):
    data = {
        'id' : user_id
    }
    User.delete_user(data)
    return redirect ('/')


@app.route('/<int:user_id>/edit')
def user_edit(user_id):
    data = {
        'id': user_id
    }
    user = User.get_user_by_id(data)
    return render_template('edit_users.html', user = user)

@app.route('/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : user_id
    }
    User.update_user(data)
    return redirect('/')



@app.route('/<int:user_id>/<string:first_name>')
def show_user(user_id,first_name):
    data = {
        'id' : user_id,
        'first_name' : first_name
    }
    user = User.get_user(data)
    return render_template('user.html', user = user)
    