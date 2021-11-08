import time
import random
from os import system
print ("Hello and welcome to...")
time.sleep(1)
print ("FIZZ...")
time.sleep(3)
print ("BUZZ!!!!!!!!")
input("Press enter to continue...")
system('clear')
print ("What mode would you like?")
modeselection = input ("""
What mode would you like to use?
a) Show all the numbers in a particular range
b) Enter a number directly.
Type your answer here: """)
if modeselection == "a":
    numrangestart = input ("Select the starting number in your range (e.g.,1)")
    numrangefinish = input ("Select the ending number in your range (e.g),100")
    numrangestartinterpreted = int(numrangestart)
    numrangefinishinterpreted = int(numrangefinish)+1
    for number in range(numrangestartinterpreted,numrangefinishinterpreted):
        if number%3 == 0 and number%5 == 0:
            print ("FizzBuzz")
        elif number%3 == 0:
            print ("Fizz")
        elif number%5 == 0:
            print ("Buzz")
        else:
            print (number)
elif modeselection == "b":
    number = input ("Please enter the number you would like to check: ")
    numinterpreted = int(number)
    if numinterpreted%3 == 0 and numinterpreted%5 == 0:
        print (str(numinterpreted)+" = FizzBuzz")
    elif numinterpreted%3 == 0:
        print (str(numinterpreted)+" = Fizz")
    elif numinterpreted%5 == 0:
        print (str(numinterpreted)+" = Buzz")
    else:
        print ()
