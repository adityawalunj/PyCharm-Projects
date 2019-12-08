def getValidInput(prompt,error,options):
    value=input(prompt)
    value=value.upper()
    while value not in options:
        print(error)
        value=input(prompt)
        value=value.upper()
    return value

def getValidNumber (prompt,error,min,max):
    number = input(prompt)
    while not number.isdigit() or len(number.strip(" "))<1 or int(number) < min or int(number) > max:
        print(error)
        number = input(prompt)
    return int (number) #int or number?

def calcPrice(value):
    price = 0
    if value =="C":
        price = 25
    elif value =="S":
        price = 35
    elif value =="V":
        price = 45
    elif value =="H":
        price = 100
    return price


def main():
    totalCost = 0

    CARPROMPT = "What type of car you want? \n1.(C)ompact\n2.(S)edan\n3.SU(V)\n4.(H)ummer"
    CARERROR = "Invalid Car Type"
    CARTYPES = ['C','S','V','H']

    GPSPROMPT = "Do you need GPS? (Y/N) "
    GPSERROR = "Invalid input"
    GPSOPTIONS = ['Y','N']

    DAYSPROMPT = "For how many days do you need the car?"
    DAYSERROR =  "Invalid input"
    DAYSMIN =  1
    DAYSMAX =  365

    AGEPROMPT = "What is your age?"
    AGEERROR = "Invalid age"
    AGEMIN = 18
    AGEMAX = 80

    carType = getValidInput(CARPROMPT, CARERROR, CARTYPES)
    carDays = getValidNumber(DAYSPROMPT, DAYSERROR, DAYSMIN, DAYSMAX)
    useGPS = getValidInput(GPSPROMPT,GPSERROR,GPSOPTIONS)
    userAge = getValidNumber(AGEPROMPT,AGEERROR,AGEMIN,AGEMAX)

    totalCost = calcPrice
    #print (sys.maxsize) #?
main()



