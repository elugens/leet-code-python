# Guess the number higher or lower
# Binary Search


"""
We can apply Binary Search to find the given number. We start with the mid number. 
We pass that number to the guessguess function. If it returns a -1, it implies that the guessed number is larger than the required one.
Thus, we use Binary Search for numbers lower than itself. Similarly, if it returns a 1, we use Binary Search for numbers higher than itself.

Time complexity : O(log_2 n)
Space complexity : O(1). No extra space is used.

"""
# Binary Search Solution


class Solution(object):
    def guessNumber(self, n):

        low = 1
        high = n

        while low <= high:
            mid = low + (high - low)//2
            res = guess(mid)

            if res == 0:
                return mid
            elif res < 0:
                high = mid-1
            else:
                low = mid+1

        return -1
