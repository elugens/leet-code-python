def climbStairs(n):

    cache = {}

    def helper(n):
        if n == 1 or n == 2:
            return n
        elif n in cache:
            return cache[n]
        else:
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]

    return helper(n)


c = climbStairs(4)

print('How many ways: ', c)
