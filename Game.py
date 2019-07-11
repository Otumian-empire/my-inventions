import random
""" 
Otumian
This is a simple test based console gambling game.
It has not yet met its target as i thought for it.
I just started jotting the general game proccss down as 
i was reading on how the ATM works and also to use a 
flowchart to explain how a merchant transacts business
electronically using visa cards, master cards, etc (I am 
refering to the cards, e-payment)

My jottings:
* Give the self a name and an initial cash (default, $1000)
* Ask the user for his name later in the game, when user is 
making more money
* Randomly generate a number in a range and prompt self to
guess the number
* if self guess is right, double bet and to cash
* else, double and subtract
* bet are in folds of $100

That's it.. Thanks


"""
class Game:

    def __init__(self, cash, username, bet=0):
        self.cash = cash
        self.username = username
        self.bet = bet

    # this function is to return the selfs detail
    def info(self):
        strinfo  = "hello " + self.username + ", you have "
        strinfo += "$" + str(self.cash) + " is your asset.."
        strinfo += "and you've place a bet of $" + str(self.bet) + ".. Good luck"
        return strinfo

    # this is to change the selfs name amids gaming
    def changeselfname(self, newname):
        self.username = newname

    # this function makes sure that the bet is in a fold of 100
    # it also takes the bet from the self
    def wager(self, bet):

        if int(bet) % 100 == 0 and int(bet) != 0:
            if int(bet) < self.cash + 1:
                self.bet = bet
                self.cash -= self.bet
            else:
                print("You only have $" + str(self.cash) + " in your asset..")
                
                if self.cash > 100:
                    self.bet = 100
                    print("For the love of the game, by default your bet is $" + str(self.bet))
                    
        else:
            # i set your bet to 0 as the user didn't specify or chose
            # a bet other than a multiple of 100
            print("Your wager is as tinny as your broke bank..")
            print("Let's just have some fun and call it a day..")
            self.bet = 0

    # This is like the main function.. Just call this function
    def startgame(self):
        # print user info
        print(self.info())
        
        endgame = "yes".lower()
        while(endgame != "no".lower()):

            # try and catch is to catch non numberic input
            try:
                # set a bet
                mybet = int(input("place your bet in a fold of hundreds: "))
                self.wager(mybet)

                # print play info
                print(self.info())

                # checking if bet is greater than half of user player cash
                if self.bet >= 0.5 * self.cash:
                    print("You are man who admires risk..")
                
                # this is where the random numbers are generated
                # you can alter this to suite your needa
                cpunumber = random.randint(0, 2)
                guess = int(input(self.username + " ..be smart and pick your lucky number: "))

                if cpunumber == guess:
                    self.bet *= 3
                    self.cash += self.bet

                    # print user info
                    print(self.info())
                    print(self.username + ", you won thing time.. your cash is : " + str(self.cash))
                else:
                    self.bet = 0
                    # print user info
                    print("you loss..")
                    print(self.info())

                if self.cash < 100:
                    print("Man you have no cash.. You better walk away.. else i'd mob the dirty floor with your damn broke face..")

                    endgame = "no"
                    # print user info
                    print(self.info())
                else:
                    endgame = input("Do you want to keep playing? ").lower()

            except ValueError as e:
                print("Dikward.. i bet your broke fat beefy ass you are a cash crop.. start with a hundred and I will double it in addition..")

        print(self.info())

# create an object of the Game class and call the start method
user = Game(1000, "f3erQ6$_")
user.startgame()