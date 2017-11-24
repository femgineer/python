from app import app, db
from functools import wraps
from flask import render_template, flash, redirect, session, abort, g
import os
from sqlalchemy.orm import sessionmaker
from flask import request
from flask import Markup
from markupsafe import soft_unicode

app.config.from_object('config')

from app import app
from forms import LoginForm
from models import User

def login_required(f):    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in'):
            return f(*args, **kwargs)
        else:
            flash('Please login to access this page.')
            return login()
    return decorated_function

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login')
def login():    
    return index()  

@app.route('/authenticate', methods = ['POST', 'GET']) 
def authenticate():
     
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])        
    user = User.query.filter_by(username=POST_USERNAME).first()

    if user is None:
        flash('Wrong username!')
    elif user.password == POST_PASSWORD:
        session['logged_in'] = True
        return madlib()
    else:
        flash('Wrong password!')
    return index()    

@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash("You have been logged out.")
    return render_template('logout.html')

@app.route('/new_user')
def new_user():    
    if session.get('logged_in'):
        flash("Please logout of your current user before creating a new one.")                
    return render_template('new_user.html')
    

@app.route('/create_new_user', methods = ['POST', 'GET'])
def create_new_user():    
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])            
    #TODO: later on check that the username is not taken
    if POST_USERNAME != "" and POST_PASSWORD != "":
        user = User(username = POST_USERNAME, password = POST_PASSWORD)
        db.session.add(user)
        db.session.commit()
        session['logged_in'] = True
        return madlib()
    else:
        flash("Please enter a valid username and password.")
        return render_template('new_user.html')    

# functionality below is for the actual madlibs game

@app.route('/madlib/')
@login_required
def madlib():
    return render_template('madlib.html')

def get_story(request):    
    character_name = request.form.get("name")
    adj1 = request.form.get("adj1")    
    adj2 = request.form.get("adj2")    
    adj3 = request.form.get("adj3")    
    verb1 = request.form.get("verb1")    
    verb2 = request.form.get("verb2")    
    verb3 = request.form.get("verb3")
    noun1 = request.form.get("noun1")    
    noun2 = request.form.get("noun2")    
    noun3 = request.form.get("noun3")    
    noun4 = request.form.get("noun4")    
    animal = request.form.get("animal")    
    food = request.form.get("food")    
    fruit = request.form.get("fruit")    
    number = request.form.get("number")    
    superhero = request.form.get("superhero")    
    year = request.form.get("year")    
    country = request.form.get("country")    
    dessert = request.form.get("dessert")    

    story = Markup("This morning I woke up and felt <strong>%s</strong> because <strong>%s</strong> was going to finally <strong>%s</strong> over the big <strong>%s</strong> <strong>%s</strong>. On the other side of the <strong>%s</strong> were many <strong>%ss</strong> protesting to keep <strong>%s</strong> in stores. The crowd began to <strong>%s</strong> to the rhythm of the <strong>%s</strong>, which made all of the <strong>%ss</strong> very <strong>%s</strong>. <strong>%s</strong> tried to <strong>%s</strong> into the sewers and found <strong>%s</strong> rats. Needing help, <strong>%s</strong> quickly called <strong>%s</strong>. <strong>%s</strong> appeared and saved <strong>%s</strong> by flying to <strong>%s</strong> and dropping <strong>%s</strong> into a puddle of <strong>%s</strong>. <strong>%s</strong> then fell asleep and woke up in the year <strong>%s</strong>, in a world where <strong>%ss</strong> ruled the world." % (adj1, character_name, verb1, adj1, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, character_name, verb3, number, character_name, superhero, superhero, character_name, country, character_name, superhero, character_name, year, noun4))
    
    return story
    
@app.route('/final_madlib', methods = ['POST', 'GET']) 
@login_required
def final_madlib():    
    story = get_story(request)
    
    return render_template('final_madlib.html', story=story) 