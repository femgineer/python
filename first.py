'''This is a fun madlibs program that lets users input words into a story 
''' 

def get_adjectives():
  adjectives = []
  index = 0

  '''while loop that prompts user to enter 3 adjectives for the story''' 
  while index < 3:
    adjective = raw_input("Enter an adjective: ")
    adjectives.append(adjective)
    index = index + 1
  return adjectives

def get_verbs():    
  verbs = []
  index = 0
  '''while loop that prompts the user to enter 3 verbs for the story'''
  while index < 3:
    verb = raw_input("Enter a verb: ")
    verbs.append(verb)
    index = index + 1
  return verbs

def get_nouns():    
  nouns = []
  index = 0
  '''while loop that prompts the user to enter 3 nouns for the story'''
  while index < 4:
    noun = raw_input("Enter a noun: ")
    nouns.append(noun)
    index = index + 1
  return nouns

def get_weird_items():
  weird_items = {'animal':"", 'food':"", 'fruit':"", 'number':"", 'superhero name':"", 'country':"", 'dessert':"", 'year':""}  

  for key in weird_items:
    value = raw_input("Enter a the name of a %s: " % key )
    weird_items[key] = value
  return weird_items

print "Welcome to Mab Libs!"
character_name = raw_input("Enter a character's name: ")
adjectives = get_adjectives()
verbs = get_verbs()
nouns = get_nouns()
weird_items = get_weird_items()

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

print (STORY % (adjectives[0], character_name, verbs[0], adjectives[1], nouns[0], nouns[1], weird_items["animal"], weird_items["food"], verbs[1], nouns[2], weird_items["fruit"], adjectives[2], character_name, verbs[2], weird_items["number"], character_name, weird_items["superhero name"], weird_items["superhero name"], character_name, weird_items["country"], character_name, weird_items["superhero name"], character_name, weird_items["year"], nouns[3]))