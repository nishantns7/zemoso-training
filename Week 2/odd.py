def odd(number):
    return bool(number%2)

if(odd(int(input("Enter number to be checked: ")))):
    print("The number is odd.")
else:
    print("The number is even.")
