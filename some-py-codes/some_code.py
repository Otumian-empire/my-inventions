print("Hello world")



def square(i):
    return i*i


def cube(i):
    return square(i) * i


def display(func, arg):
    ''' takes a function and an argument which is passed to the function'''
    print(arg, func(arg))


def dloop(func, start=0, end=10, step=1):
    for i in range(start, end, step):
        display(func, i)
        
#dloop(cube, start=1, end=20, step=2)

    
#for i in range(1, 10, 2):
#    print(i, i*i)

def floop(body, start, end, step):
    print("this is the floop")
    
    func = body['func']
    arg = body['arg']
    
    for i in range(start, end, step):
        display(func, arg)
    
    
body = {
    'func': square,
    'arg': 3
}

#floop(body, 0, 10, 1)
dloop(body['func'], 0, 10, 1)
    
print("end")   

