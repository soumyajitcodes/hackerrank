def findMedian(arr):
    # Write your code here
    arr.sort()
    index = len(arr) // 2
    return arr[index]


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().split()[:n]))

    result = findMedian(arr)

    print(result)
