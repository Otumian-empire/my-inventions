
#filename: ./trials/pat.py
# take input from user
n = int(input('Enter a number: '))

# define a constant
k = 1

# loop through n+1, in reverse other
for row in range(n+1, 1, -1):
    for column in range(row+1, 1, -1):
        print(k, end = '')
        k += 1
    print()

#filename: ./trials/BusinessCast1.py
#! /usr/bin/python3
# verion 1.0
# this is a die game, asks the user for an input and then ckecks what the 
# number is
# there is a reduction in points depending on the input
# As silly and biased as this game (script) may be, it is the base for the 
# version 2
# this version is thought provoking and you can bring on board your ideas

# how points are distributed
# value = points
#     6 = 6
#     5 = - 5
#     4 = 3
#     3 = -2
#     2 = 1
#     1 = -1

points = 0
attempts = 0
events = []
print("This game has started")

while points < 10:
    attempts += 1
    try:
        roll = input("Roll the die: ")
        events.append(roll)
        roll = int(roll)
        if roll == 6:
            points += roll
        elif roll == 5:
            points -= roll
        elif roll == 4:
            points += 3
        elif roll == 3:
            points -= 2
        elif roll == 2:
            points += 1
        elif roll == 1:
            points -= 1
        else:
            points -= 1
            print("What the fuck is " + str(roll))

        print("points: " + str(points))
        # print("events: " + str(events))
    except:
        print("Don't try to be like a computer", "Enter a number")

print("Game over!")
print("Score: ", points)
print("Attempts: ", attempts)
print("Events: ", events)

#filename: ./trials/guipyqt.py
import sys
from PyQt4 import QtGui, QtCore

class guipyqt(QtGui.QWidget):
    def __init__(self):
        super(guipyqt, self).__init__()
        self.initUI()
        self.btnObj()

    def initUI(self):
        self.setGeometry(100, 100, 500, 900)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('huhu.jpg'))
        self.show()
    
    def btnObj(self):
        btn = QtGui.QPushButton('Hello', self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.setToolTip('this is a button that will quit this app')
        btn.resize(btn.sizeHint())
        btn.show()

def main():
    
    app = QtGui.QApplication(sys.argv)#this is an appplication instance
    gui = guipyqt()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

#filename: ./trials/text.py
print("Go is in heaven")

f = open("text.py", 'r')
msg = f.read()
print(msg)
f.close()
print("Go is in heaven")
print("I am a man og God...")
print("Go is in heaven")
print('')
print("I am a man og God...")
print("Go is in heaven")
print('')
print("I am a man og God...")


#filename: ./trials/divisibleby7andnot5program.py
for x in range(10**5):
    if x % 400 == 0:
        print(str(x), end = ', ')

#filename: ./trials/t.py
d1 = {'cool': 2, 'horror': 1, 'terrifying': 2, 'nice movie': 3}

d2 = {'action': 3, 'adventure': 3, 'cool': 1, 'nice movie': 2}

def tags_jaccard_index(d1, d2):
    print('tags--- js')
    set1 = set(d1.keys())
    set2 = set(d2.keys())

    print(set1)
    print(set2)

    common_tags = set.intersection(set1, set2)
    common_tags_count = 0
    all_tags_count = sum(d1.values()) + sum(d2.values())

    for k, v in d1.items():
        if k in common_tags:
            common_tags_count += v

    for k, v in d2.items():
        if k in common_tags:
            common_tags_count += v

    # print(common_tags_count)
    # print(all_tags_count)

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    Tag_S = intersection_cardinality/float(union_cardinality)
    
    # print(Tag_S)
    
    final_tag_similarity = ((common_tags_count / all_tags_count) * 10) * Tag_S
    
    return(final_tag_similarity)
   
print(tags_jaccard_index(d1, d2))


#filename: ./trials/HelloTest.py
import unittest

name = 'Derek'


def hello():
    return 'hello'


def get_name():
    return name


class MyTestCase(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), 'hello')
        

    def test_get_name(self):
        self.assertEqual(get_name(), name)


if __name__ == '__main__':
    unittest.main()


#filename: ./trials/CatTest.py
import unittest
# import Cat


class CatTest (unittest.TestCase):

    @staticmethod
    def testIfTheNumberOfLegsIsAnInter():
        # cat = Cat.Cat("yellow", 2)
        cat = Cat("yellow", 2)
        assert(cat.number_of_legs(), type(cat.number_of_legs()))


if __name__ == "__main__":
    unittest.main()


#filename: ./trials/code.py
# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 400 == 0:
#         if year % 4 == 0:
#             leap = True
#         elif year % 100 == 0:
#             leap = False
    
#     return leap

# for i in range(2001):
#     if is_leap(i) == True:
#         print(str(i), end = ", ")

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 100 == 0 and year % 400== 0 or year % 4 ==0:
#         leap = True
    
