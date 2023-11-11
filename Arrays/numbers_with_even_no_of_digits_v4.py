# This solution works only because of the constraints given in problem i.e. 1 <= nums[i] <= 10^5
from typing import List
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or (num >= 100000 and num <= 999999):
                count += 1
        return count

if __name__ == '__main__':
    print("Enter space separated numbers: ")
    nums = list(map(int, input().split()))
    sol = Solution()
    print(f"{sol.findNumbers(nums)} numbers have even number of digits")