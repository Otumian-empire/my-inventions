def switch(n, *args):

    args = list(args)

    if type(n) != str:
        n = str(n).lower()
        
    for i in args:
        if i.lower() == n:
            return "case", args.index(i), i
    else:
        return "default", None, None


name = input("Enter your name: ")
print(switch(name, "Michael", "Kwame"))
def when(param):
    it = iter()


# i just thought to loop throught rather
