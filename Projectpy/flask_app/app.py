import os
from flask import render_template,redirect,request,session,flash, Flask 
import re	
from .models.user import User
from .models.place import Place
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "secrets"
bcrypt = Bcrypt(app)
# from flask_app.models.model import Class

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/register')
def registration():
    return render_template('register.html')


@app.route('/register/user', methods=['POST'])
def register():
    dbdata = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(dbdata)
    if user_in_db:
        flash('*email is taken*')
        return redirect ('/')
    # validate user
    if User.validate_user(request.form):
        print('registration passes')
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'user_name': request.form['user_name'],
            'email': request.form['email'],
            'password': pw_hash 
        }
        # Call the save @classmethod on user// saves info in db
        user_id = User.save(data)
        # store user id into session
        user_in_db = User.get_by_email(data)
        session['user_id'] = user_id
        session['user_name'] = user_in_db.user_name
        print(user_id)
        return redirect('/dash')
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
    if not user_in_db:
        flash('*email/password invalid*')
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['user_name'] = user_in_db.user_name
    print(user_in_db.id)
    print(user_in_db)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    return redirect('/dash')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dash')
def user_places():
    if 'user_id' not in session:
        flash('log in to view page')
        return redirect('/')
        
    list_places = Place.get_places()
    travel_time = Place.get_travel_times()
    print('post travel', travel_time)
    return render_template('index.html', places = list_places,travel_time= travel_time)

@app.route('/set/routemap/', methods = ['POST'])
def set_map():
    # locations = Place.get_places()
    data = {
        'start' : request.form['origin'],
        'end' : request.form['destination']
        }
    start_name = data['start']
    end_name = data['end']
    # start = Place.get_place_by_name(start_name)
    # end = Place.get_place_by_name(end_name)
    session['origin']= Place.get_place_id_by_name(start_name)
    session['destination'] = Place.get_place_id_by_name(end_name)
    return redirect('/dash')

@app.route('/location/new')
def new_place():
    if 'user_id' not in session:
        flash('log in to view page')
        return redirect('/')
    return render_template('add_place.html')

@app.route('/add/location', methods = ['POST'])
def create_place():
    if Place.place_is_valid(request.form):
        print('place is valid')
        # user_data = {
        #     'id': session['user_id']
        # }
        # current_place = Place.get_place_by_id(place_data)
        place_data = {
                'name' : request.form['name'],
                'city' : request.form['city'],
                'state': request.form['state'],
                'street_address': request.form['street_address'],
                'zip': request.form['zip'],
                'user_id': session['user_id']
            }
        Place.save_place(place_data)
        return redirect('/dash')
    else:
        print('validation failed')
        flash('validation failed')
        return redirect('/location/new')

