def fibo (n): 
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a


def fibonacci (n): 
    if n <= 1: 
        return n
    return(fibonacci(n-1) + fibonacci(n-2))

for i in range (10): 
    print(fibo(i))

print ()

for i in range (10): 
    print(fibonacci(i))