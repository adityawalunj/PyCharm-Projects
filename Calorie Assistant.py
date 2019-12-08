#Calorie Intake Assistant
from random import randint
import random
quitFlag = False
totalADCI = 0

def main():
    global totalADCI #global variable
    global userName
    global quitFlag
    userName= getName("Welcome to the Calorie Intake Assistant, my name is Cal. What is your name?\n")
    print("Hi" ,str(userName),"!")
    userInput = getUserConsent("To properly assist you, we will need some personal information such as age, gender, weight and height. Do you want to continue? Enter Y for yes or N for no.")
    while quitFlag != True: #program proceeds to ask consent and passes to getUserGender()
            if userInput =="N" or userInput=="n": #checks for upper and lower cases.
                print("That’s alright, good bye",str(userName),"!")
                exit()#program exits with a goodbye message
            else:
                print("Great",str(userName))
                getGender=getUserGender("Great, let’s start! What is your gender? Enter M for male or F for female.") #recalls function getUserGender()
                getAge=getUserAge("\nWhat is your age in years?")#recalls function getUserAge()
                getWeight=getUserWeight("\nWhat is your current weight in kg?")#recalls function getUserWeight()
                getHeight=getUserHeight("\nWhat is your height in cm?")#recalls function getUserHeight()
                if getGender == "M" or getGender == "m":#checks for upper and lower cases.
                    RDCI = 10 * getWeight + getHeight - 5 * getAge + 5 #calculates RDCI for men
                else:
                    RDCI = 10 * getWeight + getHeight - 5 * getAge - 161 #calculates RDCI for women
                print("\n \nThank You for your information",str(userName),"\nConsidering the details given, your daily recommended intake is of" ,RDCI, "calories per day.")
            print("Let’s see how healthy your meals were last week.")
            for i in range(1,8): #range for 7 days
                print("Day",str(i))
                getDailyInput= DailyDiet(" were your meals very unhealthy (1), unhealthy (2), healthy (3), or very healthy (4)? Enter the corresponding number.") #calls DailyDiet() function
                if DailyDiet == 1:
                    ADCI = RDCI * 1.5
                elif DailyDiet == 2:
                    ADCI = RDCI*1.2
                elif DailyDiet == 3:
                    ADCI = RDCI
                else:
                    ADCI=RDCI*0.8
                totalADCI += i
            print(str(userName), " here are your results:")

            for j in range(1, 8): #fix?
                haveTemptation = randint(0, 1)
                if int(haveTemptation)==1:
                    randNumber=randint(1,7)
                    if randNumber==1:
                        tempt=250
                    elif randNumber==2:
                        tempt=550
                    elif randNumber==3:
                        tempt=207
                    elif randNumber==4:
                        tempt=350
                    elif randNumber==5:
                        tempt=180
                    elif randNumber==6:
                        tempt=257
                    else:
                        tempt=357
                    ADCIx=int(ADCI)+int(tempt)
                    print(str(ADCIx), " calories for day ", str(j))
                    print("Also, it looks like this day you’ve been tempted with", temptation.prompt[tempt], "and",str(tempt), "calories have been added!")
                else:
                    ADCIx=int(ADCI)
                    print(str(ADCIx), " calories for day", str(j))


            suggestions(RDCI, ADCIx, userName, totalADCI)

#-----------------------------------------------------------------------------------------------------------------------
def suggestions(RDCI, ADCI, userName, totalADCI):

    avgADCI=totalADCI/7
    final = avgADCI % RDCI
    if final>100:
        Difference =final-100
    else:
        Difference=100-final
    if final<90:
        print(str(userName),"your daily calorie intake is lower than the recommended with",str(Difference),"%. This rhythm will make you lose weight, just make sure your meals contain all nutritional value needed. It’s recommended that you do not fall under the healthy weight and that you keep a balanced lifestyle.")
    elif final>110:
        print(str(userName),"your daily calorie intake is higher than the recommended with",str(Difference),"%. This rhythm will make you gain weight which will lead to health concerns. It’s recommended that you either lower your calorie intake, either exercise more!")
    else:
        print(str(userName),"your daily calorie intake is close to the recommended one! You have a balanced healthy lifestyle, well done!")

    print("Goodbye and good luck!")

    exit()

#-----------------------------------------------------------------------------------------------------------------------

def getName(prompt): # Function for getting valid username
    prompt=input(prompt) #prompts user for an input
    while  not prompt.isalpha() or len(prompt.strip(" "))<1: #checks for invalid input like numbers, special characters or blank spaces
        prompt=input("Don’t be shy. What is your name?\n")
    return prompt
#-----------------------------------------------------------------------------------------------------------------------
def getUserConsent(prompt): # Function for getting user's consent to proceed or exit with the program
    prompt=input(prompt)
    while prompt!="Y" and prompt!="y" and prompt!="N" and prompt!="n": #accepts both uppercase and lowercase.
        prompt=input("I’m sorry, I cannot understand. To properly assist you, we will need some personal information such as age, gender, weight and height. Do you want to continue? Enter Y for yes or N for no.\n")
    return prompt
#-----------------------------------------------------------------------------------------------------------------------
def getUserGender(prompt): # Function for getting user's gender
    prompt=input(prompt) #prompts user for an input
    while prompt!="M" and prompt!="m" and prompt!="F" and prompt!="f": #accepts both uppercase and lowercase.
        prompt=input("I’m sorry, I cannot understand. What is your gender? Enter M for male or F for female.\n")
    return prompt
#-----------------------------------------------------------------------------------------------------------------------
def getUserAge(prompt): #Function to get user's age
    prompt = input(prompt)
    while (not prompt.isdigit() or int(prompt)<0 or int(prompt)>99): #checks for invalid input  like alphabets or special characters or wrong age.
        prompt=input("I’m sorry, I cannot understand. What is your age in years?\n")
    return int(prompt)
#-----------------------------------------------------------------------------------------------------------------------
def getUserWeight(prompt): #Function to get user's weight
    prompt = input(prompt)
    while (not prompt.isdigit() or int(prompt)<40 or int(prompt)>150): #checks for a no. Weight cannot be less than 40 kg or greater than 150kg
        prompt=input("I’m sorry, I cannot understand. What is your weight in kgs?\n")
    return int(prompt)
#-----------------------------------------------------------------------------------------------------------------------
def getUserHeight(prompt): #Function to get user's height
    prompt = input(prompt)
    while (not prompt.isdigit() or int(prompt)<80 or int(prompt)>230): #height cannot be less than 80 cms or more than 230 cms
        prompt=input("I’m sorry, I cannot understand. What is your height in cms?\n")
    return int(prompt)
#-----------------------------------------------------------------------------------------------------------------------
def DailyDiet(prompt): #Function to get user option for meals.
    prompt = input(prompt)
    while (not prompt.isdigit() or int(prompt)<1 or int(prompt)>4): #makes sure the no. entered is between 1-4
        prompt = input("I’m sorry, I cannot understand. Kindly enter a valid response.\n")
    return int(prompt)
#-----------------------------------------------------------------------------------------------------------------------
class temptation: #class for tempatation with assigned values
    prompt = {250:'chocolate',550:'chips',207:'ice-cream',350:'fast-food',180:'fizzy drink',257:'party cake',357:'popcorn'}

main()
#END