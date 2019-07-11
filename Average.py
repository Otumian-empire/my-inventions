# A program that takes 5 input and returns
# the average of the numbers as  output
# Steps
# prompt the user for five input
# find the sum of the inputs
# divide the sum by 5
# return the result

# The average computed procedurally
sum_of_elements = 0
number_of_elements = 5
for i in range(number_of_elements):
    number = int(input("Enter a number: "))
    sum_of_elements += number

average = sum_of_elements / number_of_elements
print("The average of the five numbers is " + str(average))

# The average computed functionally


def return_average(*elements):
    number_of_element = len(elements)
    sum_of_element = 0
    for x in range(number_of_element):
        sum_of_element += elements[x]

    average_f = sum_of_element / number_of_element
    print("The average of the five numbers is " + str(average_f))

    # print(len(elements))


print("The average computed functionally")

return_average(1, 2, 3, 4, 5)
