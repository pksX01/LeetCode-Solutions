from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                count += 1
                maxCount = max(count, maxCount)
            else:
                count = 0
        return maxCount


if __name__ == '__main__':
    print("Enter the array of space separated 0s and 1s: ")
    lst = list(map(int, input().split()))
    sol = Solution()
    print("Maximum number of consecutive Ones are: ", sol.findMaxConsecutiveOnes(lst))