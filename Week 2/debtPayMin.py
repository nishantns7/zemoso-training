balance=float(input("Enter the initial balance: "))
annualInterestRate=float(input("Enter the annual interest rate: "))
monthlyPaymentRate=float(input("Enter the minimum monthly payment rate: "))

def debtPayMin(balance,annualInterestRate,monthlyPaymentRate):
    for i in range(0,12):
        unpaidBalance = balance - balance * monthlyPaymentRate
        balance = unpaidBalance + annualInterestRate / 12 * unpaidBalance
    return balance

print("The remaining balance after a year is: "+ str(round(debtPayMin(balance,annualInterestRate,monthlyPaymentRate),2)))
