from flask import Flask
from flask import render_template
from flask import request
from flask import Markup
from markupsafe import soft_unicode

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/madlib/')
def hello(name="Poornima"):
    return render_template('madlib.html', name=name)

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
def final_madlib():    
    story = get_story(request)
    
    return render_template('final_madlib.html', story=story) 