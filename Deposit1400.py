#name: Connor
#date: 10/6
#description: claculate the future value of a monthly deposit

#dec vars 
rate = 0.0 #intreset rate 
deposit = 0.0#deposit amount
months = 0.0#number of months 
fv = 0.0#future value

#greeting
print("Welecome to the Future Values calculator. It will calculate the future value of a deposit amount ")

#prompt monthly deposit, intrest rate, and the number of months to deposit.
deposit = float(input("what in the deposit amount:"))
rate = float(input("Enter the interest rate (example 2.5 or 10.25):"))
months = int(input("How many months will this be deposited (1 or greater):"))
#calculate the future - fv = (fv + deposit) * (1 + rate)
for count in range(1, months+1):
    fv = (fv + deposit) * (rate + 1)

#display results 
#if you deposit $25 a month for 3 months at 5% intreset, you will have $180000
print(f"if you deposit ${deposit:.2f} a month for {months} months at a {rate:.1f}% intreset rate, you will have ${fv:.2f}")

#graceful close 
print("This is a good reason to save money")
