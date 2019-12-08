def getValidMoney():
    money = int(input("Please enter an AUD$ amount to be converted. Whole numbers only please:\n "))
    while  money <= 0:
        print("I'm sorry values must be greater than 0. Please try again.\n")
        money = int(input("Please enter an AUD$ amount to be converted. Whole numbers only please: \n"))
    print("Thank you.")
    return money

def getValidCurrency():
    answer=input('What currency would you like this converted into: (P)ounds, (U)S Dollars, (E)uros or (B)itcoin?\n')
    validCurrencies=['P','U','E','B']
    while answer.upper() not in validCurrencies:
        answer = input('What currency would you like this converted into: (P)ounds, (U)S Dollars, (E)uros or (B)itcoin?\n')
    print("Thank you.")
    return answer.upper()

def getValidChoice():
    answer=input('Would you like to convert another amount (Y/N)?\n')
    while answer.upper() not in ["Y", "N"]:
        answer = input('Would you like to convert another amount (Y/N)?\n')
    return answer.upper()


def convertAUDtoCurrency(audAmount, currency):
    POUNDRATE = 0.52
    USRATE = 0.68
    EURORATE = 0.62
    BITCOINRATE = 0.000092

    rate = 0
    currencyName = ""
    if currency == "P":
        rate = POUNDRATE
        currencyName = "Pounds"
    elif currency == "U":
        rate = USRATE
        currencyName = "USD"
    elif currency == "E":
        rate = EURORATE
        currencyName = "Euros"
    else:
        rate = BITCOINRATE
        currencyName = "Bitcoins"

    amount = audAmount * rate
    print ("$" + str(audAmount) + " AUD equals "+str(amount)+" "+ currencyName + ".")
    return amount

def main():
    print("Welcome to the Python Currency Converter.")

    choice = "Y"
    while choice == "Y":
        money = getValidMoney()
        currency = getValidCurrency()
        convertAUDtoCurrency(money, currency)
        choice = getValidChoice()

    print("Thank you for using Python Currency Converter.")

main()
