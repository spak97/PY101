print("Welcome to mortgage/car loan calculator")
loan_amt = input("Enter loan amount in dollars: ")
apr = float(input("Enter APR in percentage: ")) * 0.01
loan_duration = int(input("Enter loan duration in months: "))

monthly_int = apr / 12
monthly_paymnt = float(loan_amt) * (monthly_int / (1 - (1 + monthly_int) ** (-(loan_duration))))

print(f"Your monthly payment amount is: ${monthly_paymnt}")


