def mergeSortedArray(nums1, m, nums2, n):
    del nums1[-n:-1]
    return nums1

def main():
    nums1 = list(map(int, input().split))
    nums2 = list(map(int, input().split))
    nums1_size = len(nums1)
    nums2_size = len(nums2)
    print(mergeSortedArray(nums1, nums1_size, nums2, nums2_size))

if __name__ == '__main__':
    main()