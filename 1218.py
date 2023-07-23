from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        next_numbers = defaultdict(int)  # next_number : cur_len
        for el in arr:
            cur_len = next_numbers.pop(el, 0)
            next_numbers[el + difference] = max(next_numbers[el + difference], cur_len + 1)
        return max(next_numbers.values())
