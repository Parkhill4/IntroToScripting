"""
    Question 6: This program will identify whether a year entered by the user
                is a leap year or not
"""

userInput = int(input("Enter a year to check if it is a leap year: "))
#Checking the remainder for the year after dividing it multiple times
if userInput %100 == 0 and userInput %400 == 0:
    print("The number of days in february in",userInput,"is 29")
if userInput %100 != 0 and userInput %4 == 0:
    print("The number of days in february in",userInput,"is 29")
else:
    print("The number of day in February in",userInput,"is 28")
