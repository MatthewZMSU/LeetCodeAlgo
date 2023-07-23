from math import sqrt


class Solution:
    @staticmethod
    def distributeCandies(candies: int, num_people: int) -> list[int]:
        candies_distribution = [0] * num_people
        # We are going to solve for maximum k: k(k + 1) / 2 <= candies.
        k = int((-1 + sqrt(1 + 8 * candies)) / 2)
        # That is number of people with expected candies (maybe + 1 to people)

        full_rows = k // num_people
        for i in range(1, num_people + 1):
            candies_distribution[i - 1] = full_rows * (2 * i + num_people * (full_rows - 1)) // 2
            candies -= candies_distribution[i - 1]

        base_candies = full_rows * num_people + 1
        for i in range(num_people):
            if candies <= base_candies + i:
                candies_distribution[i] += candies
                break
            candies_distribution[i] += base_candies + i
            candies -= base_candies + i

        return candies_distribution


sol = Solution()
print(sol.distributeCandies(60, 5))