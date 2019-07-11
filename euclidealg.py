# A python program that implements Euclide's algorithm
# find the greatest common devisor (gcd)
# def euclidalg(p, q): means, define(create) a function 
# (a collection of instructions). p, q are parameters
# if q == 0: return p, means check if q's value is 0
# if so, print p's value and end the program
# else: return euclidalg(q, p % q) means, if q's value is not
# 0, then find the remainder when q divides p
# check if the remainder is 0, if so print q and end the program
# this is done repeatedly
# print("The greatest common divisor is " , euclidalg(20, 0)), means
# when the program ends print this to the screen

def euclidalg(p, q):
    if q == 0:
        return p
    else:
        return euclidalg(q, p % q)
        
print("The greatest common divisor is " , euclidalg(20, 0))

print("The greatest common divisor is " , euclidalg(30, 160))
