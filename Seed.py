def main():
    SEED = 100
    num1 = 10  #local variables that exist in main only, num1,num2,sum
    num2 = 20
    sum = calcSum(num1, num2, SEED)
    print("Seed is: " +str(SEED))
    print("Sum is " + str(sum))

def calcSum(value1, value2, seed): #main does not know who result is or value1 and value2
    result = value1 + value2 + seed
    return result

main()