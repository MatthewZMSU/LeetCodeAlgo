class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_el = -1
        for ind in range(len(arr) - 1, -1, -1):
            arr[ind], max_el = max_el, max(max_el, arr[ind])
        return arr
