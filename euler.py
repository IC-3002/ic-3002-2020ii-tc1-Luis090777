
def factorial (n):
    n_factorial = 1
    while(n > 0):
        n_factorial = n_factorial*n
        n = n-1
    return n_factorial 

def e_cuadratica(n):
    i = 0
    r = 0
    while(i<=n):
        r += (1/factorial(i))
        i += 1
    return r

def e_lineal(n):
    i = 0
    r = 0
    factorial = 1
    while(i<=n):
        r += (1/factorial)
        i += 1
        factorial = factorial*i
    return r
