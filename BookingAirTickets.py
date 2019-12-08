#Aditya Walunj
#JC479344

#Main function contains lists,variables and constants.
#Main calls all the functions to process to return an output.
#Lists used to get inputs from user
def main():
    ticketCost = 0 #ticketCost set to zero. Constant

    MENUPROMPT = "\nTropical Airlines Ticket Ordering System \n\n(I)nstructions\n(O)rder Ticket\n(E)xit"
    MENUERROR = "\nInvalid menu choice."
    MENUCHOICES = ['I', 'O', 'E'] #Valid List

    TICKETPROMPT = "\nIs this ticket for: \n(Y)ou \n(S)omeone else"
    TICKETERROR = "\nInvalid input. Please Enter 'Y' or 'S' " #Error messages guide user to feed a valid input if they enter an invalid input
    TICKETCHOICES = ['Y','S']
    TICKETNAME = "Please enter the name of the person travelling"

    TRIPPROMPT = "\nIs this a return trip (R) or One-Way trip (O)"
    TRIPERROR = "\nInvalid input. Please select 'R' or 'O'"
    TRIPLIST = ['R','O']

    ONEWAYPROMPT = "\nPlease select the destination for your One Way trip. Fare prices are listed below. \n(C)airns - $250 \n(S)ydney - $420 \n(P)erth - $510 " #Prompts when user selects One Way Trip.
    RETURNPROMPT = "\nPlease select the destination for your Return trip. Fare prices are listed below. \n(C)airns - $400 \n(S)ydney - $575 \n(P)erth - $700 " #Prompts when user selects Return Trip.
    DESTERROR = "\nInvalid destination input. Please enter C,S or P"
    DESTCHOICES = ['C','S', 'P']

    CLASSPROMPT = "\nPlease choose the type of fare. Fees are displayed below and are in addition to the basic fare.\nPlease note choosing Frugal fare means you will not be offered a seat choice.\n(B)usiness \n(E)conomy \n(F)rugal"
    CLASSERROR ="\nInvalid fare type. Please enter B,E or F."
    CLASSLIST = ['B','E','F']

    SEATPROMPT = "\nPlease choose the seat type. Choosing the middle seat will deduct 25 from the total fare. \n\n(W)indow $75\n(A)isle $50 \n(M)iddle -$25"
    SEATERROR = "\nInvalid seat type. Please enter W, A or M"
    SEATLIST = ['W','A','M']

    AGEPROMPT = "\nHow old is the person travelling? Travellers under 16 years old will recieve a 50% discount for the child fare."
    AGEERROR = "\nInvalid age. Please enter your age in number"
    AGEMIN = 0 #Minium age limit
    AGEMAX = 113 #Maximum age limit. 113 because the world's oldest man is 113 years old.

    userName = getUsername("Welcome to Tropical Airlines App.\nPlease Enter your name :")
    print("\nWelcome",userName + '.')
    menuChoice = getValidInput(MENUPROMPT,MENUERROR,MENUCHOICES)
    ticketsList = []
    while menuChoice != "E": #while loop which exits when condition is while menuChoice == "E"
        if menuChoice == "I":
            print("\nThank you for choosing Tropical Airlines for your air travel needs.\nYou will be asked questions regarding what type of ticket you would like to purchase as well as destination information. \nWe also offer 50% discounted fares for children.")
            menuChoice = getValidInput(MENUPROMPT, MENUERROR, MENUCHOICES) #Prompts user to select from the menu again after user selects I for Instructions.
        elif menuChoice == "O": #Ticket Ordering begins from here with program asking user for name of the traveller.
            passenger = getValidInput(TICKETPROMPT,TICKETERROR,TICKETCHOICES)
            if passenger == "S":
                userName = getUsername(TICKETNAME) #If user is booking ticket for someone else, program will prompt user for traveller's name.
            else:
                passenger = userName #If user is booking tickets for him/her.
            trip = getValidInput(TRIPPROMPT,TRIPERROR,TRIPLIST)
            if trip == "R":
                destination = getValidInput(RETURNPROMPT,DESTERROR,DESTCHOICES)
                destinationPrice = getDestinationCostReturn(destination)
            else:
                destination = getValidInput(ONEWAYPROMPT,DESTERROR,DESTCHOICES)
                destinationPrice = getDestinationCostOneWay(destination)

            classType = getValidInput(CLASSPROMPT, CLASSERROR, CLASSLIST)
            classPrice = getFareType(classType)

            seatType = getValidInput(SEATPROMPT,SEATERROR,SEATLIST)
            seatPrice = getSeatType(seatType)

            userAge = getAge(AGEPROMPT, AGEERROR, AGEMIN, AGEMAX)

            ticketCost = calculateFare(destinationPrice,classType,seatType)
            ticketCost = formatCurrency(ticketCost)

            outputSummary = displaySummary(userName,destination,classType,seatType,userAge,ticketCost)

            ticketsList.append(ticketCost)
            menuChoice = getValidInput(MENUPROMPT, MENUERROR, MENUCHOICES)
    print(ticketsList.sort())#Built-in function used. sort.
    print( userName + ',' + "Your final total is :", ticketCost, "Thank You for visiting Tropical Airlines")
    exit()

