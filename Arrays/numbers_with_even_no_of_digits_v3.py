from typing import List
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            numDigits = math.floor(math.log10(num)) + 1
            if numDigits % 2 == 0:
                count += 1
        return count

if __name__ == '__main__':
    print("Enter space separated numbers: ")
    nums = list(map(int, input().split()))
    sol = Solution()
    print(f"{sol.findNumbers(nums)} numbers have even number of digits")