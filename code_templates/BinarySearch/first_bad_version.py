# Binary Search - First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

""" Complexity analysis

Time complexity : O(log n). 
The search space is halved each time, so the time complexity is O(log n).

Space complexity : O(1). """


class Solution(object):
    def firstBadVersion(self, n):
        """ 
        :type n: int 
        :rtype: int 
        """
        left = 1
        mid = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid - 1

            else:
                left = mid + 1

        return right + 1
