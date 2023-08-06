def miniMaxSum(arr):
    arr.sort()

    # minimum sum
    print(sum(arr[:4]), end=" ")
    # maximum sum
    print(sum(arr[1:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
