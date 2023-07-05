class Solution:
    def ternary(self, n):
        if n == 0:
            return '0'
        if n < 0:
            return self.ternary(-n)
        ternary_number = ''
        while n:
            n, r = divmod(n, 3)
            ternary_number += str(r)
        return ternary_number[::-1]

    def add_ternary(self, a: str, b: str):
        if len(a) < len(b):
            return self.add_ternary(b, a)
        if (length := len(a) - len(b)) > 0:
            return self.add_ternary(a, '0' * length + b)

        # Now we have len(a) == len(b)
        result = ''
        for ind in range(len(a)):
            result += str((int(a[ind]) + int(b[ind])) % 3)
        return result

    def singleNumber(self, nums: list[int]) -> int:
        pos_triple_sum, neg_triple_sum = '0', '0'
        for el in nums:
            if el >= 0:
                pos_triple_sum = self.add_ternary(pos_triple_sum, self.ternary(el))
            else:
                neg_triple_sum = self.add_ternary(neg_triple_sum, self.ternary(el))
        pos_triple_sum = int(pos_triple_sum, 3)
        neg_triple_sum = int(neg_triple_sum, 3)
        return pos_triple_sum if pos_triple_sum else -neg_triple_sum


sol = Solution()
print(sol.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
