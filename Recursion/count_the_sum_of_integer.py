# Problem 2
# Given an integer, create a function which returns the sum of all the
# individual digits in that integer. For example: if n = 4321, return 4+3+2+1


def sum_func(n):

    # Base case
    if n == 0:
        return 0
    else:
        # recursive solution
        return n % 10 + sum_func(n//10)


result = sum_func(4562)

print(result)
