#1. write a program to print even and odd numbers using switch cases
print("\r\n\r\n\tAssignment number 1 \r\n")
print("write a program to print even and odd numbers using switch cases\n")
starting_limit = 1
ending_limit = 100

for i in range(starting_limit, ending_limit):
    if (i % 2 == 0):
        print(i, "is even")
    elif (i % 2 == 1):
        print(i, "is odd")
    else:
        pass


#2. write a programme to print the largest and smallest number and arrange
# user inputer from decreasing order and vise versa
print("\r\n\r\n\tAssignment number 2 \r\n")
print("write a programme to print the largest and smallest number and \
arrange user inputer from decreasing order and vise versa\r\n")

def num_func(number = input("Enter a number: ")):
    number = list(number)
    print("The user entered:", number)

    max_num = max(number)
    print("The maximum number is:", max_num)

    min_num = min(number)
    print("The minimum number is:", min_num)

    number.sort()

    print("This is the number when sorted:", number)

    number.reverse()
    print("This is the number when reversed:", number)

    print("Thank you!!")

# calling the above function
num_func()

# #3. write a program to print a set of prime numbers  from user input in
# range of 1 - 1000000
print("\r\n\r\n\tAssignment number 3 \r\n")
print("write a program to print a set of prime numbers  from user input in \
range of 1 - 1000000\r\n")

# a list that will hold the prime numbers
prime_numbers_list = []

# taking the user
# the least value
lower_limit = int(input("Enter the starting point: "))
while(lower_limit < 2):
    lower_limit = int(input("Enter the starting point greater than 1: "))

# the most value
upper_limit = int(input("Enter the ending point: "))
while(upper_limit < 3):
    upper_limit = int(input("Enter the ending point greater than 3: "))

# looping through the limits
for number in range(lower_limit, upper_limit + 1):
    is_prime = True
    for divisor in range(2, number):
        # checking if its prime
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        # if it is prime, add to the list
        prime_numbers_list.append(number)

print(prime_numbers_list)


#4. write a programe to print your name using punctuation marks
print("\r\n\r\n\tAssignment number 4 \r\n")
print("write a programe to print your name using punctuation marks\r\n")

# My name is Otu
print("$$$$$    $    $   $")
print("$   $  $$$$$  $   $")
print("$   $    $    $   $")
print("$   $    $    $   $")
print("$$$$$    $$$  $$$$$")

#5. write a program that calculates and prints out the sum of all natural
# numbers divisible by 3 or 5, up to a given limit entered by the user. 
print("\r\n\r\n\tAssignment number 5 \r\n")
print("write a program that calculates and prints out the sum of all natural \
numbers divisible by 3 or 5, up to a given limit entered by the user. \r\n")
limit = 1000
sum_of_natural_nums = 0

for i in range(limit):
    if (i % 3 == 0) or (i % 5 == 0):
        sum_of_natural_nums += i
    else:
        pass

print("The sum of all Natural numbers divisible by 3 or 5 in a range of %d \
is %d" % (limit, sum_of_natural_nums))

