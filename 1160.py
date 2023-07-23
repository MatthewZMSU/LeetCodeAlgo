from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        sum_len = 0
        base_cnt = Counter(chars)
        for word in words:
            cmp_cnt = Counter(word)
            if cmp_cnt <= base_cnt:
                sum_len += len(word)
        return sum_len
