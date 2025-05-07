import math

listOfNumbers = [2, 43, 12, 43, 54, 43, 64, 43, 65, 87, 100, 12] # List array as needed

print(f"List of Numbers are: {listOfNumbers}\n")

#Mean Calculation
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

#Median Calculation
def calculateMedian(listOfNumbers):
    sortedList = sorted(listOfNumbers)

    if ((len(sortedList) % 2) != 0):

        print(sortedList[int( ( len ( sortedList ) - 1 ) / 2 ) ])

    else:
        position1 = sortedList[(int( ( len ( sortedList ) - 1 ) / 2 )) - 1 ]
        position2 = sortedList[(int( ( len ( sortedList ) - 1 ) / 2 )) + 1 ]
        print(f"Median is: {int((position1 + position2) / 2)}")
    
    
calculateMean(listOfNumbers)
calculateMode(listOfNumbers)
calculateMedian(listOfNumbers)



