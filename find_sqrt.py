# Newton's Method - The best way to find the square root of a number.
# NEWTONS METHOD EXAMPLE

# Binary Solution


class Solution:
    def mySqrt(self, x):

        # Base case
        if x < 2:
            return x

        x0 = x
        x1 = (x0 + x / x0) / 2

        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2

        return int(x1)


s = Solution()

result = s.mySqrt(4)

print(result)


# Newtons Method 2
# iterative solution

def mySqrt2(x):

    numiter = 500

    a = float(x)  # number to get square root of

    for i in range(numiter):  # iteration number
        x = 0.5 * (x + a / x)  # update
        # x_(n+1) = 0.5 * (x_n +a / x_n)

    return int(x)


print(mySqrt2(700))
