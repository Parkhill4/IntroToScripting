"""
    Question 7: This program will calculate a persons BMI
"""
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))
#Calculatng the BMI
BMI = (weight*703)/(height**2)
#FInding where the users BMI falls
if BMI < 18.5:
    print("Your BMI is less than 18.5, you are underweight")
if BMI > 25:
    print("Your BMI is greater than 25, you are overweight")
if BMI >= 18.5 and BMI <= 25:
    print("Your BMI is between 18.5 and 25, your BMI is optimal")