#Function to get user name. Function validated to accept only alphabets. Feeding empty strings or special characters or even numbers will display error and prompt user again for input.
def getUsername(prompt):
    name = input(prompt)
    while not name.isalpha():
        print("Invalid name. Please enter valid name.")
        name = input(prompt)
    return name

#Function to get valid input. Function validated to accept inputs which are in valid lists. Function re-used many times.
def getValidInput(prompt, error, optionList):
    value=input(prompt)
    value = value.upper()
    while value not in optionList:
        print(error)
        value=input(prompt)
        value = value.upper()
    return value

#Function to get user age. Function validated to accept age between 0 to 113. Displays error if anything other than numbers is fed as input.
def getAge(prompt,error,min,max):
    age = input(prompt)
    while not age.isdigit or int(age) < min or  int(age) > max:
        print(error)
        age = input(prompt)
    return int(age)

#Function to get destination cost for One Way Trip. Contains constants and selections.
def getDestinationCostOneWay(destination):
    CAIRNS_ONEWAY = 250 #fixed constants
    SYDNEY_ONEWAY = 420
    PERTH_ONEWAY = 510
    if destination == "C":
        journey = CAIRNS_ONEWAY
    elif destination == "S":
        journey = SYDNEY_ONEWAY
    else:
        journey = PERTH_ONEWAY
    return journey

#Function to get destination cost for Return trip. Contains constants and selections.
def getDestinationCostReturn(destination):
    CAIRNS_RETURN = 400
    SYDNEY_RETURN = 575
    PERTH_RETURN = 700
    if destination == "C":
        journey = CAIRNS_RETURN
    elif destination == "S":
        journey = SYDNEY_RETURN
    else:
        journey = PERTH_RETURN
    return journey

#Function to get type of Class in an airplane. Contains constants and selections.
def getFareType(classType):
    BUSINESS = 275
    ECONOMY = 25
    FRUGAL = 0

    if classType == "B":
        fare = BUSINESS
    elif classType == "E":
        fare = ECONOMY
    else:
        fare = FRUGAL
    return fare

#Function to get type of seat in airplane. Contains constants and selections.
def getSeatType(seatType):
    WINDOW = 75
    AISLE = 50
    MIDDLE = -25

    if seatType == "W":
        seat = WINDOW
    elif seatType == "A":
        seat = AISLE
    else:
        seat = MIDDLE
    return seat

#Function to calculate total cost of the ticket based on destination, class and type of seat in an airplane.
def calculateFare(destinationPrice,classType,seatType):
    fare = getFareType(classType)
    seat = getSeatType(seatType)
    total = fare + seat + destinationPrice
    return total

#Function to check and calculate discount for travellers below or equal to 16 years of age.
def childTicketEligibility(userAge,ticketCost):
    AGELIMIT = 16
    if (userAge >= AGELIMIT):
        discount = ticketCost * 0.5
    return discount

#Function to display output in details to user.
def displaySummary(userName,destination,classType,seatType,userAge,ticketCost):

    print("\nCalculating Fare...")
    print("\nTicket for:        ",userName)
    print("\nDestination:       ",destination)
    print("\nTicket Type:       ",classType)
    print("\nSeat Type:         ",seatType)
    print("\nAge:               ",userAge, "(eligible for child ticket, 50% discount applied)")
    print ("\nTotal Price: ",ticketCost)

#Function to place '$' sign before ticketCost
def formatCurrency(ticketCost):
    str1="$"
    ticketCost = format(ticketCost, '.2f')
    str2 =str(ticketCost)
    currency = str1+str2
    return currency

main()

