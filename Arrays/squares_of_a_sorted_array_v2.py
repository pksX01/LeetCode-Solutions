from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) #5
        squared_nums = [0 for i in range(n)]
        left, right, iter = 0, n-1, n-1
        while iter >= 0:
            if abs(nums[left]) > abs(nums[right]):
                squared_nums[iter] = nums[left] ** 2
                left += 1
            else:
                squared_nums[iter] = nums[right] ** 2
                right -= 1
            iter -= 1
        return squared_nums

if __name__ == '__main__':
    print("Enter the space separated numbers: ")
    nums = list(map(int, input().split()))
    sol = Solution()
    print("Squares of the numbers sorted in non - decreasing order: ", sol.sortedSquares(nums))