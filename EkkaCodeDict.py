
def main():

    CHILDRENINDEX = 0
    ADULTINDEX = 1
    JOINTINDEX = 2
    BAGINDEX = 3
    ICECREAMINDEX = 4

    EKKAPRICES = [20, 35, 45, 20, 4]

    ADULTSPROMPT = " How many adults are visiting Ekka? "
    ADULTSERROR = "Invalid Value.The number of Adults cannot be zero or negative"
    CHILDRENPROMPT = "How many childrens are visiting Ekka? "
    CHILDRENERROR = "INVALID VALUE THE NUMBER OF CHILDREN CANNOT BE NEGATIVE"
    SHOWBAGSPROMPT = "How many ShowBags would you like to purchase? "
    SHOWBAGSERROR = "Invalid Value. You should not get the more Showbags then the number "

    adult = getadults(ADULTSPROMPT, ADULTSERROR)
    children = getChildrens(CHILDRENPROMPT, CHILDRENERROR)
    showbags = getShowbags(SHOWBAGSPROMPT, SHOWBAGSERROR, adult, children)
    #    icrecream = childrens * 4

    quantities = calculateQuantities(adult, children, showbags)

def getadults(prompt, error):
    adults = input(prompt)
    while not adults.isdigit() or int(adults) <= 0:
        print(error)
        adults = input(prompt)
        adults = adults.upper()
    return adults


def getChildrens(prompt, error):
    childrens = input(prompt)
    while not childrens.isdigit() or int(childrens) <= 0:
        print(error)
        childrens = input(prompt)
    return childrens

#def getjointtickets(prompt,error):

def getShowbags(prompt, error, adults, childrens):
    showbags = input(prompt)
    while int(showbags) > int(adults) + int(childrens):
        print(error)
        showbags = input(prompt)
    return showbags


def calculateQuantities(adult,children,showbags,):
    quantities = adult + children + showbags
    return quantities


# def geticecream(prompt,error):
#  icecream = input(prompt)

def calculateEkkaCost(quantities, EKKAPRICES):
     cost = quantities + EKKAPRICES
     return cost

def calculateEkkaDetails(quantities, EKKAPRICES, cost):
    details = quantities + EKKAPRICES + cost
    return details

main()