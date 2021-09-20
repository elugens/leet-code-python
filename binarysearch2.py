
# Binary Search on an ordered list returning indice position


class Solution:
    def search(self, nums, target):

        # Tuple unpacking
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = left + (right - left) // 2

            if nums[pivot] == target:
                return pivot

            if target < nums[pivot]:
                right = pivot - 1

            else:
                left = pivot + 1

        return -1


nums = [-1, 0, 3, 5, 9, 12]

q = Solution()

result = q.search(nums, 3)

print(result)
