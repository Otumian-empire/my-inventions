# temperature conversion program
# C = (F - 32) * 5/9
# This program takes an input from the user
# It then converts the value to a real(a decimal)
# But before that, It takes precaution to check if the
# the value entered by the user is numerical
# if the value is not numerical, it prompts the user for
# another value

loop = True
while loop:
    try:
        fahrenheit = float(input("Enter the temp in fahrenheit: "))
        celcius = (fahrenheit - 32) * 5/9
        print("The temperature of %.2f deg celcius is %.2f degree fahrenheit" %(fahrenheit, celcius))
        loop = False
    except ValueError as e:
        print("Please enter a numerical value for fahrenheit..", e)
        
    

    