def findMaxConsecutiveOnes(nums):
    count = 0
    consecutiveOnes = []
    for index, item in enumerate(nums):
        if item == 1 and index == len(consecutiveOnes):
            count += 1
            consecutiveOnes.append(count)
        
        elif item ==1 and index != len(consecutiveOnes):
            count += 1
        
        else:
            consecutiveOnes.append(count)
            count = 0
    print(consecutiveOnes, end='\n')
    return max(consecutiveOnes)


def main():
    nums = list(map(int, input().split()))
    print(findMaxConsecutiveOnes(nums))


if __name__ == "__main__":
    main()

