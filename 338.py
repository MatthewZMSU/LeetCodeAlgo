from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        cur_pow = 1
        for ind in range(1, n + 1):
            if ind < cur_pow:
                ans[ind] = ans[ind - cur_pow // 2] + 1
            elif ind == cur_pow:
                ans[ind] = ans[0] + 1
                cur_pow *= 2
        return ans
