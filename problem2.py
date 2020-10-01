#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
intnumber = float(input("Enter a number"))
count = 0
mult = 1
output = ""
while count < 12:
    count = count + 1  
    number = intnumber * mult
    mult = mult + 1
    output = output + str(intnumber * mult) + " "

print(output)
