'''This is a program that calculates the area for a shape.'''

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()
#startup the calculator
print "The calculator is startup up..." 
print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
#sleep for one second
sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ").upper()

if option == 'C':
  #do something
  radius = float(raw_input("Enter radius: "))
  area = pi*radius**2
  print "The pie is baking..."
  sleep(1)
  print "The area for your circle is: %.2f. " % (area) + hint
elif option == 'T':
  #do something
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5*(base*height)
  print "Uni Bi Tri..."
  sleep(1)
  print "The area for your triangle is: %.2f. " % (area) + hint
else:
  print "Sorry we can only calculate the area for a Circle of a Triangle.\nGoodbye!"
  
