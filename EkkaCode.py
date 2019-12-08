#importing sys for sys.maxsize()
import sys

#CONSTANTS
SHOWBAG_PRICE = 20
ICE_CREAM_PRICE = 4
ADULT_TICKET = 35
CHILD_TICKET = 20
JOINT_TICKET = 45

def main():

    ADULTPROMPT = "Please Enter the no. of Tickets for Adults attending Ekka - \n"
    ADULTERROR = "Invalid input. Please Enter a number only \n"

    CHILDRENPROMPT = "Please Enter the no. of Tickets for Children attending Ekka - \n"
    CHILDRENERROR = "Invalid input. Please Enter a number. \n"

    SHOWBAGPROMPT = "Please Enter the no. of Showbags - \n"
    SHOWBAGERROR = "Invalid input. Please Enter a number. \n"

    adultTicket = getValidNumber(ADULTPROMPT, ADULTERROR, 1, sys.maxsize)
    childTicket = getValidNumber(CHILDRENPROMPT,CHILDRENERROR, 0, sys.maxsize)
    showBags = getValidNumber(SHOWBAGPROMPT,SHOWBAGERROR,0,sys.maxsize)

    totalCost = calcTicketCost(adultTicket,childTicket) + calcExtraCost(childTicket, showBags)
    displayTotal(childTicket, adultTicket, showBags, totalCost)


def getValidNumber(prompt, error, min, max):
    number = input(prompt)
    while not number.isdigit() or int(number) < min or int(number) > max:
        print(error)
        number = input(prompt)
    return int(number)

def calcTicketCost(adultTicket, childTicket):
    if adultTicket > childTicket:
        ticketCost = childTicket * JOINT_TICKET + (adultTicket - childTicket) * ADULT_TICKET
    elif adultTicket < childTicket:
        ticketCost = adultTicket * JOINT_TICKET + (childTicket - adultTicket) * CHILD_TICKET
    else:
        ticketCost = adultTicket * JOINT_TICKET
    return ticketCost

def calcExtraCost(childTicket, showBags):
    bags = showBags * SHOWBAG_PRICE
    iceCream = childTicket * ICE_CREAM_PRICE
    other = bags + iceCream
    return other

def displayTotal(childTicket, adultTicket, showBags, totalCost):
    print("\n----------------------------------------------------------------")
    print("No. of tickets confirmed for Adults: ", adultTicket)
    print("No. of tickets confirmed for Children (Joined Tickets) : ", childTicket)
    print("No. of Show Bags purchased:", showBags)
    print("No. of Ice Cream worth $4, each child gets for free: ", childTicket)
    print("\nTotal Cost for your tickets is: $", totalCost, "\n\nThank You for booking your tickets for The Royal Queensland Show - Ekka. \nDates: 10th August - 19th August 2018. \nSee you on Brisbane grounds.")
    print("\n----------------------------------------------------------------")

main()
