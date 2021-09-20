# Fibonacci Recursively

# Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with
# a base case checking to see if n = 0 or 1, then it returns 1.
# Else it returns fib(n-1)+fib(n+2).


def fib_rec(n):

    breakpoint()

    if n == 0 or n == 1:
        return n

    else:
        return fib_rec(n-1) + fib_rec(n-2)


result = fib_rec(10)

print(result)
