from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                for j in range(n-1, i, -1):
                    arr[j] = arr[j-1]
                i += 1
            i += 1
        print(arr)

if __name__ == '__main__':
    print("Enter space separated values of an array: ")
    arr = list(map(int, input().split()))
    sol = Solution()
    print("Array after modification: ")
    sol.duplicateZeros(arr)
