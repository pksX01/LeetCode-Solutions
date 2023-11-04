from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            numOfDigits = 0
            while (num // 10) > 0:
                numOfDigits += 1
                num //= 10
            numOfDigits += 1
            if numOfDigits % 2 == 0:
                print('Number is: ', num)
                count += 1
        return count

if __name__ == '__main__':
    print("Enter space separated numbers: ")
    nums = list(map(int, input().split()))
    sol = Solution()
    print(f"{sol.findNumbers(nums)} numbers have even number of digits")