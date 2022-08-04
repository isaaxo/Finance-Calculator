import math

# Below are two financial calculators for investment and bond.
# The investment calculator has two formulas, simple interest & compound interest.
# The lower() method is used to validate the user inputs even if the format is upper case or mixed case.

# Requesting user to choose between investment and bond calculator
choose_calculator = input("Choose either the 'investment' or 'bond' from the menu below to proceed: \n"
                          "\ninvestment       - to calculate the amount of interest you'll earn on interest "
                          "\nbond             - to calculate the amount of interest you'll earn on interest: \n")

# Printing out an error message to the user
choose_calculator = choose_calculator.lower()
if choose_calculator != 'investment' and choose_calculator != 'bond':

    print("You have entered a wrong selection, please check your spelling and try again.\n")
    choose_calculator = input("Choose either the 'investment' or 'bond' from the menu below to proceed: \n"
                              "\ninvestment       - to calculate the amount of interest you'll earn on interest "
                              "\nbond             - to calculate the amount of interest you'll earn on interest: \n")

# Calculating investment
if choose_calculator == 'investment':
    choose_calculator = choose_calculator.lower()

    # Requesting the user for inputs
    money_depositing = float(input("Please enter the amount of money to be deposited: \n"))
    interest_rate = int(input("Enter interest rate: \n"))
    years = int(input("Enter number of years for your investment: \n"))

    # Choosing between compound and simple interest
    interest = input("Do you want 'simple' or 'compound' interest: \n")
    interest = interest.lower()

    # Calculating final amount using simple interest
    if interest == 'simple':

        # Assigning values to the formula's variables
        P = money_depositing
        r = interest_rate / 100
        t = years

        # Formula for calculating simple interest
        A = P * (1 + r * t)

        # Rounding to two decimal place
        A = round(A, 2)
        print(f"\nThe final amount when using simple interest with monthly payment of R{P} \n"
              f"for {years} years with an interest of {interest_rate}% is R{A}")

    # Calculating final amount using compound interest
    else:
        # Assigning values to the formula's variables
        P = money_depositing
        r = interest_rate / 100
        t = years

        # Formula for calculating compound interest
        A = P * math.pow((1 + r), t)

        # Rounding to two decimal place
        A = round(A, 2)
        print(f"\nThe final amount when using compound interest with monthly payment of R{P} \n"
              f"for {years} years with an interest of {interest_rate}% is R{A}")

# Calculating bond payment
else:

    # Requesting inputs from user
    present_value_ = int(input("Please enter the present value: \n"))
    interest_rate = int(input("Enter interest rate: \n"))
    number_of_months = int(input("Enter number of months to repay the bond: \n"))

    # Assigning values to the formula's variables
    P = present_value_
    n = number_of_months
    i = interest_rate / 12

    # Rounding to two decimal place
    i = round(i, 2)

    # Calculating the total amount to be repaid
    x = (i*P)/(1 - math.pow((1 + i), (-n)))
    x = round(x, 2)
    print(f"\nThe total amount to be repaid is R{x} with an interest of {i} \n"
          f"with a present value of R{P} that is paid for a period of  {n} months.")



