# Fibonacci Sequence - Dynamically
# In the form it is implemented here, the cache is set beforehand
# and is based on the desired n number of the Fibonacci Sequence.
# Note how we check it the cache[n] != None, meaning we have a check
# to know wether or not to keep setting the cache (and more importantly
# keep cache of old results!)
# ------------------------ Code Starts Below  ---------------

# Instantiate Cache information

n = 10
cache = [None] * (n+1)


def fib_dynamic(n):

    # breakpoint()

    # Base Case
    if n == 0 or n == 1:
        return n

    # Check Cache

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dynamic(n-1) + fib_dynamic(n-2)

    return cache[n]


result = fib_dynamic(10)

print(result)
