# 3.4 b) Write a program that
# estimates the value of the mathematical constant e by using the formula

e = 1.0
i = 1
factorial = 1.0
n = eval(input("Input a number: "))

while (i <= n):
    j = 1
    while (j <= i):
        factorial *= j;
        j = j+1
    i = i+1
    e = e + (1.0 / factorial);

print(e)