#     return leap


# sumn = counter = 0
# # year = int(input("enter year: "))

# for i in range(10**5):
#     sumn += 1
#     if is_leap(i) == True:
#         counter += 1
#         print(i)
# print(str(counter) + "/" + str(sumn) + " tests passed")

# m = [1,2,3,5,6]
# print([m[i] ** i for i in range(1, len(m))], sep='$', end='program Has Ended\n')


#filename: ./trials/testrandomecode.py
# import random, sys

# for i in range(1, random.randint(1, 10) + 1, 2):
#     print(i, "and ((i ** 2) % i) is ", ((i ** 2) % 2))
#     if i > ((i ** 2) % 2):
#         sys.exit(0)

# from random import randint as rnd

# print(rnd(1,100))
from time import time
t1 = time()
print("Hello world")
t2 = time()
print(t2 - t1)



#filename: ./trials/Cat.py
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def number_of_legs(self):
        return self.legs

    def color_of_obj(self):
        return self.color

    def run(self):
        print("My name is Dioratikos and I have " + str(self.number_of_legs()) + " legs")
        print("I am " + self.color_of_obj() + " in complexion")


class Tiger (Cat):
    def __init__(self, is_big, color, legs):
        super().__init__(color, legs)
        self.is_big = is_big

    def tiger_run(self):
        super().run()
        print("I have enormous claws for sprinting")


# felix = Cat("yellow", 6)
#
# felix.run()
#
# tiger = Tiger(True, "green", 1000)
#
# # tiger.run()
#
# tiger.tiger_run()


#filename: ./trials/MiCLI.py
import sys
memo = """MiCLI 2.0.0 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information."""
print(memo)
while True:
    response = input(">>> ")
    if response == "exit":
        sys.exit()
    elif response == "help":
        help_msg = """Welcome to MiCLI 2.0.0's help utility!

If this is your first time using MiCLI, you should definitely check out
the tutorial on the Internet at https://docs.MiCLI.org/2.0.0/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
MiCLI programs and using MiCLI modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam"."""

        print(help_msg)
    else:
        print("This world is not my home, i am just a passing through")

#filename: ./trials/concatdic.py
dicA = {1:5, 2:10}
dicB = {3:15, 5:25}
dicC = {8:40, 9:45, 11:55}
dicD = {15:75, 16:80}
dicE = {19:95, 20:100}

dicResult = {}

# There are two ways, uncomment one
# The one you don't like, remove it
# Also remove all the comments

# method one
# dicResult.update(dicA)
# dicResult.update(dicB)
# dicResult.update(dicC)
# dicResult.update(dicD)
# dicResult.update(dicE)


# method two
# for i in [dicA, dicB, dicC, dicD, dicE]:
#     dicResult.update(i)

print(dicResult)

#filename: ./trials/mm.py


# for a in range(a, num):
#     if a % num == 0:
#         print('not prime')
#         break
# else: # loop not exited via break
#     print('prime')

#filename: ./trials/charcount.py
def count_chars(objval):
    objval = str(objval)
    counter = 0
    for i in objval:
        x = 2
        counter += 1
    print(x)
    return "There are " + str(counter) + " characters"

text = input("Enter a text: ")
print(count_chars(text))

#filename: ./trials/rmvlistdupct.py
# You can do all  this on one line or two or more
names = [
	"Ama", "Cynthia", "Kofi", "Esi", "Ama", "Frank", 
	"Grace", "Frank", "Aseda", "Ama", "Patience"]
names = list(set(names))
print(names)

#filename: ./trials/hello.py
# # f = open('hello.txt', 'r')
# # s = f.read()
# # print("I am a mad programmer", file=f)
# # print(s)
# s = [i.strip() for i in open('hello.txt', 'r').read()]
# print(s)
# f.close()

# lines = [line for line in open('hello.txt', 'r')]
# print(lines)
# print("Opening of file")
# file = open('hello.txt')
# file.close()
# print("file is now closed")
# print()

# print("Now reading from file")
# file = open('hello.txt', 'r+')
# content = [i.strip() for i in file]
# # content = [i.strip() for i in open('hello.txt', 'r+')]
# print(content)
# file.close()
# print("now file is closed after reading")
# print()

# print("Now writing into file")
# file = open('hello.txt', 'w+')
# print('My name  is michael', file=file)
# file.write('I was written using the print function and file param')
# file.close()
# print("now file is closed after writing")
# print()

# print("I am trying to print in a creative manner into the file", file=open('hello.txt', 'w+'))

# print(open('hello.py', 'r').read(), file=open('hello1.txt', 'w+'))

#filename: ./trials/newpat.py

for i in range(7, 11, 1):
    print(i, end='')
    


