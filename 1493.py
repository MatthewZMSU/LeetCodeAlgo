class Solution:
    def find_two_subarrays(self, nums: list[int]) -> int:
        left_array, right_array = 0, 0
        max_length = 0
        zero_occurance = False
        for el in nums:
            if el == 0:
                if not zero_occurance:
                    max_length = max(max_length, left_array + right_array)
                zero_occurance = True
                left_array = right_array
                right_array = 0
            else:
                zero_occurance = False
                right_array += 1
        return max(max_length, left_array + right_array)

    def longestSubarray(self, nums: list[int]) -> int:
        return length if ((length := self.find_two_subarrays(nums)) != len(nums)) else length - 1
