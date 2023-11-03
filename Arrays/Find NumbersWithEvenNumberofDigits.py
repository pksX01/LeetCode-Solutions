def numsWithEvenNoOfDigits(nums):
    occur_lst = []
    count = 0
    for num in nums:
        noOfDigits = findNoOfDigits(num)
        occur_lst.append(noOfDigits)
    for val in occur_lst:
        if val % 2 == 0:
            count += 1
    return count

def findNoOfDigits(num):
    noOfDigits = 0
    while (num//10 > 0):
        noOfDigits += 1
        num = num//10
    return noOfDigits + 1

def main():
    nums = list(map(int, input().split()))
    print(numsWithEvenNoOfDigits(nums))

if __name__ == "__main__":
    main()