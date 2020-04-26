# problem: Write a  program to find the maximum number between 3 numbers
# Author: Otumian

# def maxNum(a, b, c):
#     maxNumber = 0
#     if a == b and b == c:
#         return a
#     elif a > b and a > c:
#         maxNumber = a
#     elif b > a and b > c:
#         maxNumber = b
#     else:
#         maxNumber = c

#     return maxNumber


# print(maxNum(1, 1, 3))
# print(maxNum(1.2, 1.4, -3.0))
    
# x = 0
# while x < 5:
#     print(x, "i loop number", x + 1)
#     x += 1



mylist = [1,2,3,4,5,6,7]
lenlist = len(mylist)
counter = 2
while counter < lenlist:
    print(counter, mylist[counter])
    counter += 1