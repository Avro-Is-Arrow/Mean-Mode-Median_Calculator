import math

# IMPLEMENT RANGE


listOfNumbers = [1, 2, 3] # List array, change values as needed


#Mean Calculation, Can be thrown off by outliers
def calculateMean(listOfNumbers: list):
    sumOfAllElements : int = 0
    for num in listOfNumbers:
        sumOfAllElements += num

    print(f"Mean is: {math.ceil(int(sumOfAllElements / len(listOfNumbers)))}")

#Mode Calculation
def calculateMode(listOfNumbers: list):
    largestValue = 0
    keyWhichHoldsTheLargestValue = 0
    MostFeqValuesInAList = {}

    for num in listOfNumbers:

        if num in MostFeqValuesInAList:
            MostFeqValuesInAList[num] += 1

        else:
            MostFeqValuesInAList[num] = 1

    for key, value in MostFeqValuesInAList.items():
        if value > largestValue:
            largestValue = value
            keyWhichHoldsTheLargestValue = key
            
    print(f"The mode is: {keyWhichHoldsTheLargestValue}... With the amount of times it appearing being: {largestValue}")

#Median Calculation, not thrown off by outliers
def calculateMedian(listOfNumbers):
    sortedList = sorted(listOfNumbers)

    if ((len(sortedList) % 2) != 0):

        print(f"Median is: {sortedList[int( ( len ( sortedList ) - 1 ) / 2 ) ]}")

    else:
        position1 = sortedList[(int( ( len ( sortedList ) - 1 ) / 2 )) - 1 ]
        position2 = sortedList[(int( ( len ( sortedList ) - 1 ) / 2 )) + 1 ]
        print(f"Median is: {int((position1 + position2) / 2)}")


print(f"ENTIRE LIST: {listOfNumbers}\n")
calculateMean(listOfNumbers)
calculateMode(listOfNumbers)
calculateMedian(listOfNumbers)



