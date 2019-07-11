# author: Otumian Dioratikos
# purpose: I have no idea, Just playing or mocking a phonebook on the terminal
# I was glancing through the book by al-sweigart - automate boring stuff with python
# you may make it better but remember to also make yours as mine
# let me know of how you wish to improves yours, perhaps i could borrow your your
# idea for a second
# I am a programmer and I have a beautiful life.. 
# when you run the code for first time i recommend your first command should be
# info or menu - to display the functionality

namebook = []

def printnamebook(myarg):
    myarg = list(myarg)
    print("%3s %4s" %('No.', 'Names'))
    for i in range(len(myarg)):
        print("%3d %4s" %(i, myarg[i]))

sentinel = True

while sentinel == True:

    name = input("Enter a name or command : ")

    if name == 'exit' or name == 'quit' or name == 'q' or name == 'shutdown':
        print("There are(is) " + str(len(namebook)) + " in your name book")
        
        printnamebook(namebook)

        print("Shutdown, namebook has shutdown!!__!!__!!")
        sentinel = False

    elif name == 'names' or name == 'name' or name == 'namebook':
        printnamebook(namebook)
            
    elif name == 'delete' or name == 'del':
        name = input("Enter name to delete from namebook: ")

        if name in namebook:
            index = namebook.index(name)
            del namebook[index]

        else:
            print(name + " does not exist in namebook")
            printnamebook(namebook)

    elif name == 'info' or name == 'menu':
        print("enter name, to add name to name book!")
        print("enter exit, quit, q or shutdown, to close namebook!!")
        print("enter delete or del, to remove a name from namebook!!!")
        print("enter info or menu, to return the navigation menu!!!!")
        print("enter name, names or namebook, to return all names in namebook!!!!!")

    elif name in namebook:
        print("The name, " + name + " already exist")

    elif len(namebook) == 10:
        print("The fonebok has readed its maximum capcity of 10..")
        print("Delete a name to create space..")

    else:
        namebook.append(name)