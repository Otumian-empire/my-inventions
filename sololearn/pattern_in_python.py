""" Patterns.. I couldn't figure out the last pattern """

star = '*'
limit = eval(input('Enter the range: '))
last_limit = limit - 1
loop_limit = limit * last_limit

print()

# box with filled center
for first_loop_val in range(limit):
    for second_loop_val in range(loop_limit + 1):
        print(star, end='')
    print()

print()

# box with empty center
for first_loop_val in range(limit):
    if first_loop_val == 0 or first_loop_val == (last_limit):
        for second_loop_val in range(loop_limit + 1):
            print(star, end='')
        print()
    else:
        print(star + " " * (loop_limit - 1) + star)

print()

# triangle
for first_loop_val in range(1, limit + 1):
    print(star * first_loop_val)

print()

# triangle reverse
for first_loop_val in range(limit, 0, -1):
    print(star * first_loop_val)

# print()

# fused triangle
init = 1
limit = limit 
step = 1

for first_loop_val in range(limit):
    if first_loop_val % 2 == 0:
        for second_loop_val in range(init, limit, step):
            print(star * second_loop_val)
    else:
        for second_loop_val in range(limit, init, -step):
            print(star * second_loop_val)
