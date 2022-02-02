"""
    Question 4: This program asks the user to enter their age and displays what
                age group they fall under
"""

userAge = int(input("Enter your age: "))
if userAge <= 1:
    print("You are an infant")
if userAge > 1 and userAge < 13:
    print("You are a child")
if userAge >= 13 and userAge < 20:
    print("You are a teenager")
if userAge >= 20:
    print("You are an adult")
