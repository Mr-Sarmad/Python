def factorial(n):
    '''it takes a num and give factorial of it '''
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial(9))
print(factorial.__doc__)

def f(n):
    '''its take a number and gave us a fibonannci sequence'''
    if(n==0 or n==1):
        return 1
    else:
        xf=f(n-1)+f(n-2)
        return xf
    
print(f(9))
print(f.__doc__)