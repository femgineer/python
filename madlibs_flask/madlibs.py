from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/madlib/')
def hello(name="Poornima"):
    return render_template('madlib.html', name=name)

@app.route('/final_madlib', methods = ['POST', 'GET']) 
def final_madlib():
    print "inside adjectives"
    adj1 = request.form.get("adj1")
    print "adj1: %s" % adj1
    adj2 = request.form.get("adj2")
    print "adj2: %s" % adj2
    adj3 = request.form.get("adj3")
    print "adj3: %s" % adj3

    verb1 = request.form.get("verb1")
    print "verb1: %s" % verb1
    verb2 = request.form.get("verb2")
    print "verb2: %s" % verb2
    verb3 = request.form.get("verb3")
    print "verb3: %s" % verb3

    noun1 = request.form.get("noun1")
    print "noun1: %s" % noun1
    noun2 = request.form.get("noun2")
    print "noun2: %s" % noun2
    noun3 = request.form.get("noun3")
    print "noun3: %s" % noun3
    noun4 = request.form.get("noun4")
    print "noun4: %s" % noun4

    animal = request.form.get("animal")
    print "animal: %s" % animal
    food = request.form.get("food")
    print "food: %s" % food
    fruit = request.form.get("fruit")
    print "fruit: %s" % fruit
    number = request.form.get("number")
    print "number: %s" % number
    superhero = request.form.get("superhero")
    print "superhero: %s" % superhero
    year = request.form.get("year")
    print "year: %s" % year
    country = request.form.get("country")
    print "country: %s" % country
    dessert = request.form.get("dessert")
    print "dessert: %s" % dessert
    result = request.form

    return render_template('final_madlib.html', result=result) 