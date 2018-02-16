firstBalance=float(input("Enter the initial balance: "))
annualInterestRate=float(input("Enter the annual interest rate as a decimal: "))

def debtPayFullBisect(firstBalance,annualInterestRate):
    payLower=firstBalance/12
    payUpper=firstBalance*((1+annualInterestRate/12)**12)/12
    balance=firstBalance
    while(abs(balance)>0.009):
        balance=firstBalance
        payment=(payUpper+payLower)/2
        for i in range(0,12):
            unpaidBalance = balance - payment
            balance = unpaidBalance + annualInterestRate / 12 * unpaidBalance
        if(balance>0.009):
            payLower=payment
        else:
            payUpper=payment
    return payment

print("The amount to be paid monthly to clear debt in one year is: "+str(round(debtPayFullBisect(firstBalance,annualInterestRate),2)))
