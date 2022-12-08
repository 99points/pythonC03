# your code goes here
gallonUsed = 0
gallonUsedTotal = 0
miles = 0
totalMiles = 0
while gallonUsed >= 0:
    gallonUsed = (input("Enter the gallons used (-1 to end): "))
    gallonUsed = float(gallonUsed)
    if gallonUsed >= 0:
        miles = (input("Enter the miles driven: "))
        miles = float(miles)
        totalMiles = totalMiles + miles
        gallonUsedTotal = gallonUsedTotal + gallonUsed

        output = (miles / gallonUsed)
        output = float(output)
        print("The miles / gallon for this tank was " )
        print(output)

FinalOutput = totalMiles / gallonUsedTotal
print("The overall average miles/gallon was: " )
print(FinalOutput)
