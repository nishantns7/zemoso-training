def square(x):
    """
        Input is a number
        Output is the square of the input number
    """
    return x*x

s=input("Enter the number whose square is to be calculated: ")
if '.' in s:
    n=float(s)
else:
    n=int(s)
print(square(n))
