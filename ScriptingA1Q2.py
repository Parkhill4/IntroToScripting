"""
    Question 2: This programs calculates the acreage of a tract of land, using
                a number inputed by the user
"""
Acre = 43560
userInput = int(input("Enter the total square feet of a tract of land: "))
calcAcres = userInput/Acre
print("There are:", calcAcres, "acres")
