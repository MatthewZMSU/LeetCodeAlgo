from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        letter_counter = Counter({'a': 0, 'b': 0, 'c': 0})
        for ind, char in enumerate(s):
            letter_counter.update(char)
            while all(letter_counter.values()):
                count += len(s) - ind
                letter_counter.subtract(s[left])
                left += 1
        return count
