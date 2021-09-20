class Solution:

    def search(self, nums, target):

        left = 0
        right = len(nums)-1

        while left <= right:

            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid+1

            else:
                right = mid-1

        return -1


nums = [2, 3, 4, 10, 40]

s = Solution()

result = s.search(nums, 4)

print(result)
