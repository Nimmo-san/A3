
# f(x) = 1 - a/x^2
# f'(x) = a/x^3
# Newton-Raphson method
# x_n+1 = x_n - f(x_n)/f'(x_n)

a=4.0;

## Original function
def func(x):
    return 1 - (a * (1/x**2))

## Derivative of OF
def derivfunc(x):
    return 2 * a * (1/x**3)


## Function to find the root
## Using the Newton-Raphson method
def newtonraphson(x0):
    b = func(float(x0));
    c = derivfunc(float(x0));
    
    while abs(b/c) >= 0.000001:
        b = func(x0);
        c = derivfunc(x0);
        h =  x0 - (b / c)
        print ("Solution found %.6f" % h);
        x0=h;

## Starting root
x0 = float((a+1)/2);
newtonraphson(x0)


