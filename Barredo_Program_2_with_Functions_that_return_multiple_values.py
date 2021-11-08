# Create a program with functions that return multiple values.
# It will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25 pesos. Display the output in the following format.
# The total amount is _______ pesos.

def prices():
    priceA = 20
    priceB = 25
    return priceA, priceB

def printPriceA_B(priceA, priceB):
    print(f'The price of one apple is {priceA} pesos.')
    print(f'The price of one orange is {priceB} pesos.')

def Quantity_to_purchase():
    applesFunction = int(input('Quantity of apples to Purchase: '))
    orangesFunction = int(input('Quantity of oranges to Purchase: '))
    return applesFunction, orangesFunction

def Total_amount(priceA, apples, priceB, oranges):
    Amount = float(priceA * apples + priceB * oranges)
    return Amount

def displayOutput(Amount):
    print(f'The total amount is {Amount} pesos.')

# Steps
# 1. Print the cost of an apple and an orange.
priceA, priceB = prices()
printPriceA_B(priceA, priceB)
# 2. Inquire with the user about the quantity of apples and oranges to be purchased and save it to a variable.
apples, oranges = Quantity_to_purchase()
# 3. Calculate the total amount you must pay.
Amount = Total_amount(priceA, apples, priceB, oranges)
# 4. Display the Output.
displayOutput(Amount)