#filename: ./trials/filehandling.py
print("\t\tWe are to write into files\t\t")

f = open("text.py", "a")
f.write("print(\"Go is in heaven\")\n")
f.write("print('\n')\n")
f.write("print(\"I am a man og God...\")\n")
f.close()

#filename: ./trials/primeNumberTest.py
def isprime(param = 40):
    flag = False
    for i in range(2, param):
        if param % i == 0:
            flag = True

    if flag == True:
        return 'is not prime'
    else:
        return 'is prime'

try:            
    limit = eval(input('enter a number: '))
    for i in range(2, limit):
        print(i, isprime(i))
except Exception as e:
    limit = 50
    for i in range(2, limit):
        print(i, isprime(i))
        

#filename: ./trials/CostOfMilkCalc.py
# A milk carton can hold 3.78 liters of milk. Each morning, a dairy farm ships
# cartons of milk to a local grocery store. The cost of producing one liter of
# milk is $0.38, and the profit of each carton of milk is $0.27. Write a
# program that does the following:
# a. Prompts the user to enter the total amount of milk produced in the
# morning in litres
# b. Outputs the number of milk cartons needed to hold milk (Round your
# answer to the nearest integer.)
# c. Outputs the cost of producing milk
# d. Outputs the profit for producing milk

# A milk carton can hold 3.78 liters of milk.
amount_of_milk_in_carton = 3.78

# The cost of producing one liter of milk is $0.38.
cost_one_liter_of_milk = 0.38

# the profit of each carton of milk is $0.27
profit_one_carton_of_milk = 0.27

# prompting the user to enter amount of milk produced /liters
amount_of_milk_produced = float(input("Enter the amount of milk produced in the morning: "))
# print(amount_of_milk_produced)

# Outputting the number of cartons needed to hold the milk
number_of_cartons_needed = amount_of_milk_produced / amount_of_milk_in_carton
# print(round(number_of_cartons_needed))

# Outputting the cost of producing the milk
# using the amount of milk produced in litres
# cost_of_producing_milk = amount_of_milk_produced * cost_one_liter_of_milk
# print(cost_of_producing_milk)
# using the amount of cartons estimated
cost_of_a_carton = amount_of_milk_in_carton * cost_one_liter_of_milk
print(round(cost_of_a_carton, 2))
cost_of_producing_milk = number_of_cartons_needed * round(cost_of_a_carton, 2)
print(round(cost_of_producing_milk, 2))



#filename: ./trials/readallcontent.py
from glob import glob
from random import randint as rdt, shuffle as shf

def genfilename(targetfile='hellomybabyhellomygirl', fileextension='.txt'):
    """ takes file name as first arg, the file extension as second arg
    if the file name is not give a default is given like wise a .txt 
    as the extention"""
    targetfile = list(targetfile + str(rdt(121, 2123)))
    shf(targetfile)
    targetfile = ''.join(targetfile) + fileextension

    return [targetfile, fileextension]
    

def copyall(targetfile=''.join(genfilename()[0]), 
	fileextension=''.join(genfilename()[1]), mode='w+'):
    """ takes file name as first arg, else it calls the genfilename(), 
    fileextension as second arg, this  refers to the extension of the files 
    you want to read, by default, it takes the extension of the target file
    and if none is given, txt is then given.
    The 3rd arg is mode, mode (r+, w+, a+) in which you want 
    to open the target file. w+ or a+ is ok. by default, w+. """
    myfile = open(str(targetfile), mode)

    filenames = glob('./trials/*' + str(fileextension))

    for i in filenames:
        filecontent = open(i, 'r').read()
        print('\n#filename: ' + str(i) , filecontent, sep='\n', file=myfile)

    myfile.close()

    return "Content copied successfully :- " + str(targetfile)


targetfile, mode = ''.join(genfilename('copyingcontent')[0]), 'w+'
print(copyall(targetfile))
print(copyall('sololearn.py', '.py'))
print(copyall())

# This is the second version
# from glob import glob

# def copyall(filepath='newcopyallfile.txt', fileextension='.py' , filemode='w+'):
#     """ filepath: this is the directed file, by default, 'newcopyallfile.txt'
#     fileextension: this is the file extension and by default is .txt
#     filemode: this is the file mode(a+, w+, r+)"""
#     for i in glob('*'+ fileextension):
#         print("#file name: " + str(i), open(i, 'r').read(), sep='\n',
# file=open(filepath, filemode))
    
#     return 'Copied: True' + ' into File: ' + filepath

# print(copyall())

#filename: ./trials/IpOt.py
#!python3
#get input to output

#get input
#while input != EOF
#print output

c = input(">>> ")
while (c != 'quit'):
    print(c)
    c = input(">>> ")

#filename: ./trials/patterns.py
""" Patterns.. I couldn't figure out the last pattern """

