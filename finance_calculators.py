import math


def investment_calculator() -> None:
    """
    This function calculates accumulation of interests using
    simple interest & compound interest.
    :return:
    """

    while True:
        try:
            # Requesting the user for inputs
            print("Welcome to the investment calculator.")
            money_depositing: float = float(input("Please enter the amount of money to be deposited: \n"))
            interest_rate: int = int(input("Enter interest rate: \n"))
            years: int = int(input("Enter number of years for your investment: \n"))
            interest: int = int(input("Do you want 'simple' or 'compound' interest: \n"
                                      "Enter 1 for simple interest and 2 for compound interest: \n"))

            # Calculating final amount using simple interest
            if interest == 1:
                # Assigning values to the formula's variables
                p = money_depositing
                r = interest_rate / 100
                t = years

                # Formula for calculating simple interest
                a = p * (1 + r * t)

                # Rounding to two decimal place
                a = round(a, 2)
                print(f"\nThe final amount when using simple interest with monthly payment of R{p} \n"
                      f"for {years} years with an interest rate of {interest_rate}% is R{a}\n")
                break

            if interest == 2:
                # Assigning values to the formula's variables
                p = money_depositing
                r = interest_rate / 100
                t = years

                # Formula for calculating compound interest
                a = p * math.pow((1 + r), t)

                # Rounding to two decimal place
                a = round(a, 2)
                print(f"\nThe final amount when using compound interest with monthly payment of R{p} \n"
                      f"for {years} years with an interest rate of {interest_rate}% is R{p}\n")
                break

        except ValueError:
            print("Wrong selection try again: ")
            continue


def bond_calculator() -> None:
    """
    This function calculates the amount to be paid on monthly basis for a bond.
    :return:
    """
    while True:
        try:
            print("Welcome to the bond calculator.")
            # Requesting inputs from user
            present_value_: int = int(input("Please enter the present value: \n"))
            interest_rate: int = int(input("Enter interest rate: \n"))
            number_of_months: int = int(input("Enter number of months to repay the bond: \n"))

            # Assigning values to the formula's variables
            p = present_value_
            n = number_of_months
            i = interest_rate / 12

            # Rounding to two decimal place
            i = round(i, 2)

            # Calculating the total amount to be repaid
            x = (i * p) / (1 - math.pow((1 + i), (-n)))
            x = round(x, 2)
            total = x + p
            print(f"\nThe amount to be paid every month is R{x} with an interest rate of {i}% \n"
                  f"with a present value of R{p} that is paid for a period of  {n} months, \nand it will accumulate to"
                  f" R{total}\n")
            break

        except ValueError:
            print("Wrong input please enter numbers only, try again: ")
            continue


def main() -> None:
    """
    This function serves as the entry point this software, it provides the user with options
    to use the software
    :return:
    """
    while True:
        choose_calculator: str = input("Enter i for investment and b for bond: "
                                       "\n-investment to calculate the amount of interest you'll earn on interest "
                                       "\n-bond to calculate the amount of interest you'll pay: \n").lower()

        menu: list = ['i', 'b']

        if choose_calculator == 'i':
            investment_calculator()

        if choose_calculator == 'b':
            bond_calculator()

        if choose_calculator not in menu:
            print("Wrong selection please enter i or b, try again: ")
            continue


if __name__ == '__main__':
    main()
