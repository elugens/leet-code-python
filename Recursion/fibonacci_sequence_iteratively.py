def fib_iter(n):

    # Set Starting Poin
    a, b = 0, 1

    # Follow Algorithm
    for i in range(n):

        a, b = b, a+b

    return a


result = fib_iter(10)

print(result)
