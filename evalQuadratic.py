def evalQuadratic(a,b,c,x):
    """
        Input are the coefficients of the quadratic equation and the initial guess
        Uses Newton-Raphson
        Output is the correct value of x
    """
    epsilon=0.000001
    while(abs(a*x**2+b*x+c)>epsilon):
        x=x-(a*x**2+b*x+c)/(2*a*x+b)
    print("One of the roots of the quadratic equation is "+str(x))

a=2
b=5
c=-3
x=-10
evalQuadratic(a,b,c,x)
