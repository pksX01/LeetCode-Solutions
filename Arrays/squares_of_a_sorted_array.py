from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [num ** 2 for num in nums]
        return sorted(squared_nums)

if __name__ == '__main__':
    print("Enter the space separated numbers: ")
    nums = list(map(int, input().split()))
    sol = Solution()
    print("Squares of the numbers sorted in non - decreasing order: ", sol.sortedSquares(nums))