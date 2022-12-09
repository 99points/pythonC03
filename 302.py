# 3.2 A palindrome is a number or a text phrase that reads the same backwards or forwards.
# For example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611.
# Write a program that reads in a five-digit integer and determines whether it is a palindrome.
# (Hint: Use the division and modulus operators to separate the number into its individual digits.)

input_text = 0
input_text = input("Enter a number / text to check if its palindrome: ")

if input_text == input_text[::-1]:
    print("Its a palindrome")
else:
    print("No, Its not a palindrome")