def calculateRubricMarks(maxMarks, percentage):
    marks = maxMarks * percentage/100
    return marks

# res = calculateRubricMarks(25,40) \n print (res) ---- testing for above function

def readPercentage(prompt):
    print(prompt)
    percentage = float(input())
    return percentage

def showRubricMarks(rubricNr, marks):
    print("Rubric", rubricNr,":", marks,"marks")

def calculateTotalMarks(marks1, marks2, marks3):
        total = marks1 + marks2 + marks3
        return total

def main():
    RUBRIC1_MAXMARKS = 25    #3 constants for max marks
    RUBRIC2_MAXMARKS = 25
    RUBRIC3_MAXMARKS = 50

    percentageRubric1 = readPercentage("Enter percentage Rubric 1: ")
    percentageRubric2 = readPercentage("Enter percentage Rubric 2: ")
    percentageRubric3 = readPercentage("Enter percentage Rubric 3: ")

    marksRubric1 = calculateRubricMarks(RUBRIC1_MAXMARKS, percentageRubric1)
    marksRubric2 = calculateRubricMarks(RUBRIC2_MAXMARKS, percentageRubric2)
    marksRubric3 = calculateRubricMarks(RUBRIC3_MAXMARKS, percentageRubric3)

    showRubricMarks(1, marksRubric1)
    showRubricMarks(2, marksRubric2)
    showRubricMarks(3, marksRubric3)

    totalMarks = calculateTotalMarks(marksRubric1, marksRubric2, marksRubric3)
    print(totalMarks)

main()





