from typing import List, Optional


class Solution:
    def __init__(self):
        self.ranges: list = None

    def minTaps(self, n: int, ranges: List[int]) -> int:
        self.ranges = [(ind, (ind - radius, ind + radius)) for ind, radius in enumerate(ranges)]
        self._make_ranges(0, n)



        cur_coverage = [-1, -1]  # (a, b) -> it covers [a, b]
        opened_taps = 0

        for point in range(n + 1):
            if cur_coverage[0] <= point <= cur_coverage[1]:
                pass  # Everything is good!
            else:
                left, right = self._find_maximum_coverage(point)

                if left == right == -1:
                    return -1
                if left > cur_coverage[1] or right < cur_coverage[0]:
                    return -1

                if left <= cur_coverage[0]:
                    cur_coverage[0] = left
                if right >= cur_coverage[1]:
                    cur_coverage[1] = right
                opened_taps += 1
        return opened_taps

    def _make_ranges(self, left: int, right: int):
        def __cut_range(coverage: tuple) -> tuple:
            if coverage[0] < left:
                coverage = (left, coverage[1])
            if coverage[1] > right:
                coverage = (coverage[0], right)
            return coverage

        self.ranges = sorted(((ind, __cut_range(coverage)) for ind, coverage in self.ranges),
                             key=lambda el: el[1][1] - el[1][0])

    # def _find_maximum_coverage(self, point):
    #     max_dist, cover_ind = -1, -1
    #     for ind, (left, right) in enumerate(self.ranges):
    #         if left <= point <= right and (d := right - left) >= max_dist:
    #             max_dist = d
    #             cover_ind = ind
    #     try:
    #         return self.ranges.pop(cover_ind)
    #     except IndexError:
    #         return -1, -1


sol = Solution()
array = [4, 1, 5, 0, 5, 3, 3, 3, 0, 0, 3, 3, 2, 2, 4, 4, 2, 3, 4, 2]
print(sol.minTaps(len(array) - 1, array))
