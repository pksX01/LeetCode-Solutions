def calc_mex(lst):
    max_ele = max(lst)
    mex = 1
    for num in range(0, max_ele):
        if num not in lst:
            mex = num
            break
    else:
        mex = max_ele + 1
    return mex


def main():
    t = int(input())
    for j in range(t):
        n =  int(input())
        arr = list(map(int, input().split()))
        for i in range(0, n):
            left_mex = calc_mex(arr[:i+1])
            right_mex = calc_mex(arr[i+1:])
            if left_mex == right_mex:
                print(i+1)
                break
            else:
                continue
        else:
            print("-1\n")

if __name__ == "__main__":
    main()
