def evalQuadratic(a,b,c,x):
    """
        Input are the coefficients of the quadratic equation and the initial guess
        Uses Newton-Raphson
        Output is the value of ax^2 + bx + c
    """
    return a*x*x + b*x + c

a=2
b=5
c=-3
x=-10
print(evalQuadratic(a,b,c,x))
