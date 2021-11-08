# Create a program with functions the return multiple values which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy _____ apples and your change is _____ pesos.

def Cash_Price():
    moneyFunction = int(input('Amount of cash you have: '))
    priceFunction = int(input('Price of an apple: '))
    return moneyFunction, priceFunction

def Max_apples(money, price):
    Maximum_apples_you_can_buy = int(money/price)
    return Maximum_apples_you_can_buy

def rem_money(money, Maximum_apples_you_can_buy, price):
    remaining_money = float(money-(Maximum_apples_you_can_buy*price))
    return remaining_money

def displayMaxAppleCanBuy_remainingCash(Maximum_apples_you_can_buy, remaining_money):
    print(f'Maximum apple you can buy: {Maximum_apples_you_can_buy} pieces.')
    print(f'Your remaining money will be: {remaining_money} pesos.')

def displayMaxApple_Change(Maximum_apples_you_can_buy, remaining_money):
    print(f'You can buy {Maximum_apples_you_can_buy} apples and your change is {remaining_money} pesos.')

# Steps
# 1. Inquire with the user about the amount of money he/she has, the cost of one apple, and save the value to a variable.
money, price = Cash_Price()
# 2. Calculate the maximum number of apples you can buy.
Maximum_apples_you_can_buy = Max_apples(money, price)
# 3. Calculate the remaining money that you will have.
remaining_money = rem_money(money, Maximum_apples_you_can_buy, price)
# 4. Display the maximum numbers of apples you can buy and remaining cash.
displayMaxAppleCanBuy_remainingCash(Maximum_apples_you_can_buy, remaining_money)
# 5. Display the final output. 
displayMaxApple_Change(Maximum_apples_you_can_buy, remaining_money)