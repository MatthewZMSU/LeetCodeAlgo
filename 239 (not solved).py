from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.skip_times = 0
        self.window = None
        self.cur_max = None

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        clearing_number = 10 if 10 < k else k
        max_in_windows = []
        self.window = deque(nums[i] for i in range(k - 1))
        self.cur_max = max(self.window)
        for i in range(k - 1, len(nums)):
            el = nums[i]
            if el > self.cur_max:
                # Todo: tp change this part
                self.cur_max = el
                max_in_windows.append(self.cur_max)
                self.window = [el]
                self.skip_times = k - 1
            elif self.skip_times:
                self.skip_times -= 1
                max_in_windows.append(self.cur_max)
                self.window.append(el)
            else:
                # el <= self.cur_max and self.skip_times = 0
                tmp_max = self.window[0]
                for j in range(1, clearing_number):
                    if self.window[j] > tmp_max:
                        tmp_max = self.window[j]
                        self.skip_times += 1
                    else:
                        break


        return max_in_windows
