def reverseArray(a):
    # Write your code here
    reversedArray = list()

    for i in range(len(a)-1, -1, -1):
        reversedArray.append(a[i])

    return reversedArray


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
