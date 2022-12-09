# 3.4 a) Write a program that reads a nonnegative integer and
# computes and prints its factorial.

input_number = -1
while (input_number<=0):
    input_number = input("Input a nonnegative integer: ")
    input_number = int(input_number)

temp = input_number
while (True):
    if (temp == 1 ):
        break;
    temp = temp-1
    input_number = input_number*temp

print(input_number)


