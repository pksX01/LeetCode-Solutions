def main():
    nums = list(map(int, input().split()))
    squared_nums = []
    for item in nums:
        squared_nums.append(item ** 2)
    print(sorted(squared_nums))


if __name__ == '__main__':
    main()