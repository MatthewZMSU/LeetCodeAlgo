class Solution:
    @staticmethod
    def getRow(rowIndex: int) -> list[int]:
        pascals_triangle = [1] * (rowIndex + 1)
        for ind in range(1, rowIndex + 1):
            pascals_triangle[ind] = pascals_triangle[ind - 1] * (rowIndex + 1 - ind) // ind
        return pascals_triangle
