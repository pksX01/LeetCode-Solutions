def DuplicateZeros(arr):
    skip  = False
    for item_index, item in enumerate(arr):
        if item == 0 and skip == False:
            arr.insert(item_index + 1, 0)
            del arr[-1]
            skip = True
        else:
            skip = False
    return arr

def main():
    nums = list(map(int, input().split()))
    print(DuplicateZeros(nums))

if __name__ == '__main__':
    main()