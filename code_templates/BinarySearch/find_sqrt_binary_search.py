# Find the square root using a binary search
class Solution(object):

    def mySqrt(self, x):

        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot

            if num > x:
                right = pivot-1
            elif num < x:
                left = pivot+1
            else:
                return pivot

        return right


s = Solution()

result = s.mySqrt(10)

print(result)
