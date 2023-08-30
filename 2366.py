from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replacement_num = 0
        cur_max = nums[-1]
        for ind in range(len(nums) - 2, -1, -1):
            el = nums[ind]
            if el <= cur_max:
                cur_max = el
            else:
                # el > cur_max
                cur_replacement_num = el // cur_max

                if el % cur_max:
                    cur_replacement_num += 1
                    cur_max = el // cur_replacement_num

                replacement_num += cur_replacement_num - 1
        return replacement_num
