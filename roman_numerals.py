# This program rewrites a decimal integer to a roman numeral

# get number from the user
num = int(input("Enter a number from 1 - 10: "))

# validate input
while num < 1 or num > 10:
    num = int(input("Enter a number from 1 - 10: "))

# assign numbers to roman numerals
if num == 1:
    print("I")
elif num == 2:
    print("II")
elif num == 3:
    print("III")
elif num == 4:
    print("IV")
elif num == 5:
    print("V")
elif num == 6:
    print("VI")
elif num == 7:
    print("VII")
elif num == 8:
    print("VIII")
elif num == 9:
    print("IX")
else:
    print("X")