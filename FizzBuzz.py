""" FIzzBuzz implementation in python Otumian 'Dioratikos' Empire"""

# Initializing an empty list
myList = []

# to loop through 1000 ints
for i in range(100,300):
    # storing the 1000 int into the empty list
    myList.append(i)

# looping through the list
for i in range(len(myList)):
    # checking if an int in the list is a multiple of 2 and 3
    if ((myList[i] % 2 == 0) & (myList[i] % 3 == 0)):
        myList[i] = "FizzBuzz";
    # checking if an int in the list is a multiple of 3
    elif (myList[i] % 3 == 0):
        myList[i] = "Buzz";
    # checking if an int in the list is a multiple of 2 
    elif (myList[i] % 2 == 0):
        myList[i] = "Fizz";
    # this else block can be ommited, as such i will comment it out
    # else:
    #     pass

# displaying the list
print(myList)

""" 
    There is another way of implementing this code
    Looping the throught the list and then appending the int that
    meets the coditions stated above
    			OR
    You can use print through out without the code leaving out the list
"""
 
