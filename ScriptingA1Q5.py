"""
    Question 5: This program will ask the user to add up different coins
                so that the final total equals 100 cents or 1 dollar.
"""

#Each letter corresponds to the first letter of the coin
q = 25
d = 10
n = 5
p = 1

print("In this game you will enter the number of coins to equal 1 dollar")
quarters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickels = int(input("Enter the number of nickels: "))
pennies = int(input("Enter the number of pennies: "))
#We take the number entered by the user and multiply it by the coins amount
quarters = quarters * q
dimes = dimes * d
nickels = nickels * n
pennies = pennies * p
#Adding all of the coins together
total = quarters + dimes + nickels + pennies
#Displaying the outcome to the user depending on their result
if total == 100:
    print("*********CONGRATULATIONS THE TOTAL EQUALED 1 DOLLAR*********")
if total < 100:
    print("The total was",total, "which is less than 100")
if total > 100:
    print("The total was",total, "which is greater than 100")
