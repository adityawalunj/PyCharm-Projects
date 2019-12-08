#Aditya Walunj
#JC479344
#Ascending order not working

# TASK 3
def divisbleNumber(userInput):
    if ((userInput % 3 == 0) and  (userInput % 5==0)) :
        print('FizzBuzz')
    elif userInput % 3 == 0:
            print('Fizz')
    elif userInput % 5 == 0:
            print('Buzz')
    else:
        print(userInput)

def main():
    for i in range(1, 51):
        divisbleNumber(i)
main()

## TASK 5
def getValue(userInput):
    value=input("Enter a number")
    while not value.isdigit():
            print("Invalid Input")
            value=input(userInput)
    return value

def main():
    userList=[]
    for i in range(0,5):
        value=getValue("Enter the number")
        userList.append(value)
        userList.sort()
    print("number in ascending order is:",userList )
main()
