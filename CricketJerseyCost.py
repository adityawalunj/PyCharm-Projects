def main():
    totalCost=0;
    size =["S","M","L","XL"];
    for i in range(3):
        playernum=i+1;
        tshirtSize=inputSize(playernum);
        while tshirtSize.upper() not in size:
            print("Please enter a valid Tshirt size ")
            tshirtSize=inputSize(playernum);
        if i>1:
            print("Thank You for your time");
        else:
            print("Awesome!Good to go further");
        totalCost=totalCost+calcPrice(tshirtSize);
    totalCost=formatCurrency(totalCost);
    print("------------------------------------------------------------");
    print("Total Cost for the equipments of three players  :",totalCost);
    print("------------------------------------------------------------");

def inputSize(playernum):
    print("Enter the t-shirt size of Player ",playernum," please")
    tshirtSize=input(" (S)mall,(M)edium,(L)arge (XL) Extra Long :");
    return tshirtSize;

def calcPrice(tshirtSize):
    if tshirtSize.upper()=="S":
        return 70+130+45;
    elif tshirtSize.upper()=="M":
        return 70+130+55;
    elif tshirtSize.upper()=="L":
        return 70+130+65;
    elif tshirtSize.upper()=="XL":
        return 70+130+75;

def formatCurrency(price):
    str1="$"
    price=format(price,'.2f')
    str2=str(price)
    currency=str1+str2
    return currency

main()