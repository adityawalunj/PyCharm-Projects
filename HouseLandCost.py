def main():
    houseCost = int(input("Enter the cost of house: "))
    landSize = int(input("Enter the size of land: "))
    landCost = int(input("Enter the cost of land: "))
    totalLandcost = landSize * landCost
    totalCost = totalLandcost + houseCost
    print("The total cost is", +totalCost)
    print("Land will cost: ", +totalLandcost)

main()
