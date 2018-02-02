import math
firstBalance=float(input("Enter the initial balance: "))
annualInterestRate=float(input("Enter the annual interest rate: "))

def debtPayFull(firstBalance,annualInterestRate):
    payment=math.floor(firstBalance/12/10)*10
    balance=firstBalance
    while(balance>0):
        balance=firstBalance
        for i in range(0,12):
            unpaidBalance = balance - payment
            balance = unpaidBalance + annualInterestRate / 12 * unpaidBalance
        payment+=10
    return payment-10

print("The amount to be paid monthly to clear debt in one year is: "+str(round(debtPayFull(firstBalance,annualInterestRate),2)))
