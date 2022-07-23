import re
from flask import render_template,redirect,request,session,flash
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User

@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if User.validate_user(request.form):
        print('registration passes')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash 
        }
        # Call the save @classmethod on User// saves info in db
        user_id = User.save(data)
        # store user id into session
        session['user_id'] = user_id
        return redirect('/dashboard')
    else:
        print('validation failed')
        flash('validation failed')
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    # if len(user_in_db) != 1:
    #     flash('No accounts with this email')
        # return redirect('/')
    if not user_in_db:
        flash('*email/password invalid*')
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def logged_in():
    if 'user_id' not in session:
        flash('log in to view page')
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
