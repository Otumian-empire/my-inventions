"""
Write a program that prompts the user to enter five test scores and then
 prints
the average test score. (Assume that the test scores are decimal numbers.)
"""

firstnumber = secondnumber = thirdnumber = 0
fourthnumber = fifthnumber = sumofnumbers = averageofthenumbers = 0

firstnumber = float(input('Enter the first number: '))
secondnumber = float(input('Enter the second number: '))
thirdnumber = float(input('Enter the third number: '))
fourthnumber = float(input('Enter the fourth number: '))
fifthnumber = float(input('Enter the fifth number: '))

sumofnumbers = firstnumber + secondnumber + thirdnumber + fourthnumber 
sumofnumbers += fifthnumber

averageofthenumbers = sumofnumbers / 5.0

print("The average of the five test scores are:", averageofthenumbers)
