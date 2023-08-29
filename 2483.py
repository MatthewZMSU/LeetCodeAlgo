class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_hour, min_penalty = 0, customers.count('Y')
        cur_penalty = min_penalty
        for hour, customer in enumerate(customers, start=1):
            if customer == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                best_hour = hour
        return best_hour
