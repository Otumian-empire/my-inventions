# making use of the math class
import math

class QuadraticFunction:
    """ This is a Quadratic Function Class.\n
        f(x) = ax^2 + bx + c, where a, b, c are constants and a != 0 (a is not equal to zero).\n
        Create a new instance of the class and give the constractor, a, b and c from your quadratic function"""
    

    def __init__(self, a, b, c):
        """ a is the co-efficient of x^2, b is the co-efficient of x and c is a constant """
        self.a = a
        self.b = b
        self.c = c

    
    def nature_of_turning_point(self):
        """ A function that returns the type of curve a function is.\n
            If the co-efficient of x^2, a > 0, the functions generates a minimum point as such the function becomes a minimum curve (The function points downwards).\n 
            Also, if the co-efficient of x^2, a < 0, the functions generates a maximum point as such the function becomes a maximum curve (The function points upwards).\n """
        return_msg = "The nature of the turning point:\n\t"
        if self.a > 0:
            return_msg += "The function is a Minimum curve, because the co-efficient of x^2, a " + str(self.a) + " > 0.\n"
        elif self.a < 0:
            return_msg += "The function is a Maximum curve, because the co-efficient of x^2, a " + str(self.a) + " < 0.\n"
        else:
            return_msg += "The function is not a Quadratic Type, because the co-efficient of x^2, a" + str(self.a) + " = 0. This means the function a linear function with no x^2 as a variable.\n"

        return return_msg


    def turning_point(self):
        """ This returns the turning point, tp of the quadratic function. """
        return_msg = "The turning point:\n\t"
        if self.a == 0:
            return_msg += "The function is not a Quadratic Type, because " + str(self.a) + " = 0. This means the function a linear function with no x^2 as a variable and has no turning point.\n"
        else:
            # x and y are the horizontal and vertical components, respectively
            x = (-self.b)  / (2 * self.a)
            y = ((4 * self.a * self.c) - (math.pow(self.b, 2))) / (4 * self.a)
            return_msg += "The turning point of the curve is " + str((x, y)) + "\n"

        return return_msg


    def roots_of_the_function(self):
        """ This returns the solutions of a Quadratic Function, the roots of the function """
        return_msg = "The roots of the equation:\n\t"
        # the discriminat = b^2 - 4ac
        D = (math.pow(self.b, 2)) - (4 * self.a * self.c)
        
        if D > 0:
            return_msg += "The function has two distinct roots.This means, the curve cuts (intersects) the x-axis twice.\n"
        elif D == 0:
            return_msg += "The function has one repeated root.This means, the curve cuts (intersects) the x-axis once.\n"
        else:
            return_msg += "The function has complex roots.This means, the curve doesn't cuts (intersects or tourch) the x-axis twice.\n"

        # this is the first root
        alpha = ((-self.b) + math.sqrt(D)) / (2 * self.a)

        # this is the second root
        beta = ((-self.b) - math.sqrt(D)) / (2 * self.a)

        # the roots are alpha and beta
        roots = (alpha, beta)

        return_msg += "\tThe roots of the function is " + str(roots) + "\n"

        return return_msg



# qdt = QuadraticFunction(3, -4, -2)
# print(qdt.nature_of_turning_point())
# print(qdt.turning_point())
# print(qdt.roots_of_the_function())