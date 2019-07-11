""" 
Write a C++ program that prompts the user to input the elapsed time for
an event in seconds. The program then outputs the elapsed time in hours,
minutes, and seconds. (For example, if the elapsed time is 9630 seconds,
then the output is
2:40:30
.) 
"""

# create a varaible to hold the elasped time
elaspedtime = int(input("Enter elasped time in seconds: "))

# create 3 variables to hold the elasped time in hours, minutes and seconds
hrs = mins = secs = 0

# check if the elasped time is less than 60.. if it is, the it is in seconds
if elaspedtime < 60:
    secs = elaspedtime
    print(hrs, ":", mins, ":" , secs)
else:
    # if the elasped time greater than 60, it is in minute
    # so reduce it by 60 and increase minute by one
    while elaspedtime > 59:
        elaspedtime -= 60
        mins += 1
        # if the minute is greater than 60, it is in hours
        # so reduce it by 60 and increase hours by one
        if mins > 59:
            mins -= 60
            hrs += 1

    secs = elaspedtime
    print(hrs, ":", mins, ":" , secs)


# create a varaible to hold the elasped time
elaspedtime = int(input("Enter elasped time in seconds: "))

# create 3 variables to hold the elasped time in hours, minutes and seconds
hrs = mins = secs = 0

# check if the elasped time is less than 60.. if it is, the it is in seconds
if elaspedtime < 60:
    secs = elaspedtime
    print(hrs, ":", mins, ":" , secs)
else:
    if elaspedtime > 59:
        mins = elaspedtime // 60
        if mins > 60:
            mins %= 60
        hrs = elaspedtime // 3600
        secs = elaspedtime % 60

    print(hrs, ":", mins, ":" , secs)

