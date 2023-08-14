from typing import List


class Solution(object):
    def validPartition(self, nums: List[int]) -> bool:
        # ... , c, b, a, ...
        if len(nums) == 2:
            return nums[0] == nums[1]
        if len(nums) == 3:
            c, b, a = nums
            return a == b == c or a - b == b - c == 1

        partition_number = [0] * (len(nums) + 3)
        partition_number[1] = int(nums[0] == nums[1])
        c, b, a = nums[0:3]
        partition_number[2] = sum([a == b == c, a - b == b - c == 1])

        for ind in range(3, len(nums)):
            a = nums[ind]
            if ind - 1 >= 0:
                b = nums[ind - 1]
                if b == a:
                    prev = partition_number[ind - 2]
                    partition_number[ind] += prev
                if ind - 2 >= 0:
                    c = nums[ind - 2]
                    if c == b == a:
                        prev = partition_number[ind - 3]
                        partition_number[ind] += prev
                    elif a - b == b - c == 1:
                        prev = partition_number[ind - 3]
                        partition_number[ind] += prev
        return bool(partition_number[-4])


sol = Solution()
print(sol.validPartition([579611,579611,579611,731172,731172,496074,496074,496074,151416,151416,151416]))
