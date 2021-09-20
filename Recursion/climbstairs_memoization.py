def climbStairs(self, n):

    cache = [None]*(n+1)
    return self._helper(n, cache)


def _helper(self, n, cache):
    if n < 0:
        return 0

    if n == 1 or n == 0:
        return 1

    if cache[n]:
        return cache[n]

    cache[n] = self._helper(n-1, cache) + self._helper(n-2, cache)

    return cache[n]


climbStairs(self, 10)
