class Solution:
    @staticmethod
    def isMonotonic(nums: list[int]) -> bool:
        pos_inc = map(lambda x: x[1] >= nums[x[0]], enumerate(nums[1:]))
        neg_inc = map(lambda x: x[1] <= nums[x[0]], enumerate(nums[1:]))
        return all(pos_inc) or all(neg_inc)


sol = Solution()
numbers = [1,2,4,5]
print(sol.isMonotonic(numbers))
