def fact(n):

    # Base Case
    if n == 0:
        return 1

    else:
        # Recursive Call
        return n * fact(n-1)


result = fact(5)

print(result)
