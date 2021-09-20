# Problem 1 in Recursion Chapter
# Write a recursive function which takes an integer
# and computes the cumulative sum of 0 to that integer


def rec_sum(n):

    if n == 0:
        return 0

    else:
        return n + rec_sum(n-1)


result = rec_sum(5)

print(result)
