# 3.5 Write a program that prints the following patterns separately, one below the other each pat- tern separated from the next by one blank line. Use for loops to generate the patterns. All asterisks (*) should be printed by a single statement of the form
# print '*',
# (which causes the asterisks to print side by side separated by a space). (Hint: The last two patterns require that each line begin with an appropriate number of blanks.) Extra credit: Combine your code from the four separate problems into a single program that prints all four patterns side by side by making clever use of nested for loops. For all parts of this program—minimize the numbers of asterisks and spaces and the number of statements that print these characters.
# a) Half pyramid
# b)Left Half Pyramid
# c) Inverted half pyramid d)Full inverted Pyramid

rows = 5

"""
#a) Half pyramid

*

*  *

*  *  *

*  *  *  *

*  *  *  *  *
"""
print("a) Half pyramid")
for i in range(rows):
    for j in range(i+1):
        print("* ", end=" ")
    print("\n")

"""

#b) Left Half Pyramid

            *

         *  *

      *  *  *

   *  *  *  *

*  *  *  *  *
"""
print("b)Left Half Pyramid")
for i in range(rows):
    loop = rows-i
    j = 1
    while j < loop:
        print(end="   ")
        j += 1
    k = 0
    while k <= i:
        print("* ", end=" ")
        k += 1
    print("\n")

"""

#c) Inverted half pyramid

*  *  *  *  *

*  *  *  *

*  *  *

*  *

*
"""
print("c) Inverted half pyramid")
for i in range(rows):
    loop = rows - i
    for j in range(loop):
        print("* ", end=" ")
    print("\n")

"""

#d) Full inverted Pyramid

*  *  *  *  *  *  *  *  *

   *  *  *  *  *  *  *

      *  *  *  *  *

         *  *  *

            *

"""
print("d) Full inverted Pyramid")
rows = 9
loop = rows

for i in range(rows):
    k = 0
    for j in range(loop):
        while(k<i):
            print(end="   ")
            k = k+1
        print("* ", end=" ")

    loop = loop - 2

    print("\n")



