import random

Balance = 100

def quit(remanin_balance,totalbet):
    print("Your final balance is " + str(remaning_balance) + ". Overall you lost .", totalbet)



def gamefunction():
    remaning_balance = 100
    print("Your balance is ",remaning_balance)
    round = 0
    totalbet = 0
    if remaning_balance > 0:
        while round <= 10:      #calculate round from to 10
            bets = betting_amount()   #recall function from betting amount()
            totalbet = 0           #here total bet is declare zero so that user can see how much they lose money
            playercard = cardassigning() #recall function from random card
            computercard = cardassigning()
            g = "Computer card",computercard[0],computercard[1]
            print("Your card is ",playercard[0],(playercard[1])) #here playercard[0] = playernumber and playercard[1]=
            player_ans = player_input()                          #player card name  same for computercard
            if player_ans == "l":
                if playercard[1] > computercard[1]:
                    remaning_balance = int(bets) + remaning_balance
                    print(g)
                    print("Awesome guess, you win this round! You won $" + bets + "!")

                elif (playercard[1] < computercard[1]):
                    remaning_balance = remaning_balance - int(bets)
                    totalbet = totalbet + int(bets)
                    print(g)
                    print("Oh no! You lose this round, better luck next time. You lost $",bets)
                else:
                     print("It’s a tie!")
                print(g)
            elif (player_ans  == "h"):
                if playercard[1] > computercard[1]:
                    remaning_balance = int(bets) + remaning_balance
                    print(g)
                    print("Woohoo!, you guessed it right! You won $" + str(bets) + "!")

                elif playercard[1] < computercard[1]:
                    remaning_balance = remaning_balance - int(bets)
                    print(g)
                    print("Uh oh! You lose this round, better luck next time. You lost $", bets)
                    totalbet = totalbet + int(bets)
                else:
                    print("It’s a tie! ")
                    print(g)
            print("The computer’s card is " + computercard[0], computercard[1] + ".")
            userinput = input("Continue (C) or Quit (Q)?").lower()
            while not (userinput == 'q' or 'c'):
                userinput = input("Continue (C) or Quit (Q)?").lower()
                print(userinput)

            if userinput == 'c':  # if user enter c than round get pluse one to round variable
                round = round + 1
                print("Round finished ",round)
            else:
                round = 10
                break

    else:
        print("your balance is low")


    print("Your final balance is "+str(remaning_balance)+". Overall you lost .",totalbet)
    return remaning_balance



#-----------------------------------------------------------------------------------------------------------------------
def player_input():# take player input whether high or low
    ans = str(input(" Is the computer’s card higher (H) or lower (L)? ")).lower()
    while not (ans == "h" or "L"):
        ans = str(input( "Incorrect option, please choose H for Higher or L for Lower.\n" )).lower()
    return ans

#-----------------------------------------------------------------------------------------------------------------
def cardassigning():#give random card from dictionary
    cards_dict = {'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5', 'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9',
             'Ten': '10', 'Jack': '11', 'Queen': '12', 'King': '13', 'Ace': '1'}

    cards = random.choice(list(cards_dict.items()))
    return cards

#-----------------------------------------------------------------------------------------------------------------------
def betting_amount():
    bet = input(" How much do you want to bet?")
    while not bet.isdigit() or int(bet) % 5 != 0 or int(bet) > 100:
        del bet
        #Delete varable value so that prevent the str error and int
        print("Invalid bet value! How much do you want to bet? ")
        bet = input()
    return bet
#-----------------------------------------------------------------------------------------------------------------------
def Getname():
    name = input("Please enter your name.")
    while not name.isalpha():
        name = input(" It’s unlikely that your name is " + name+ ". Please enter your name? ")
    while name == " ": # if user enter space for input than ask again
            name = input("Please enter your name to begin.")
    print( name+" welcome to the Computer Wars Game!")
    return name
#----------------------------------------------------------------------------------------------------------------------

def main():
    g = Getname()
    s = gamefunction()
    print(g,"have a good day")
main()




