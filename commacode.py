# Say you have a list value like this: spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns 
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous 
# spam list to the function would return 'apples, bananas, tofu, and cats'
# But your function should be able to work with any list value passed to it.


def comma(*param, sep = ', '):
    """ *param is a list/collection of args
        sep=', ' by default, to change it, do, sep = 'you delimeter here' 
        Example: comma(1,2,3,4,5,6,7, "music","sugar ray", sep="$$$") 
    """
    param = list(param)
    
    if len(param) < 2:
        if len(param) == 0:
            print("The paramter list expected at least 1 argument but 0 found")
            return 
        else:
            print(param[0])
            return 
        print(param)
        return 
    else:
        for i in range(len(param)):
            if param[i] == param[-2]:
                sep = ''
                print(str(param[-2]) + " and ", end='')

            else:
                print(param[i] + sep, end='')
    print()


comma()
comma('foo')
comma('foo', 'boo')
comma('foo', 'boo', 'doo')
comma('foo', 'boo', 'doo', 'zoo')
comma('foo', 'boo', 'doo', 'zoo', 'bobo', 'mississipi')
comma(['michael'], ('michael', 'dunga'), 1, 2.3)
