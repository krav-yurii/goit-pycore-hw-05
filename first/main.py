def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        if n < 0:
            raise ValueError("n must be a non-negative integer")

        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))   
print(fib(15))  