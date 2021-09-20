class Solution:
    def twoSum(self, nums, target):

        if len(nums) < 2:
            return

        # Sets for track
        seen = set()
        output = set()

        for num in nums:

            numbers = target-num

            if numbers not in seen:
                seen.add(num)

            else:
                output.add(((min(num, numbers)), max(num, numbers)))

        print('\n'.join(map(str, list(output))))


total = Solution()

total.twoSum([2, 7, 11, 15], 9)
