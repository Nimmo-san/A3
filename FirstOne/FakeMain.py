

# f(x) = 1 - a/x^2
# f'(x) = a/x^3
# Newton-Raphson method
# x_n+1 = x_n - f(x_n)/f'(x_n)

a=4.0;

def func(x):
    return 1 - (a * (1/x**2))


def derivfunc(x):
    return a * (1/x**3)


# Function to find the root
def newtonraphson(x0):
    b = func(float(x0));
    c = derivfunc(float(x0));
    print b
    print c
    print b/c;
    print x0-(b/c);
    while abs(b/c) >= 0.00001:
        b = func(float(x0));
        c = derivfunc(float(x0));
        h =  x0 - (b / c)
        print ("Solution found %.4f" % h);
        x = x0 - (b/c);
        x=x0;


x0 = float((a+1)/2);
newtonraphson(x0)

