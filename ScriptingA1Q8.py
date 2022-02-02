"""
    Question 8: This program details joes timeline in his stock exchange
"""
joeShares = 2000
paidShares = 40.00
soldShares = 42.75
bought = joeShares * paidShares
sold = joeShares * soldShares
paidBroker1 = (bought * 0.03)
paidBroker2 = (sold * 0.03)
#Calculate whether the money he has left is positive or negative
moneyLeft = bought - sold - paidBroker1 - paidBroker2
#Display all the information to the user after all calculations
print("Joe paid $", bought, "for 2000 shares")
print("Joe paid $", paidBroker1, "to his broker after he bought the shares the first time")
print("Joe sold his stock for $", sold)
print("Joe paid $", paidBroker2, "to his broker after he sold his shares")
#Displaying whether the money left was a profit or not
if moneyLeft > 0:
    print("Joe earned $",moneyLeft)
if moneyLeft < 0:
    print("Joe lost $",moneyLeft)
