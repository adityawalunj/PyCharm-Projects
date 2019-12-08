def main():
    height = float(input("Enter the height in metres: "))
    weight =  float(input("Enter the weight in kgs: "))
    calcBMI = (weight/height**2)
    print(calcBMI)

main()
