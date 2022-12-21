
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
    session['first_name'] = user_in_db.first_name
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
    list_recipes = Recipe.get_recipes_and_users()
    return render_template('index.html', recipes = list_recipes)


###################################

@app.route('/recipe/new')
def new_recipe():
    return render_template('add_recipe.html')

@app.route('/add/recipe', methods = ['POST'])
def create_recipe():
    if Recipe.recipe_is_valid(request.form):
        print('recipe is valid')
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
    else:
        print('ya blew it')
        flash('validation failed')
        return redirect('/recipe/new')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'first_name' not in session:
        return redirect ('/')
    data = {
        'id':id
    }
    recipe = Recipe.get_recipe_by_id(data)
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/recipe/<int:id>')
def show_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_recipe_by_id(data)
    return render_template('view_recipe.html', recipe = recipe)

@app.route('/update/recipe/<int:id>', methods = ['POST'])
def update_recipe(id):
    if not Recipe.recipe_is_valid(request.form):
        print('recipe is invalid')
        return redirect(f'/edit/recipe/{id}')
    recipe_data = {
        **request.form,
        'id': id,
        'user_id': session['user_id']
    }
    Recipe.update_one(recipe_data)
    return redirect('/recipes')


@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    datas = {
        'id': id
    }
    Recipe.delete_one(datas)
    return redirect('/recipes')