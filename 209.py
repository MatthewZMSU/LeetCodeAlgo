class Solution:
    @staticmethod
    def minSubArrayLen(target: int, nums: list[int]) -> int:
        left = 0  # left - including
        min_length = 10 ** 10
        cur_sum = 0
        for right, el in enumerate(nums):  # right - excluding
            cur_sum += el
            if cur_sum >= target:
                while cur_sum >= target:
                    cur_sum -= nums[left]
                    left += 1
                min_length = min(min_length, right - left + 2)
        return min_length if min_length != 10 ** 10 else 0
