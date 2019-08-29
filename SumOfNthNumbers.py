# Recursive approach
def sum_nth_numbers(number, total = 0):
    if (number > 0):
        total = sum_nth_numbers(number - 1, number + total)
        return total
    else:
        return total
    

# Iterative approach
def sum_nth_numbers1(number, total = 0):
    if (number == 0):
        return total
    else:
        # while(number > 0):
        for i in range(number):
            total += number
            number -= 1
        return total


testing1 = []
for i in range(100):
    result = sum_nth_numbers(i)
    testing1.append(result)

testing2 = []
for i in range(10):
    result = sum_nth_numbers1(i)
    testing2.append(result)    

testing3 = []
for i in range(10):
    result = sum_nth_numbers1(i, 1)
    testing3.append(result)    


print(testing1)
print(len(testing1))
print(testing2)
print(testing3)

