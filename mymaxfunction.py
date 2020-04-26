""" Write a program to find the maximum number in a given set """

def m_max(*args):
    """ Returns the maximum number """
    
    # take the arguments and cast into a list
    # and find the length of the list
    args = list(args)
    cursor_ptr = pointer = maximum_number = counter = 0
    
    maximum_number = args[cursor_ptr]
    cursor_ptr += 1
    pointer = args[cursor_ptr]

    counter = cursor_ptr + 1
    len_of_args = len(args)

    with open("answer.txt", "w+") as fp:
            
        print("args:", args, file=fp)
        print("length of args:", len_of_args, file=fp)
        print("counter:", counter, file=fp)
        print("cursor_ptr:", cursor_ptr, file=fp)
        
        for counter in range(len_of_args - 1):

            if pointer >= maximum_number:
                maximum_number = pointer
            else:
                maximum_number = maximum_number
            
            cursor_ptr += 1
            pointer = args[cursor_ptr]

            print("counter:", counter, file=fp)
        print("cursor_ptr:", cursor_ptr, file=fp)
        
        print("the maximum number is", maximum_number, file=fp)
        print('\n'*2, file=fp)

# m_max(6, 2, 3, 3.4, 6.01)
m_max(2,3,1,-3, 6, 4, -100, -45, 45)