star = '*'
limit = eval(input('Enter the range: '))
last_limit = limit - 1
loop_limit = limit * last_limit

print()

# box with filled center
for first_loop_val in range(limit):
    for second_loop_val in range(loop_limit + 1):
        print(star, end='')
    print()

print()

# box with empty center
for first_loop_val in range(limit):
    if first_loop_val == 0 or first_loop_val == (last_limit):
        for second_loop_val in range(loop_limit + 1):
            print(star, end='')
        print()
    else:
        print(star + " " * (loop_limit - 1) + star)

print()

# triangle
for first_loop_val in range(1, limit + 1):
    print(star * first_loop_val)

print()

# triangle reverse
for first_loop_val in range(limit, 0, -1):
    print(star * first_loop_val)

# print()

# fused triangle
init = 1
limit = limit 
step = 1

for first_loop_val in range(limit):
    if first_loop_val % 2 == 0:
        for second_loop_val in range(init, limit, step):
            print(star * second_loop_val)
    else:
        for second_loop_val in range(limit, init, -step):
            print(star * second_loop_val)

#filename: ./trials/pat2.py
n = int(input("enter a number: "))
for row in range(n, 0, -1):
    print(row)
    x = (row * (row + 1)) / 2
    print(x)
    for column in range(int(x)-row+1, int(x)+1):
        print(column, end='')
    print()

#filename: ./trials/BusinessCast2.py
#! /usr/bin/python3
# version 2.0
# this is a die game, asks the user for an input and then 
# checks if it is equal to a particular number
# there is a reduction in dollar depending on the input
# As silly and biased as this game (script) may be, it is the base for 
# the version 3
# this version is thought provoking and you can bring on board your ideas

# how points are distributed
# value = points
#     6 = 600
#     5 = - 500
#     4 = 300
#     3 = -200
#     2 = 100
#     1 = -100

from random import randint as rand
# user
"""
userAcount: this will save the amount that the user has
userGamePlayAccount: this is the amount the user brings to board
userInterest: this should return the loo/profit
"""


def playeraccount(name, occupation, accountnumber):
    print("Account name: " + str(name))
    print("Account number: " + str(accountnumber))
    print("Works at: " + str(occupation))
    print("Amount in account: $" + str(500))


def cpuguess():
    return rand(1, 7)


playeraccount("michael Dioratikos", "Computer scientist", 123456)
""" get a list of occupation """
occupations = []
# computer
# betting (either with computer or just play)
# counting of games played, user cash, computer cash, bet
# conditions: if user cash is less 50, user can't bet
# ...: if user cash is greater than 100000, bet is raised to 500 per game
# user pays a tax of 2% of cash if the cash ever exceeds 10000
# user should quit the game if he press quit or close or q or 0000
# borrow;: user can borrow
# usrDollars = 500

# bet = 50
# attempts = 0
# events = []
# print("This game has started!!!")

# while (attempts < 3):
#     try:
#         print("Bets are in $50, do you wanna bet? You have $" + str(usrDollars) + " in your account  $$$")
#         usrBet = int(input("How much do ya wanna bet: "))
#         if ((usrBet >= bet) and (usrBet % 50 == 0)):
#             usrDollars -= usrBet
#         elif (usrBet == 0):
#             print(usrDollars, usrBet)
#         else:
#             print('You can bet on 0 or a multiple of 50')

#         print(usrDollars, usrBet)
#         attempts += 1
        
#         roll = input("Roll the die: ")
#         events.append(roll)
#         roll = int(roll)
#         if (roll == 6):
#             usrDollars += roll
#         elif (roll == 5):
#             usrDollars -= roll
#         elif (roll == 4):
#             usrDollars += 3
#         elif (roll == 3):
#             usrDollars -= 2
#         elif (roll == 2):
#             usrDollars += 1
#         elif (roll == 1):
#             usrDollars -= 1
#         else:
#             usrDollars -= 1
#             print("What the fuck is " + str(roll))

#         print("points: " + str(points) )
#         # print("events: " + str(events))
#     except:
#         print("Don't try to be like a computer", "Enter a number")

# print("Game over!")
# print("Score: ", usrDollars)
# print("Attempts: ", attempts)
# print("Events: ", events)


#filename: ./trials/matrix.py
def key_mat():
    min_val = 0
    max_val = 5
    key = []
    for a in range(min_val, max_val + 1, 1):
        for b in range(min_val, max_val + 1, 1):
            for c in range(min_val, max_val + 1, 1):
                for d in range(min_val, max_val + 1, 1):
                    key = [a, b, c, d]
                    det = (key[0] * key[3]) - (key[1] * key[3])
                    if (det % 2 != 0) and (det % 13 != 0):
                        print("The matrix, ", key, "is suitable and has a \
determinant of", det)

key_mat()

