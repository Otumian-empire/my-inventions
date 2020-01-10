import random

# author: Otumian empire
# description: This is a simple text based console gambling game.
#	 It has not yet met its target as i thought for it.
#	 I just started jotting the general game proccss down as
#	 i was reading on how the ATM works and also to use a
#	 flowchart to explain how a merchant transacts business
#	 electronically using visa cards, master cards, etc (I am
#	 refering to the cards, e-payment)

# My jottings:
#	 * Give the user a name and an initial cash (default, $1000)
#	 * Ask the user for his name later in the game, when user is
#	 making more money
#	 * Randomly generate a number in a range and prompt self to
#	 guess the number
#	 * if user guess is right, double bet and add to cash
#	 * else, double and subtract from cash
#	 * bet are in folds of $100

# That's it.. Thanks


class Game:

    def __init__(self, username, cash=1000, bet=0):
        self.username = username
        self.cash = cash
        self.bet = bet

        # returns user details
    def game_info(self):
        strinfo = f"you have ${self.cash} is your asset.. "
        strinfo += f"and you've place a bet of ${self.bet}"
        strinfo += f".. Good luck"

        return strinfo

    # returns game details
    def player_info(self):
        strinfo = f"hello {self.username}, you have "
        strinfo += f"${self.cash} is your asset.."

        return strinfo

    # change the users name amids gaming
    def changeselfname(self, newname):
        self.username = newname

    # makes sure that the bet is in a fold of 100
    # before allowing bet
    def wager(self, bet):

        try:
            if bet != 0 and bet % 100 == 0:
                if int(bet) < self.cash + 1:
                    self.bet = int(bet)
                    self.cash -= self.bet
                else:
                    print(f"You only have ${self.cash} in your asset..")

                    if self.cash > 100:
                        self.bet = 100
                        print(
                            f"For the love of the game, by default your bet is ${self.bet}")

            else:
                # set bet to 0 since the user didn't chose
                # a bet other than a multiple of 100
                print("Your wager is as tinny as your broke bank..")
                print("Let's just have some fun and call it a day..")
                self.bet = 0

        except ValueError as e:
            print(f"You have to use something quite monery..\n{e}")
            # set a bet again
            mybet = int(
                input("place your bet in a fold of hundreds [100, 200, 300, ...]: "))
            self.wager(mybet)

    # the main function.. Just call this function

    def startgame(self):
        # print user info
        print(self.player_info())

        endgame = "yes".lower()
        while(endgame != "no".lower()):

            # catch non numberic inputs
            try:
                # set a bet
                mybet = int(
                    input("place your bet in a fold of hundreds [100, 200, 300, ...]: "))
                self.wager(mybet)

                # print game info
                print(self.game_info())

                # checking if bet is greater than half of user player cash
                if self.bet >= 0.5 * self.cash:
                    print("You are a man who admires risks, we love you..")

                # this is where the random numbers are generated
                # you can alter this to suite your needa
                start, end = 0, 2
                cpunumber = random.randint(start, end + 1)

                guess = int(input(
                    f"{self.username}, be smart and pick your lucky number between {start} and {end}: "))

                if cpunumber == guess:
                    self.bet *= 2
                    self.cash += self.bet

                    # print game info
                    print(self.game_info())
                    print(
                        f"{self.username}, you won this time.. your cash is : {self.cash}")
                else:
                    self.bet = 0
                    # print game info
                    print("you loss..")
                    print(self.game_info())

                if self.cash < 100:
                    print(
                        "Man you have no cash.. You better walk away.. else i'd mob the dirty floor with your damn broke face..")

                    # print user info
                    print(self.game_info())
                    endgame = "no"
                else:
                    endgame = input("Do you want to keep playing? ").lower()

            except ValueError as e:
                print("Dikward.. i bet your broke fat beefy ass you are a cash crop.. start with a hundred and I will double it in addition..")

        print(self.game_info())


# create an instance object of the Game class and call the start method
user = Game("f3erQ6$_", 1000)
user.startgame()
