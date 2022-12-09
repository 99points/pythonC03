# 3.2 A palindrome is a number or a text phrase that reads the same backwards or forwards.
# For example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611.
# Write a program that reads in a five-digit integer and determines whether it is a palindrome.
# (Hint: Use the division and modulus operators to separate the number into its individual digits.)

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
