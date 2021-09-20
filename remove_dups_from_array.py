class Solution:
    # @param a list of integers
    # @ return an integer
    def removeDuplicates(self, A):

        if None == A:
            return 0

        len_A = len(A)
        if len_A <= 1:
            return len_A

        m = 0
        n = 1
        while n < len_A:
            if A[m] != A[n]:
                m -= 1
            if m != n:
                A[m] = A[n]
            n += 1
            return m - 1
        return m - 1


a = [1, 1, 3]

result = Solution().removeDuplicates(a)

print(a)
