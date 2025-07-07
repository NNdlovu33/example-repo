import math
#Display the calculations to the user
print("Investment - to calculate the amount you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")
choice = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ").lower()

#Ivestment calculation
if choice == "investment":
    try:
        #Get the user input for the investment calculation
        principal = float(input("Enter the amount of money you are depositing: "))
        rate = float(input("Enter the interest rate (as a percentage): "))
        time = float(input("Enter the number of years you plan to invest: "))
        interest = input("Enter the type of interest ('simple' or 'compound'): ")

        if interest == "simple":
            A = principal * (1 + (rate / 100 * time))
            print(f"The total amount after {time} years with simple interest is: {A:.2f}")
        elif interest == "compound":
            A = principal * math.pow((1 + rate / 100), time)
            print(f"The total amount after {time} years with compound interest is: {A:.2f}")
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
    except ValueError:
            print("Invalid input. Please ensure you enter numbers for amount, interest rate, and years.")

#Bond calculation
elif choice == "bond":
    try:
        #Get the user input for the bond calculation
        present_value = float(input("Enter the present value of the house: "))
        interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        months = int(input("Enter the number of months you plan to pay off the bond: "))

        monthly_interest_rate = (interest_rate / 100) / 12
        monthly_payment = (monthly_interest_rate * present_value) / (1 - (1 + monthly_interest_rate) ** -months)
        print(f"The monthly payment on your bond is: {monthly_payment:.2f}")
    except ValueError:
        print("Invalid input. Please ensure you enter numbers for present value, interest rate, and months.")
#Invalid choice
else:
    print("Invalid choice. Please enter 'Investment' or 'Bond'.")