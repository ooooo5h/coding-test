def fibonacci(n) :
    if n == 0 :
        return n
    
    elif n == 1 :
        return n
    
    else :
        n = fibonacci(n-1) + fibonacci(n-2)
        return n

print(fibonacci(int(input())))