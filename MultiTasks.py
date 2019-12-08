#Week 8
#Aditya Walunj
#JC479344


#Task1
def getValue():

 num = int (input("Enter a number"))
 return num

def main():

    numberVal = getValue()

    print(numberVal)

main()

#Task2
def main():
    sentence=str(input("Enter any sentence"))
    showasterisk()
    divideSentence(sentence)
    showasterisk()

def showasterisk():
        asterisk = "*"
        lineOfAsterisk = ""

        for i in range(20):
            lineOfAsterisk = lineOfAsterisk + asterisk
        print(lineOfAsterisk)

def divideSentence(sentence):
    length = len(sentence)
    halfLength = length//2
    print(sentence[0:halfLength])
    print(sentence[halfLength:length])


main()



#task3

def main():
    names = list()
    for i in range(3):
        firstName=str(input("Enter your first name"))
        names.append(firstName)
    printNames(names)

def printNames(names):

    for i in range(3):
        print(i,names[i])

main()

#task4
def main():

    multipicationTable()


def multipicationTable():
   number = int(input("Enter the number: "))
   print("Johnny's time tables ")
   print("The time table for %d is: " % number)



   for i in range(1,10):


    print(number,"*", i ,"=",number*i)

main()
