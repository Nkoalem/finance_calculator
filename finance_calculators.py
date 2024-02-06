import math

# ask the user to choose the type of investment they would like: to minimise errors associated with capital letters
# .lower() was used
calculation = input(
    "Choose either 'investment' or 'bond' from the menu to proceed: \ninvestment-\tto calculate the amount of "
    "interest you'll earn on interest \nbond- \tto calculate the amount you'll have to pay on a home loan \n").lower()

# if the user chooses investment,ask them to input a series of data:
if calculation == 'investment':
    dep_amount = float(input("Please enter the amount you'd like to deposit: "))
    interest_rate = float(input("Please enter the interest rate: "))
    years = int(input("Enter the number of years for the investment: "))
    interest = input("Select the type of interest : 'simple' or 'compound' ").lower()
    # declared the variables again, so they can use  in the calculations:
    # interest rate divided by 100 to get its decimal form, so we can use it in the calculation/formula.
    r = interest_rate / 100
    t = years
    p = dep_amount

    # if the user chose simple/compound interest in the previous If statement for calculation,one of the following
    # calculation gets executed:
    if interest == 'simple':
        total_amount = p * (1 + r * t)
        print(int(total_amount))

    if interest == 'compound':
        total_amount = p * math.pow((1 + r), t)
        print(int(total_amount))

# elif condition gets executed if the user chose 'bond' as a calculation(line 1)
elif calculation == 'bond':
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months the bond will be repaid: "))
    # declare the variables, so they can be used in the calculation:
    decimal_rate = interest_rate / 100
    p = present_value
    i = decimal_rate
    n = months
    monthly_repayments = (i / 12) * (1 / (1 - (1 + i / 12) ** (-n))) * p
    print(round(monthly_repayments, 2))

# the else statement gets executed if the user has not made a valid Calculation selection in line one
else:
    print("Please make a valid selection.")

# reference: Discord
# reference: http://www.statology.org/python-monthly-payment-function/

