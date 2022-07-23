import re
from flask import render_template,redirect,request,session,flash
from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_recipe import Recipe
from flask_app.models.user import User

@app.route('/')
def login_page():
    return render_template('login.html')


#########################login/ registration #########################

@app.route('/register', methods=['POST'])
def register():
    # validate user
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
        print(user_id)
        return redirect('/recipes')
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
    # session['first_name'] = User.get_by_email(data)
    session['user_id'] = user_in_db.id
    print(user_in_db.id)
    print(user_in_db)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    return redirect('/recipes')


@app.route('/')
def logged_in():
    if 'user_id' not in session:
        flash('log in to view page')
        return redirect('/')
    
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

###############user's recipes page######################
@app.route('/recipes')
def user_recipes():
    if 'user_id' not in session:
        flash('log in to view page')
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    recipe_data = {
        'user_id' : session['user_id']
    }

    User.get_user_by_id(data)
    recipes = Recipe.get_recipes_by_user_id(recipe_data)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    return render_template('index.html', recipes = recipes)


###################################

@app.route('/recipe/new')
def new_recipe():
    return render_template('add_recipe.html')

@app.route('/add/recipe', methods = ['POST'])
def create_recipe():
    user_data = {
        'id': session['user_id']
    }
    current_user = User.get_user_by_id(user_data)
    recipe_data = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'under_30': request.form['under_30'],
        'posted_by' : current_user.first_name,
        'user_id': session['user_id']
        }
    Recipe.save_recipe(recipe_data)
    return redirect('/recipes')

@app.route('/edit/recipe')
def edit_recipe():
    
    return render_template()

@app.route('/recipe/<int:id>')
def show_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_recipe_by_id(data)
    return render_template('view_recipe.html', recipe = recipe)
