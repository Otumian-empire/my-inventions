filename = 'numberfile.txt'
mode = 'r'

sumofnums = 0

# with open(filename, mode) as fp:
#     for num in fp:
#         sumofnums += int(num)

#     print("Sum = ", sumofnums)

fp = open(filename, mode)
# nums  = fp.read()
# print(nums)

for num in fp:

    sumofnums += int(num)

print("Sum =", sumofnums)
fp.close()
