def odd(number):
    return bool(number%2)

number=int(input("Enter the number to be checked: "))
print("The number is odd"*int(odd(number))+"The number is even"*int(odd(number+1)))
